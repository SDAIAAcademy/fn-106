# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.3 · A partner's data request
#
# Day 2 · Session 3 (Sharing with another entity) · 25 min.
#
# A university research centre asks Rawafid for attendance data to study commute distance and
# absence. You read the request against the eight principles of the Data Sharing Policy (adopted
# by Rawafid's own policy) and the PDPL's rules on disclosure and research, cut the request to what
# the purpose needs, draft the conditions, build the extract, and check it for small groups.
#
# **Reference state.** `data/partner_request.json`, `data/students.csv`, `data/guardians.csv`,
# `data/attendance.csv`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Read the request against the eight principles (6')
# - [ ] 2 · Mark each requested field needed or not (5')
# - [ ] 3 · Draft the conditions of sharing (6')
# - [ ] 4 · Build the minimised extract (5')
# - [ ] 5 · Check the extract for small groups (3')
# - [ ] ✱ Stretch · Write the destruction confirmation the partner signs

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

import hashlib
import hmac
import json
import pandas as pd
import rawafid as U

request = U.json("partner_request.json")
print(json.dumps(request, indent=1, ensure_ascii=False))

# %% [markdown]
# ## 1 · The eight principles (6')
#
# The Data Sharing Policy's principles: (1) a data-sharing culture, (2) a single source of truth,
# (3) a **legitimate purpose** with a legal basis, data used only for the stated purpose,
# (4) **authorised access**, (5) **transparency** about the data, its classification, storage,
# protection and destruction, (6) **collective accountability** under an agreement, (7) **data
# security**, (8) **ethical data use**. The PDPL adds: disclosure only in listed cases
# (Article 15), and research without consent only when the data does not identify the person or
# the identity evidence is destroyed first (Article 27).
#
# ✏️ **Exercise** · For each principle, return `"met"`, `"not met"` or `"met with conditions"` and a
# reason taken from the request.

# %%
PRINCIPLES = ["sharing culture", "single source of truth", "legitimate purpose", "authorised access",
              "transparency", "collective accountability", "data security", "ethical data use"]

def assess(request: dict) -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "sharing culture": {"status": "met", "reason": "Research on absence serves the public interest; sharing is the default when the conditions hold."},
        "single source of truth": {"status": "met", "reason": "Rawafid is the source of its own attendance records."},
        "legitimate purpose": {"status": "met with conditions", "reason": "The study is legitimate, but names, IDs, employer and health notes go beyond it; onward sharing would change the purpose."},
        "authorised access": {"status": "not met", "reason": "No named researchers; 'research partners when needed' is open-ended."},
        "transparency": {"status": "met with conditions", "reason": "Classification, storage, protection and destruction must be stated; today storage is abroad and retention indefinite."},
        "collective accountability": {"status": "not met", "reason": "No agreement yet; roles and responsibilities must be signed."},
        "data security": {"status": "not met", "reason": "A password-protected spreadsheet by email and a workspace outside the Kingdom."},
        "ethical data use": {"status": "met with conditions", "reason": "Children's health notes have no place in a commute study."},
    }
    # END SOLUTION

# %%
try:
    assessment = assess(request)
except NotImplementedError:
    assessment = U.reference("lab23_assessment")
U.check(set(assessment) == set(PRINCIPLES), "every principle assessed")
U.check(assessment["data security"]["status"] == "not met", "email and a workspace abroad fail data security")
U.table([{"principle": p, **assessment[p]} for p in PRINCIPLES])

# %% [markdown]
# ## 2 · Field by field (5')
#
# The purpose: commute distance and absence in primary and middle school. ✏️ **Exercise** · Return the
# requested fields the purpose needs. A field that is needed in a coarser form counts as needed
# (date of birth as a birth year; daily records as monthly counts).

# %%
def needed_fields(request: dict) -> list[str]:
    # BEGIN SOLUTION
    keep = {"date_of_birth", "gender", "grade", "campus", "district", "daily_attendance_records"}
    return [f for f in request["requested_fields"] if f in keep]
    # END SOLUTION

# %%
try:
    needed = needed_fields(request)
except NotImplementedError:
    needed = U.reference("lab23_needed")
refused = [f for f in request["requested_fields"] if f not in needed]
print("share, in a coarser form:", needed)
print("refuse:", refused)
U.check({"full_name", "national_id", "health_notes", "guardian_employer"} <= set(refused), "no names, IDs, employer or health notes")

# %% [markdown]
# ## 3 · The conditions (6')
#
# ✏️ **Exercise** · Write the conditions Rawafid sets before it shares, one per line. Cover: the
# purpose and no other use, the fields and their form, the classification label (Restricted) on the
# data, storage in the Kingdom or a lawful transfer, named authorised users, no onward sharing,
# destruction at the end of the study with a confirmation, and a signed agreement.

# %%
def conditions() -> list[str]:
    # BEGIN SOLUTION
    return [
        "Used only for the stated study of commute distance and absence; any other use needs a new request.",
        "Pseudonymised extract: birth year, gender, grade band, campus, district, monthly absence counts for grades 1 to 9.",
        "Labelled Restricted, with the classification in the metadata, and protected as Restricted data.",
        "Stored in the Kingdom; no transfer abroad unless the PDPL transfer conditions are met and Rawafid agrees in writing.",
        "Accessed only by the named researchers listed in the agreement.",
        "No onward sharing with any party.",
        "Destroyed at the end of the study, within a set date, with a signed destruction confirmation.",
        "Sent through a secure channel agreed with Rawafid, not by email.",
        "A data-sharing agreement signed before any data moves, naming each side's responsibilities.",
    ]
    # END SOLUTION

# %%
try:
    conds = conditions()
except NotImplementedError:
    conds = U.reference("lab23_conditions")
for c in conds:
    print("-", c)
text = " ".join(conds).lower()
U.check(all(w in text for w in ("study", "restricted", "kingdom", "onward", "destroy", "agreement")),
        "the conditions cover use, label, location, onward sharing, destruction and the agreement")

# %% [markdown]
# ## 4 · The extract (5')
#
# ✏️ **Exercise** · Write `build_extract(students, guardians, attendance, key)`: grades 1 to 9 only;
# a project pseudonym per student (HMAC with a key used for this project only); `birth_year`,
# `gender`, `grade_band`, `campus`, the guardian's `district`; and absence counts per month
# (`2026-08` to `2026-11`). No notes, no names, no IDs.

# %%
students = U.load("students.csv")
guardians = U.load("guardians.csv")
attendance = U.load("attendance.csv")
PROJECT_KEY = "al-mizan-study-2026-lab-key"
MONTHS = ["2026-08", "2026-09", "2026-10", "2026-11"]

def band(g):
    g = int(g)
    return "1-3" if g <= 3 else "4-6" if g <= 6 else "7-9"

def build_extract(students, guardians, attendance, key) -> pd.DataFrame:
    # BEGIN SOLUTION
    s = students[students["grade"].astype(int) <= 9].merge(guardians[["guardian_id", "district"]], on="guardian_id")
    absn = attendance[attendance["status"] == "absent"].assign(month=lambda d: d["date"].str[:7])
    counts = absn.groupby(["student_id", "month"]).size().unstack(fill_value=0).reindex(columns=MONTHS, fill_value=0)
    out = pd.DataFrame({
        "pid": s["student_id"].map(lambda v: hmac.new(key.encode(), v.encode(), hashlib.sha256).hexdigest()[:10]),
        "birth_year": s["date_of_birth"].str[:4], "gender": s["gender"], "grade_band": s["grade"].map(band),
        "campus": s["campus"], "district": s["district"], "student_id": s["student_id"]})
    out = out.merge(counts, left_on="student_id", right_index=True, how="left").fillna(0)
    for m in MONTHS:
        out[m] = out[m].astype(int)
    return out.drop(columns=["student_id"]).reset_index(drop=True)
    # END SOLUTION

# %%
try:
    extract = build_extract(students, guardians, attendance, PROJECT_KEY)
except NotImplementedError:
    extract = pd.DataFrame(U.reference("lab23_extract"))
print(len(extract), "rows;", list(extract.columns))
U.check(not {"full_name", "national_id", "note", "health_notes", "student_id"} & set(extract.columns), "no names, IDs or notes")
extract.head()

# %% [markdown]
# ## 5 · Small groups (3')
#
# Campus, district, grade band and gender together can still single a child out. Count the groups
# with fewer than five pupils.

# %%
QI = ["campus", "district", "grade_band", "gender"]
groups = extract.groupby(QI).size()
print(f"{(groups < 5).sum()} of {len(groups)} groups have fewer than five pupils; smallest k = {groups.min()}")
coarse = extract.groupby(["campus", "grade_band", "gender"]).size()
print(f"without the district: {(coarse < 5).sum()} of {len(coarse)} groups under five; k = {coarse.min()}")

# %% [markdown]
# **Look at** the trade-off: the district is the study's whole point (commute distance), yet it
# makes the small groups. One answer is to share the district, and suppress or merge groups under
# five before the file leaves; another is to compute commute bands inside Rawafid and share those.
# Write your choice into the conditions.

# %% [markdown]
# ## ✱ Stretch · The destruction confirmation
#
# Write the short statement the centre's principal investigator signs at the end of the study:
# what was destroyed, how (backups included), when, and that no copy was passed on.

# %% [markdown]
# ## Check yourself
#
# 1. Which principle does "kept indefinitely for future studies" break?
# 2. Under which PDPL article may Rawafid share for research without the guardians' consent, and on what condition?
# 3. Why a project-specific key for the pseudonyms?
#
# <details><summary>Answers</summary>
#
# 1. Transparency about destruction, and the legitimate purpose: data is used only for the stated purpose.
# 2. Article 27: when the data does not specifically identify the child, or identity evidence is destroyed before disclosure and the data is not sensitive.
# 3. So the centre's codes cannot be joined with any other file Rawafid shares, and the key never leaves Rawafid.
# </details>
#
# **Carry forward.** The assessment and conditions are the "sharing" part of the capstone's classification and sharing criterion.
