"""Wafi, the parent-enquiry assistant of Rawafid Schools Group, as Dana built it.

This is the build the course makes lawful and responsible. It is deliberately not: the first
prompt builder sends the whole student record, the log keeps every prompt, and the router that
sends sensitive enquiries to staff knows English keywords only.

    import wafi
    bot = wafi.Wafi()                         # Dana's build, as found
    out = bot.handle("0551234567", "How many days has Sara missed this term?")
    out["reply"], out["escalated"], bot.log[-1]

Models:
- WAFI_MODEL=standin (or no OPENROUTER_API_KEY): a scripted stand-in model that writes the reply
  from the facts in the prompt with fixed templates. It runs without a key and gives the same
  result every time. It is not a language model: it imitates one weakness on purpose (it reads
  Modern Standard Arabic phrasings better than Gulf Arabic ones).
- Otherwise a free hosted model on OpenRouter (WAFI_HOSTED_MODEL, default below). Use it only
  with this synthetic data: a hosted endpoint outside the Kingdom is a transfer of whatever the
  prompt carries.
If the hosted call fails (no key, 401, 429, no network) the stand-in answers and `model` in the
result says so.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

import rawafid as U

HOSTED_MODEL = os.environ.get("WAFI_HOSTED_MODEL", "google/gemma-4-31b-it:free")
FALLBACK_MODEL = "google/gemma-4-26b-a4b-it:free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
ARABIC = re.compile(r"[؀-ۿ]")


def is_arabic(text: str) -> bool:
    return bool(ARABIC.search(text or ""))


# ------------------------------------------------------------------ the records Wafi reads
class Records:
    """The student information system and the fee system, read through one object."""

    def __init__(self):
        self.guardians = {g["guardian_id"]: g for g in U.load("guardians.csv").to_dict("records")}
        self.students = U.load("students.csv").to_dict("records")
        self.by_mobile = {g["mobile"]: g for g in self.guardians.values()}
        self.children = defaultdict(list)
        for s in self.students:
            self.children[s["guardian_id"]].append(s)
        self.events = defaultdict(list)
        for a in U.load("attendance.csv").to_dict("records"):
            self.events[a["student_id"]].append(a)
        self.fees = {f["student_id"]: f for f in U.load("fees.csv").to_dict("records")}

    def child_named(self, guardian_id: str, text: str) -> dict | None:
        kids = self.children.get(guardian_id, [])
        for s in kids:
            if s["full_name"].split()[0] in text or s["full_name_ar"].split()[0] in text:
                return s
        return kids[0] if kids else None

    def facts(self, student_id: str) -> dict:
        ev = self.events.get(student_id, [])
        return {"absences_this_term": sum(1 for e in ev if e["status"] == "absent"),
                "lates_this_term": sum(1 for e in ev if e["status"] == "late"),
                "balance": int(self.fees[student_id]["balance"])}


# ------------------------------------------------------------------ prompt builders
def build_prompt_v1(text: str, student: dict, guardian: dict, facts: dict) -> dict:
    """Dana's prompt builder: the whole student record, the guardian, and the derived facts."""
    record = dict(student)
    record["guardian"] = {k: guardian[k] for k in ("full_name", "national_id", "mobile", "relationship")}
    record.update(facts)
    fields = ([f"student.{k}" for k in student] + [f"guardian.{k}" for k in record["guardian"]] +
              [f"derived.{k}" for k in facts] + ["enquiry.text"])
    prompt = ("You are Wafi, the parent-enquiry assistant of Rawafid Schools. Answer the guardian in the language "
              f"of the message.\nStudent record: {json.dumps(record, ensure_ascii=False)}\nGuardian message: {text}")
    return {"text": prompt, "fields": fields}


def build_prompt_min(text: str, student: dict, guardian: dict, facts: dict) -> dict:
    """The minimised builder of Lab 1.2: the child's first name and three counts, nothing else."""
    name = (student["full_name_ar"] if is_arabic(text) else student["full_name"]).split()[0]
    data = {"first_name": name, **facts}
    prompt = ("You are Wafi, the parent-enquiry assistant of Rawafid Schools. Answer the guardian in the language "
              f"of the message, using only these facts.\nFacts: {json.dumps(data, ensure_ascii=False)}\n"
              f"Guardian message: {text}")
    return {"text": prompt, "fields": ["student.first_name"] + [f"derived.{k}" for k in facts] + ["enquiry.text"]}


# ------------------------------------------------------------------ routing
ROUTER_V1 = ["medication", "allergy", "sick", "bullied", "bullying", "hurting", "charged twice", "dispute",
             "complaint", "custody", "insulin", "nurse", "شكوى", "تنمر"]


def route_v1(text: str) -> bool:
    """True when the enquiry must go to a member of staff. Dana's list."""
    t = text.lower()
    return any(k in t for k in ROUTER_V1)


# ------------------------------------------------------------------ models
EN_INTENTS = [("absences", r"absen|missed"), ("lates", r"late"), ("balance", r"balance|owe|paid|fee")]
AR_INTENTS = [("absences", r"أيام غياب|عدد أيام"), ("lates", r"تأخر"), ("balance", r"المبلغ المتبقي|رسوم")]
TEMPLATES = {
    ("absences", "en"): "Thank you for your message. {n} has been absent on {v} school days this term.",
    ("lates", "en"): "Thank you for your message. {n} has arrived late {v} times this term.",
    ("balance", "en"): "Thank you for your message. The remaining balance for {n} this term is SAR {v}.",
    ("absences", "ar"): "شكرًا لتواصلكم. عدد أيام غياب {n} في هذا الفصل: {v}.",
    ("lates", "ar"): "شكرًا لتواصلكم. عدد مرات تأخر {n} في هذا الفصل: {v}.",
    ("balance", "ar"): "شكرًا لتواصلكم. المبلغ المتبقي على {n} لهذا الفصل: {v} ريال.",
    ("other", "en"): "Thank you for your message. A member of our team will look into it and reply to you.",
    ("other", "ar"): "شكرًا لتواصلكم. سيتابع أحد أعضاء الفريق رسالتكم ويرد عليكم.",
}
FACT_KEY = {"absences": "absences_this_term", "lates": "lates_this_term", "balance": "balance"}


def _facts_in(prompt: str) -> dict:
    m = re.search(r"\{.*\}", prompt, re.S)
    return json.loads(m.group(0)) if m else {}


def standin_model(prompt: str, text: str) -> str:
    """The scripted stand-in: a fixed template filled with a fact from the prompt."""
    lang = "ar" if is_arabic(text) else "en"
    facts = _facts_in(prompt)
    name = facts.get("first_name") or (facts.get("full_name_ar" if lang == "ar" else "full_name", "") or "").split(" ")[0] \
        or ("طفلكم" if lang == "ar" else "your child")
    for intent, pattern in (AR_INTENTS if lang == "ar" else EN_INTENTS):
        if re.search(pattern, text, re.I) and FACT_KEY[intent] in facts:
            return TEMPLATES[(intent, lang)].format(n=name, v=facts[FACT_KEY[intent]])
    return TEMPLATES[("other", lang)]


def hosted_model(prompt: str, model: str = HOSTED_MODEL, timeout: int = 60) -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        raise RuntimeError("no OPENROUTER_API_KEY")
    body = json.dumps({"model": model, "temperature": 0, "max_tokens": 300,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(OPENROUTER_URL, data=body, method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"].strip()


_WARNED = set()


def draft(prompt: str, text: str, model: str = "auto") -> tuple[str, str]:
    """Returns (reply, model used)."""
    choice = os.environ.get("WAFI_MODEL", model)
    if choice != "standin" and os.environ.get("OPENROUTER_API_KEY"):
        for m in (HOSTED_MODEL, FALLBACK_MODEL):
            try:
                return hosted_model(prompt, m), m
            except Exception as e:                      # 401, 429, timeouts: fall back
                if m not in _WARNED:
                    print(f"(hosted model {m} did not answer: {str(e)[:80]}; trying the next one)")
                    _WARNED.add(m)
    return standin_model(prompt, text), "stand-in"


# ------------------------------------------------------------------ tracing
class Tracer:
    """Records every field Wafi reads, sends, logs and stores, step by step."""

    def __init__(self):
        self.events: list[dict] = []

    def __call__(self, step: str, action: str, where: str, fields: list[str]) -> None:
        self.events.append({"step": step, "action": action, "where": where, "fields": list(fields)})


def _null(*_a, **_k):
    return None


# ------------------------------------------------------------------ the assistant
class Wafi:
    def __init__(self, prompt_builder=build_prompt_v1, router=route_v1, model: str = "auto",
                 tracer=None, records: Records | None = None, disclosure: str | None = None):
        self.records = records or Records()
        self.prompt_builder = prompt_builder
        self.router = router
        self.model = model
        self.trace = tracer or _null
        self.disclosure = disclosure
        self.log: list[dict] = []
        self.cache: dict[str, str] = {}
        self.review_queue: list[dict] = []

    def handle(self, mobile: str, text: str, day: str = str(U.TODAY)) -> dict:
        self.trace("1 intake", "read", "parent channel", ["guardian.mobile", "enquiry.text"])
        guardian = self.records.by_mobile.get(mobile)
        if guardian is None:
            return {"reply": "", "escalated": True, "model": "", "prompt": None}
        self.trace("2 find guardian", "read", "student information system", [f"guardian.{k}" for k in guardian])
        student = self.records.child_named(guardian["guardian_id"], text)
        self.trace("3 find student", "read", "student information system", [f"student.{k}" for k in student])
        facts = self.records.facts(student["student_id"])
        self.trace("4 attendance and fees", "read", "student information system and fee system",
                   ["attendance.status", "attendance.reason", "attendance.note", "fees.balance"])
        built = self.prompt_builder(text, student, guardian, facts)
        self.trace("5 send prompt", "send", "model provider", built["fields"])
        key = hashlib.sha256(built["text"].encode()).hexdigest()
        if key in self.cache:
            reply, used = self.cache[key], "cache"
        else:
            reply, used = draft(built["text"], text, self.model)
        self.trace("6 receive draft", "read", "model provider", ["reply.text"])
        escalated = bool(self.router(text))
        if self.disclosure:
            reply = reply + "\n\n" + self.disclosure
        if escalated:
            self.review_queue.append({"mobile": mobile, "text": text, "draft": reply})
            self.trace("7 staff review", "store", "staff review queue", ["guardian.mobile", "enquiry.text", "reply.text"])
        self.log.append({"date": day, "guardian_mobile": mobile, "enquiry": text, "prompt": built["text"],
                         "reply": reply, "model": used, "escalated": escalated})
        self.trace("8 log", "log", "Wafi enquiry log", ["guardian.mobile", "enquiry.text", "prompt.text", "reply.text"])
        self.cache[key] = reply
        self.trace("9 cache", "store", "Wafi reply cache", ["prompt.hash", "reply.text"])
        return {"reply": reply, "escalated": escalated, "model": used, "prompt": built["text"],
                "student_id": student["student_id"]}


def mobile_of(guardian_id: str, records: Records | None = None) -> str:
    recs = records or Records()
    return recs.guardians[guardian_id]["mobile"]
