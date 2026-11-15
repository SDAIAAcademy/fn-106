# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.4 · Retention and a seeded breach
#
# Day 1 · Session 4 (Rights, retention and breaches) · 25 min.
#
# Wafi's six stores keep data with no end date. You write a retention rule for each, count what the
# enquiry log holds past its rule, then handle an incident Dana reported this week: an export of the
# log on a shared drive whose link reached a public forum. You size the breach from the log itself
# and draft the notice to SDAIA under the Personal Data Breach Incidents Procedural Guide.
#
# **Reference state.** `data/stores.json`, `data/wafi_log.jsonl`, `data/incident_note.md`. The labs'
# "today" is Thursday 2026-11-12. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Write a retention rule per store (6')
# - [ ] 2 · Count log rows past the rule (4')
# - [ ] 3 · Read the incident and size the breach (5')
# - [ ] 4 · Draft the notice to SDAIA with its five contents (6')
# - [ ] 5 · Decide the notice to guardians (4')
# - [ ] ✱ Stretch · Add the breach to the documentation record with its corrective actions

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
from datetime import date, timedelta
import pandas as pd
import rawafid as U

stores = U.json("stores.json")
log = pd.DataFrame(U.jsonl("wafi_log.jsonl"))
log["date"] = pd.to_datetime(log["date"]).dt.date
print(len(log), "log rows from", log["date"].min(), "to", log["date"].max())
U.table(stores)

# %% [markdown]
# ## 1 · A retention rule per store (6')
#
# The law: destroy personal data without undue delay once the purpose no longer needs it, unless a
# legal basis requires keeping it for a set period (Article 18). A rule names a **period**, the
# **event that starts it**, and the **method** of destruction (the Destruction Guideline lists
# secure erasure and overwriting, among others).
#
# ✏️ **Exercise** · Return one rule per store. Use a number of days where Rawafid decides the period
# itself; where another law or the provider's contract decides it, say who confirms the period.
# Rawafid's data protection officer has agreed that complaints about a reply arrive within 60 days.

# %%
def retention_rules() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "student information system": {"days": None, "starts": "the student leaves Rawafid",
                                       "period": "the period the applicable education records rules require, confirmed by the DPO",
                                       "method": "secure erasure, then confirm with the system's audit report"},
        "fee system": {"days": None, "starts": "the end of the financial year of the last invoice",
                       "period": "the period the applicable financial records rules require, confirmed by Osama Al-Qurashi",
                       "method": "secure erasure; card digits removed at once when no longer needed"},
        "Wafi enquiry log": {"days": 90, "starts": "the date of the enquiry",
                             "period": "60 days for complaints plus 30 days to investigate", "method": "scheduled deletion of rows and backups"},
        "Wafi reply cache": {"days": 7, "starts": "the date the reply was cached", "period": "a week of repeated questions",
                             "method": "automatic expiry"},
        "staff review queue": {"days": 90, "starts": "the case is closed", "period": "the same as the log",
                               "method": "scheduled deletion"},
        "model provider": {"days": 0, "starts": "the request is answered", "period": "no retention, in the contract with the provider",
                           "method": "contract clause and the provider's confirmation"},
    }
    # END SOLUTION

# %%
try:
    rules = retention_rules()
except NotImplementedError:
    rules = U.reference("lab14_rules")
U.check(set(rules) == {s["store"] for s in stores}, "one rule per store")
U.check(rules["Wafi enquiry log"]["days"] is not None and rules["Wafi enquiry log"]["days"] <= 90,
        "the log has a period of at most 90 days")
U.table([{"store": k, **v} for k, v in rules.items()])

# %% [markdown]
# ## 2 · What the log holds past its rule (4')
#
# ✏️ **Exercise** · Write `past_rule(log, days)`: the rows older than `days` before `U.TODAY`.

# %%
def past_rule(log: pd.DataFrame, days: int) -> pd.DataFrame:
    # BEGIN SOLUTION
    return log[log["date"] < U.TODAY - timedelta(days=days)]
    # END SOLUTION

# %%
days = rules["Wafi enquiry log"]["days"]
try:
    old = past_rule(log, days)
except NotImplementedError:
    old = log[log["date"] < U.TODAY - timedelta(days=days)]
print(f"{len(old)} of {len(log)} rows ({len(old) / len(log):.0%}) are past a {days}-day rule; oldest {old['date'].min()}")

# %% [markdown]
# ## 3 · The incident, sized from the log (5')

# %%
print((U.DATA / "incident_note.md").read_text(encoding="utf-8"))

# %% [markdown]
# ✏️ **Exercise** · Write `size_breach(log)` for the exported rows (2026-05-01 to 2026-10-20
# inclusive). Return the number of rows, of distinct guardians (mobiles), of distinct students (the
# `student_id` inside each prompt), of rows whose prompt holds a non-empty health note, and of
# distinct student national IDs exposed.

# %%
def student_of(prompt: str) -> dict:
    return json.loads(re.search(r"\{.*\}", prompt, re.S).group(0))

def size_breach(log: pd.DataFrame) -> dict:
    # BEGIN SOLUTION
    rows = log[(log["date"] >= date(2026, 5, 1)) & (log["date"] <= date(2026, 10, 20))]
    recs = rows["prompt"].map(student_of)
    return {"rows": int(len(rows)), "guardians": int(rows["guardian_mobile"].nunique()),
            "students": int(recs.map(lambda r: r["student_id"]).nunique()),
            "rows_with_health_notes": int(recs.map(lambda r: r["health_notes"] != "").sum()),
            "student_national_ids": int(recs.map(lambda r: r["national_id"]).nunique())}
    # END SOLUTION

# %%
try:
    size = size_breach(log)
except NotImplementedError:
    size = U.reference("lab14_breach")
print(size)
U.check(size["students"] > 100 and size["rows_with_health_notes"] > 0, "the export exposes minors' IDs and health notes")

# %% [markdown]
# ## 4 · The notice to SDAIA (6')
#
# The guide: notify SDAIA **within 72 hours of becoming aware** when the breach is expected to harm
# the data or the data subjects, through the national data governance platform, with five
# contents: (1) a description with the date, how it happened and when Rawafid became aware;
# (2) the categories of data subjects, their numbers and the kinds of data; (3) the risks, the
# remedial actions taken and the measures to stop it happening again; (4) whether the data subjects
# have been or will be notified; (5) the contact details of the controller or its data protection
# officer.
#
# ✏️ **Exercise** · Return the notice as a dict with the keys below and the deadline date: three
# days after the day of awareness.

# %%
NOTICE_KEYS = ["description", "subjects_and_data", "risks_and_actions", "data_subjects_notified", "contact", "deadline"]

def notice_to_sdaia(size: dict) -> dict:
    # BEGIN SOLUTION
    aware = date(2026, 11, 9)
    return {
        "description": "An export of Wafi's enquiry log (rows dated 2026-05-01 to 2026-10-20) was placed on 2026-10-21 in a "
                       "shared drive folder open to anyone with the link; the link was found in a public forum on "
                       "2026-11-09, the day Rawafid became aware, with views from outside accounts.",
        "subjects_and_data": f"{size['students']} students (minors) and {size['guardians']} guardians: names, national IDs, "
                             f"dates of birth, mobile numbers, enquiry texts and {size['rows_with_health_notes']} records with health notes.",
        "risks_and_actions": "Risks: identity misuse, exposure of children's health conditions, targeted fraud against guardians. "
                             "Done: link removed and folder locked on 2026-11-09. Next: prompts minimised, log kept 90 days, "
                             "exports to contractors stopped.",
        "data_subjects_notified": "Guardians will be notified without undue delay (task 5).",
        "contact": "Nasser Al-Mansour, data protection officer, Rawafid Schools Group",
        "deadline": str(aware + timedelta(days=3)),
    }
    # END SOLUTION

# %%
try:
    notice = notice_to_sdaia(size)
except NotImplementedError:
    notice = U.reference("lab14_notice")
U.check(all(notice.get(k) for k in NOTICE_KEYS), "the notice has all five contents and the deadline")
U.check(notice["deadline"] == "2026-11-12", "72 hours from awareness on 2026-11-09 end on 2026-11-12: today")
print(json.dumps(notice, indent=1, ensure_ascii=False))

# %% [markdown]
# ## 5 · The notice to guardians (4')
#
# The guide asks for a notice to the data subjects without undue delay when the breach damages their
# data or conflicts with their rights or interests, in clear and simple words, with four contents:
# what happened, the risks and the measures taken, the controller's contact and its DPO, and advice
# to protect themselves. ✏️ **Exercise** · Decide, and give the reason and the four contents in one
# short line each.

# %%
def notice_to_guardians() -> dict:
    # BEGIN SOLUTION
    return {"notify": True,
            "why": "National IDs and children's health notes were open to the public: harm to the children and guardians is expected.",
            "contents": ["What happened and which of your data was in the file",
                         "The risks, and what Rawafid has done and will do",
                         "How to reach Rawafid and its data protection officer",
                         "Advice: watch for messages that quote your child's details, never share verification codes"]}
    # END SOLUTION

# %%
try:
    g_notice = notice_to_guardians()
except NotImplementedError:
    g_notice = {"notify": True, "why": "see the reference", "contents": ["", "", "", ""]}
U.check(g_notice["notify"] is True and len(g_notice["contents"]) == 4, "guardians are told, with four contents")

# %% [markdown]
# ## ✱ Stretch · The documentation record
#
# The guide's third stage: keep copies of what was sent to SDAIA, the corrective actions and the
# lessons learned. Write that record as a dict, with the retention rule it falls under.

# %% [markdown]
# ## Check yourself
#
# 1. From which moment do the 72 hours run?
# 2. Why would a 90-day log rule have made this breach smaller?
# 3. A guardian asks for a copy of the data Rawafid holds on their child. Within how long, at most?
#
# <details><summary>Answers</summary>
#
# 1. From the moment Rawafid became aware of the incident, not from the day it happened.
# 2. The export reached back to May: with a 90-day rule most of those rows would already have been destroyed.
# 3. Thirty days, extendable by thirty more with notice and reasons (Implementing Regulation, Article 3).
# </details>
#
# **Carry forward.** The retention table and the breach checklist are two parts of the capstone pack.
