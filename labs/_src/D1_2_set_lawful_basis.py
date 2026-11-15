# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.2 · Lawful basis and minimum fields
#
# Day 1 · Session 2 (Lawful basis and minimisation) · 25 min.
#
# Every flow of Wafi needs a legal basis and a purpose, and every field it sends must be needed
# for that purpose. You set the basis of five flows, test the 21 fields of Dana's prompt against
# the purpose, write a prompt builder that sends the minimum, and prove on ten enquiries that the
# replies are as good and the prompts carry no identifier.
#
# **Reference state.** `wafi.py` and `data/`. The 21 sent fields of Lab 1.1 are listed below, so
# you do not need that lab's result.
#
# **Tasks**
# - [ ] 1 · Set a basis and purpose for each of the five flows (6')
# - [ ] 2 · Test each prompt field against the purpose (6')
# - [ ] 3 · Write the minimised prompt builder (7')
# - [ ] 4 · Check ten prompts and print the before-and-after list (6')
# - [ ] ✱ Stretch · Draft the consent wording for the one optional flow

# %%
import os, sys, subprocess
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    REPO_URL = "https://github.com/SDAIAAcademy/fn-106.git"
    if not Path("/content/fn-106").exists():
        subprocess.run(["git", "clone", "-q", REPO_URL, "/content/fn-106"], check=True)
    os.chdir("/content/fn-106/labs")
else:
    while not Path("rawafid.py").exists() and Path.cwd() != Path.cwd().parent:
        os.chdir("..")  # solutions/ notebooks run from labs/
sys.path.insert(0, os.getcwd())

import json
import re
import pandas as pd
import rawafid as U
import wafi

records = wafi.Records()
s0, g0 = records.students[0], records.guardians[records.students[0]["guardian_id"]]
before = wafi.build_prompt_v1("x", s0, g0, records.facts(s0["student_id"]))["fields"]
print(len(before), "fields in Dana's prompt:", ", ".join(before))

# %% [markdown]
# ## 1 · A basis and a purpose for each flow (6')
#
# The guardian signed an enrolment contract with Rawafid. The student is a minor: the guardian acts
# for them (Implementing Regulation, Article 13). The bases the law offers, in short:
#
# | Basis | When (Personal Data Protection Law) |
# |---|---|
# | `consent` | The data subject or guardian agreed (Article 5); it can be withdrawn at any time |
# | `contract` | Processing in implementation of an agreement the data subject is a party to (Article 6) |
# | `legal obligation` | Processing required by another law (Article 6) |
# | `legitimate interest` | The controller's legitimate interest, without prejudice to the data subject, **and no sensitive data** (Article 6) |
#
# ✏️ **Exercise** · Return a basis and a one-line purpose for each flow.

# %%
FLOWS = {
    "F1 answer": "Wafi reads the child's attendance and fee records to answer the guardian's question",
    "F2 draft": "Wafi sends a prompt to a hosted model that drafts the reply",
    "F3 log": "Wafi keeps a log of enquiries and replies to check quality and investigate complaints",
    "F4 cache": "Wafi caches replies to identical prompts to save model calls",
    "F5 offers": "Wafi adds summer-camp offers to its replies",
}

def bases() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "F1 answer": {"basis": "contract", "purpose": "Answer the guardian's own question about their child under the enrolment contract"},
        "F2 draft": {"basis": "contract", "purpose": "Draft that answer; the model provider acts as a processor for F1"},
        "F3 log": {"basis": "legitimate interest", "purpose": "Check reply quality and investigate complaints, without sensitive data"},
        "F4 cache": {"basis": "legitimate interest", "purpose": "Avoid repeated model calls for identical prompts"},
        "F5 offers": {"basis": "consent", "purpose": "Send offers only to guardians who agreed, with a way to stop"},
    }
    # END SOLUTION

# %%
try:
    basis = bases()
except NotImplementedError:
    basis = U.reference("lab12_basis")
U.table([{"flow": f, **basis[f]} for f in FLOWS])
U.check(set(basis) == set(FLOWS), "every flow has a basis")
U.check(basis["F5 offers"]["basis"] == "consent", "advertising needs consent (Articles 25 and 26)")
U.check(basis["F1 answer"]["basis"] != "consent", "answering the guardian's own question rests on the contract, not consent")

# %% [markdown]
# ## 2 · Test each field against the purpose (6')
#
# The purpose of F1 and F2 is to answer the guardian's question about their child's attendance or
# fees. The Minimum Personal Data Guideline asks of each element: is it **actually needed** for the
# purpose? ✏️ **Exercise** · Return the subset of `before` that the purpose needs. The reply greets
# the child by first name.

# %%
def needed_fields(fields: list[str]) -> list[str]:
    # BEGIN SOLUTION
    keep = {"student.full_name", "derived.absences_this_term", "derived.lates_this_term", "derived.balance", "enquiry.text"}
    return [f for f in fields if f in keep]
    # END SOLUTION

# %%
try:
    needed = needed_fields(before)
except NotImplementedError:
    needed = U.reference("lab12_needed")
dropped = [f for f in before if f not in needed]
print("keep:", needed)
print("drop:", dropped)
U.check("student.health_notes" in dropped and "student.national_id" in dropped and "guardian.national_id" in dropped,
        "health notes and both national IDs go")
U.check(len(needed) <= 6, "at most six of 21 fields are needed")

# %% [markdown]
# ## 3 · The minimised prompt builder (7')
#
# ✏️ **Exercise** · Write `build_prompt_min(text, student, guardian, facts)` with the same return shape
# as `wafi.build_prompt_v1`: a dict with `text` and `fields`. Put only the facts in a JSON object:
# `first_name` (Arabic script when the message is in Arabic), `absences_this_term`,
# `lates_this_term`, `balance`. List the fields as `student.first_name`, the three `derived.` names and
# `enquiry.text`.

# %%
def build_prompt_min(text: str, student: dict, guardian: dict, facts: dict) -> dict:
    # BEGIN SOLUTION
    name = (student["full_name_ar"] if wafi.is_arabic(text) else student["full_name"]).split()[0]
    data = {"first_name": name, **facts}
    prompt = ("You are Wafi, the parent-enquiry assistant of Rawafid Schools. Answer the guardian in the language "
              f"of the message, using only these facts.\nFacts: {json.dumps(data, ensure_ascii=False)}\n"
              f"Guardian message: {text}")
    return {"text": prompt, "fields": ["student.first_name"] + [f"derived.{k}" for k in facts] + ["enquiry.text"]}
    # END SOLUTION

# %%
try:
    build_prompt_min("test", s0, g0, records.facts(s0["student_id"]))
    builder = build_prompt_min
except NotImplementedError:
    print("(safety net: using a reference builder)")
    def builder(text, student, guardian, facts):
        name = (student["full_name_ar"] if wafi.is_arabic(text) else student["full_name"]).split()[0]
        data = {"first_name": name, **facts}
        return {"text": f"Answer in the message's language from these facts only.\nFacts: {json.dumps(data, ensure_ascii=False)}\n"
                        f"Guardian message: {text}",
                "fields": ["student.first_name"] + [f"derived.{k}" for k in facts] + ["enquiry.text"]}
after = builder("test", s0, g0, records.facts(s0["student_id"]))["fields"]
print(len(before), "->", len(after), "fields")

# %% [markdown]
# ## 4 · Ten prompts, before and after (6')
#
# Run ten logged enquiries through both builders. The answers must stay the same, and no prompt may
# carry a national ID, a mobile number or a health note.

# %%
log = U.jsonl("wafi_log.jsonl")[-10:]
old = wafi.Wafi(records=records, model="standin")
new = wafi.Wafi(records=records, model="standin", prompt_builder=builder)
ID = re.compile(r"\b[12]\d{9}\b")
MOBILE = re.compile(r"\b05\d{8}\b")
HEALTH = [h.split(",")[0] for h in ("asthma", "allergy", "diabetes", "epilepsy", "hearing aid", "ADHD", "migraine")]
same, leaks = 0, 0
for row in log:
    a = old.handle(row["guardian_mobile"], row["enquiry"])
    b = new.handle(row["guardian_mobile"], row["enquiry"])
    same += a["reply"] == b["reply"]
    p = b["prompt"]
    leaks += bool(ID.search(p) or MOBILE.search(p) or any(h in p for h in HEALTH))
print(f"{same} of {len(log)} replies unchanged; {leaks} minimised prompts with an identifier or health note")
U.check(same == len(log), "the minimised prompt answers exactly as well")
U.check(leaks == 0, "no identifier and no health note in any minimised prompt")
pd.DataFrame({"field": before, "sent after minimisation": [f in needed for f in before]})

# %% [markdown]
# **Look at** the two prompt lengths: `len(a["prompt"])` against `len(b["prompt"])`. Fewer fields
# is also fewer tokens, which is cheaper and faster.

# %%
print(len(a["prompt"]), "characters before,", len(b["prompt"]), "after")

# %% [markdown]
# ## ✱ Stretch · Consent for F5
#
# Write the three sentences a guardian sees before agreeing to offers: what is sent, how to stop,
# and that saying no changes nothing about the answers Wafi gives (Article 7).

# %% [markdown]
# ## Check yourself
#
# 1. Why can F3, the log, not rest on legitimate interest while it keeps health notes?
# 2. The guardian consented to nothing about Wafi. Why may F1 still run?
# 3. Which field did you keep that is still personal data?
#
# <details><summary>Answers</summary>
#
# 1. Legitimate interest excludes sensitive data, and health notes are sensitive.
# 2. It implements the enrolment contract the guardian is a party to.
# 3. The child's first name, and the counts themselves: they are about an identifiable child.
# </details>
#
# **Carry forward.** `build_prompt_min` is the builder of Day 3's labs (`wafi.py` copies it as
# `build_prompt_min`).
