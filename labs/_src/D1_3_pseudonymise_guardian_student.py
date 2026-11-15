# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.3 · Pseudonymise, then attack
#
# Day 1 · Session 3 (Pseudonymisation and its limits) · 25 min.
#
# Dana wants to give a contractor the student records "with the names taken out" to tune Wafi. You
# pseudonymise the records with a keyed hash, then play the attacker: Rawafid's own website
# published sports-day results with names, campus, grade, gender and date of birth. You join the two
# on those quasi-identifiers and count how many children you can name, and what you learn about
# them. Then you generalise and measure again.
#
# **Reference state.** `data/students.csv`, `data/guardians.csv`, `data/public_sports_day.csv` and
# the lab key in `data/lab_key.txt`. Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Replace identifiers with keyed pseudonyms (6')
# - [ ] 2 · Join with the sports-day page on quasi-identifiers (6')
# - [ ] 3 · Measure the re-identification rate (4')
# - [ ] 4 · Generalise birth date and grade, measure again (6')
# - [ ] 5 · Record k and the residual risk (3')
# - [ ] ✱ Stretch · Show that an unkeyed hash of a student number is reversed by trying every number
#
# **AI policy.** AI off for the first attempt at the join in task 2: the point is to see how little it takes.

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
import pandas as pd
import rawafid as U

students = U.load("students.csv")
page = U.load("public_sports_day.csv")
page.insert(0, "row", range(len(page)))   # one number per name on the page
KEY = (U.DATA / "lab_key.txt").read_text(encoding="utf-8").strip()   # a lab key: kept apart from the data
QI = ["campus", "grade", "gender", "date_of_birth"]
print(len(students), "students;", len(page), "names on the public sports-day page")
page.head(3)

# %% [markdown]
# ## 1 · Keyed pseudonyms (6')
#
# The Pseudonymisation Guideline: identifiers are replaced by codes, and the extra information
# that links them back (here, the key) is kept separately. A keyed hash (HMAC) gives the same code
# for the same person every time, and nobody without the key can recompute it.
#
# ✏️ **Exercise** · Write `pseudonymise(df, key)`: drop `full_name`, `full_name_ar` and
# `national_id`, and replace `student_id` and `guardian_id` with `code(value, key)`.

# %%
def code(value: str, key: str) -> str:
    return "P" + hmac.new(key.encode(), value.encode(), hashlib.sha256).hexdigest()[:10]

def pseudonymise(df: pd.DataFrame, key: str) -> pd.DataFrame:
    # BEGIN SOLUTION
    out = df.drop(columns=["full_name", "full_name_ar", "national_id"]).copy()
    for col in ("student_id", "guardian_id"):
        out[col] = out[col].map(lambda v: code(v, key))
    return out
    # END SOLUTION

# %%
try:
    pseudo = pseudonymise(students, KEY)
except NotImplementedError:
    pseudo = pd.DataFrame(U.reference("lab13_pseudo"))
U.check(not {"full_name", "national_id"} & set(pseudo.columns), "names and national IDs are gone")
U.check(pseudo["student_id"].nunique() == len(students), "one distinct code per student")
pseudo.head(3)

# %% [markdown]
# ## 2 · The linkage attack (6')
#
# ✏️ **Exercise** · Write `link(pseudo, page)`: join the page to the pseudonymised records on the
# four quasi-identifiers in `QI` and return the joined rows, with the page's `name` beside the
# record's `health_notes`.

# %%
def link(pseudo: pd.DataFrame, page: pd.DataFrame, on: list[str] = QI) -> pd.DataFrame:
    # BEGIN SOLUTION
    return page[["row", "name"] + on].merge(pseudo, on=on, how="inner")
    # END SOLUTION

# %%
try:
    joined = link(pseudo, page)
except NotImplementedError:
    joined = page[["row", "name"] + QI].merge(pseudo, on=QI, how="inner")
print(len(joined), "joined rows")
joined[joined["health_notes"] != ""][["name", "campus", "grade", "health_notes"]].head(5)

# %% [markdown]
# ## 3 · The re-identification rate (4')
#
# A page row is **re-identified** when it matches exactly one record (two children can share a
# name, so count rows, not names). ✏️ **Exercise** · Write
# `reid_rate(joined, page)` returning the number of uniquely matched names and that number divided by
# the number of names on the page.

# %%
def reid_rate(joined: pd.DataFrame, page: pd.DataFrame) -> tuple[int, float]:
    # BEGIN SOLUTION
    counts = joined.groupby("row").size()
    unique = int((counts == 1).sum())
    return unique, round(unique / len(page), 3)
    # END SOLUTION

# %%
try:
    unique, rate = reid_rate(joined, page)
except NotImplementedError:
    r = U.reference("lab13_matches")
    unique, rate = r["unique"], r["rate"]
named = joined.groupby("row").filter(lambda g: len(g) == 1)
print(f"{unique} of {len(page)} names re-identified ({rate:.0%}); "
      f"{(named['health_notes'] != '').sum()} of them with a health note now known")
U.check(rate > 0.9, "more than nine in ten names come back from records without names")

# %% [markdown]
# ## 4 · Generalise, then attack again (6')
#
# The guideline's techniques include **generalisation** (age bands instead of exact ages) and
# **aggregation** (birth year instead of birth date). ✏️ **Exercise** · Write `generalise(df)`:
# replace `date_of_birth` by `birth_year`, `grade` by `grade_band` (`1-3`, `4-6`, `7-9`, `10-12`) and
# drop `section`. The same function must work on the page, so the attacker can generalise too.

# %%
def grade_band(g: str) -> str:
    g = int(g)
    return "1-3" if g <= 3 else "4-6" if g <= 6 else "7-9" if g <= 9 else "10-12"

def generalise(df: pd.DataFrame) -> pd.DataFrame:
    # BEGIN SOLUTION
    out = df.copy()
    out["birth_year"] = out["date_of_birth"].str[:4]
    out["grade_band"] = out["grade"].map(grade_band)
    return out.drop(columns=[c for c in ("date_of_birth", "grade", "section") if c in out.columns])
    # END SOLUTION

# %%
QI2 = ["campus", "grade_band", "gender", "birth_year"]
try:
    general = generalise(pseudo)
    page2 = generalise(page)
except NotImplementedError:
    general = pd.DataFrame(U.reference("lab13_general"))
    page2 = page.assign(birth_year=page["date_of_birth"].str[:4], grade_band=page["grade"].map(grade_band))
joined2 = page2[["row", "name"] + QI2].merge(general, on=QI2, how="inner")
unique2 = int((joined2.groupby("row").size() == 1).sum())
rate2 = round(unique2 / len(page), 3)
k = int(general.groupby(QI2).size().min())
print(f"after generalisation: {unique2} of {len(page)} names re-identified ({rate2:.0%}); smallest group k = {k}")
U.check(rate2 < rate / 3, "generalising cuts the re-identification rate by more than two thirds")

# %% [markdown]
# **Look at** `k`. Some groups still hold one child: a small campus, an older grade. Generalising
# lowers the risk on average and leaves the rare child exposed.

# %%
groups = general.groupby(QI2).size()
print((groups < 5).sum(), "of", len(groups), "groups have fewer than five children")

# %% [markdown]
# ## 5 · Record k and the residual risk (3')
#
# ✏️ **Exercise** · Fill the record your capstone will reuse: the method, the attack, both rates, k,
# and one sentence on what is still needed (for example, suppressing groups under five before any
# release, and that the result is still personal data because Rawafid holds the key).

# %%
def risk_record() -> dict:
    # BEGIN SOLUTION
    return {"method": "HMAC-SHA256 pseudonyms with a separately held key; names and national IDs dropped",
            "attack": "join with the public sports-day page on campus, grade, gender and date of birth",
            "rate_before": rate, "rate_after_generalisation": rate2, "k": k,
            "residual": "Groups under five remain; suppress them before any release. The data stays personal data "
                        "because the key can link it back."}
    # END SOLUTION

# %%
try:
    record = risk_record()
except NotImplementedError:
    record = {"rate_before": rate, "rate_after_generalisation": rate2, "k": k, "residual": "to write"}
print(record)
U.check(record["k"] == k and record["rate_before"] == rate, "the record carries the measured numbers")

# %% [markdown]
# ## ✱ Stretch · An unkeyed hash is not a pseudonym
#
# Hash each `student_id` with plain SHA-256, no key. Then, as the attacker, hash every possible
# number from `S10001` to `S11200` and look each hash up. How many do you reverse, and how long did
# it take?

# %% [markdown]
# ## Check yourself
#
# 1. Is the pseudonymised file still personal data under the PDPL guidelines? Why?
# 2. Which column did the attack need most?
# 3. Why must the key not travel with the file?
#
# <details><summary>Answers</summary>
#
# 1. Yes: pseudonymised data can be linked back, so it stays personal data; only irreversibly
#    anonymised data leaves the law's scope, and that must be tested.
# 2. The exact date of birth: with campus, grade and gender it is almost unique per child.
# 3. With the key anyone can recompute every code from a student number and undo the pseudonyms.
# </details>
#
# **Carry forward.** `generalise` and the measured rates go into the capstone's minimisation code.
