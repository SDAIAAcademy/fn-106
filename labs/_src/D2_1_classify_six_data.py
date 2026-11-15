# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.1 · Classify six data sets
#
# Day 2 · Session 1 (Data classification levels) · 25 min.
#
# Rawafid's data policy adopts the NDMO Data Classification Policy. You classify the six data sets
# Wafi touches or Rawafid publishes: assess the impact of their disclosure by category and level,
# map the impact to a classification level and sub-level, catch an aggregate table that still
# reveals children, and write the classification register with a reason for each set.
#
# **Reference state.** `data/datasets.json` (the inventory) and the six files it names. Nothing
# from Day 1 is needed.
#
# **Tasks**
# - [ ] 1 · Read the inventory and the impact categories (4')
# - [ ] 2 · Assess impact category and level per set (8')
# - [ ] 3 · Map impact to level and sub-level (5')
# - [ ] 4 · Find the small cells in the aggregate table (5')
# - [ ] 5 · Record reasons in the register (3')
# - [ ] ✱ Stretch · Suppress the small cells and classify the aggregate table again
#
# **AI policy.** AI off for your first classification of each set (task 2). Afterwards you may
# compare with an assistant and must say where you disagree and why.

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

from datetime import timedelta
import pandas as pd
import rawafid as U

inventory = U.json("datasets.json")
U.table(inventory, ["name", "description", "records", "individuals", "owner"])

# %% [markdown]
# ## 1 · The inventory and the impact categories (4')
#
# The policy assesses the impact of **unauthorised access or disclosure** in four main categories:
# national interest, entity activities, individuals (health and safety, privacy) and environment.
# Each impact has a level: **High**, **Medium**, **Low** or **None**. Read the fields of each set.

# %%
for d in inventory:
    print(f"{d['name']:<20} {', '.join(d['fields'])}")

# %% [markdown]
# ## 2 · Impact per set (8')
#
# ✏️ **Exercise** · Return, for each set, the main impact category, the sub-category and the impact
# level. The policy's own guidance for individuals' privacy: disclosure of an individual's personal
# information is a **Low** impact; a VIP's personal information affecting the national interest is
# Medium or High. Published information has no impact.

# %%
def impacts() -> dict[str, dict]:
    # BEGIN SOLUTION
    priv = {"category": "Individuals", "sub_category": "Privacy", "level": "Low"}
    return {
        "fee_schedule": {"category": "None", "sub_category": "already published", "level": "None"},
        "guardians": priv,
        "students": priv,
        "attendance": priv,
        "fees": {"category": "Individuals", "sub_category": "Privacy (detailed statements of individual transactions)", "level": "Low"},
        "attendance_summary": {"category": "Individuals", "sub_category": "Privacy (cells small enough to point at a child)", "level": "Low"},
    }
    # END SOLUTION

# %%
try:
    impact = impacts()
except NotImplementedError:
    impact = U.reference("lab21_impact")
U.check(set(impact) == {d["name"] for d in inventory}, "an impact for every set")
U.check(impact["fee_schedule"]["level"] == "None" and impact["students"]["level"] == "Low", "published: none; personal: low")

# %% [markdown]
# ## 3 · From impact to level (5')
#
# The policy's steps: High impact gives **Top Secret**, Medium **Secret**, None **Public**. A Low
# impact needs two more questions: would disclosure conflict with a law (step 4)? If yes,
# **Restricted**. If not, do the benefits of disclosure outweigh the harm (step 5)? If yes,
# **Public**, otherwise **Restricted**. Inside Restricted the sub-level follows the scale of the
# impact: **A** a whole sector, **B** several entities or a group of individuals, **C** one entity
# or one individual.
#
# ✏️ **Exercise** · Write `classify(level, conflicts_with_law, benefits_outweigh, scale)`.

# %%
def classify(level: str, conflicts_with_law: bool, benefits_outweigh: bool, scale: str) -> tuple[str, str]:
    # BEGIN SOLUTION
    if level == "High":
        return "Top Secret", ""
    if level == "Medium":
        return "Secret", ""
    if level == "None":
        return "Public", ""
    if conflicts_with_law or not benefits_outweigh:
        sub = {"sector": "A", "group": "B", "one": "C"}[scale]
        return "Restricted", sub
    return "Public", ""
    # END SOLUTION

# %%
# Disclosing children's or guardians' records would break the PDPL: step 4 answers yes for them.
LAW = {"fee_schedule": False, "guardians": True, "students": True, "attendance": True, "fees": True,
       "attendance_summary": True}
SCALE = {d["name"]: ("group" if d["individuals"] or d["name"] == "attendance_summary" else "one") for d in inventory}
try:
    levels = {n: classify(impact[n]["level"], LAW[n], False, SCALE[n]) for n in impact}
except NotImplementedError:
    levels = {r["name"]: (r["level"], r["sub_level"]) for r in U.reference("lab21_register")}
print(levels)
U.check(levels["fee_schedule"][0] == "Public", "the published fee schedule is Public")
U.check(all(levels[n] == ("Restricted", "B") for n in ("guardians", "students", "attendance", "fees")),
        "the four record sets are Restricted, category B")

# %% [markdown]
# ## 4 · An aggregate that still points at a child (5')
#
# The summary table looks harmless: rates, no names. ✏️ **Exercise** · Write `small_cells(df, k)`
# returning the rows with fewer than `k` students. With a campus, a grade and a gender, a cell of
# one or two students is a child's attendance record.

# %%
summary = U.load("attendance_summary.csv")
summary["students"] = summary["students"].astype(int)

def small_cells(df: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    # BEGIN SOLUTION
    return df[df["students"] < k]
    # END SOLUTION

# %%
try:
    small = small_cells(summary)
except NotImplementedError:
    small = pd.DataFrame(U.reference("lab21_small"))
print(len(small), "of", len(summary), "cells have fewer than five students")
small.head(8)

# %% [markdown]
# ## 5 · The register (3')
#
# ✏️ **Exercise** · Build the register: one row per set with `name`, `level`, `sub_level`,
# `impact`, `reason`, `owner` and `review_by` (the policy has the classification reviewed within a
# month of the first classification). Unclassified data is treated as Restricted until it is
# classified.

# %%
REVIEW_BY = str(U.TODAY + timedelta(days=30))

def register_rows() -> list[dict]:
    # BEGIN SOLUTION
    reasons = {
        "fee_schedule": "Already published on the website; disclosure has no impact.",
        "guardians": "Names, national IDs, mobiles and IBANs of individuals; disclosure would breach the PDPL.",
        "students": "Children's identities and health notes; disclosure would breach the PDPL.",
        "attendance": "Each child's absences, with notes that can reveal health.",
        "fees": "Each family's payments and balance: detailed statements of individual transactions.",
        "attendance_summary": f"{len(small)} cells have under five students, so rates can point at a child.",
    }
    owners = {d["name"]: d["owner"] for d in inventory}
    return [{"name": n, "level": levels[n][0], "sub_level": levels[n][1],
             "impact": f"{impact[n]['category']} / {impact[n]['level']}", "reason": reasons[n],
             "owner": owners[n], "review_by": REVIEW_BY} for n in impact]
    # END SOLUTION

# %%
try:
    register = pd.DataFrame(register_rows())
except NotImplementedError:
    register = pd.DataFrame(U.reference("lab21_register"))
U.check(len(register) == 6 and register["reason"].str.len().min() > 20, "six rows, each with a reason")
register

# %% [markdown]
# ## ✱ Stretch · Suppress and classify again
#
# Replace the rate of every cell under five with an empty value (or merge it into its grade band)
# and run the assessment again. What level does the suppressed table get, and what may Rawafid then
# do with it under the Open Data Policy?

# %% [markdown]
# ## Check yourself
#
# 1. Why does the policy send a Low impact through two more steps instead of straight to Restricted?
# 2. Which principle decides the level of a file that joins the fee schedule with the fees file?
# 3. Rawafid is a private group. Why does it use this policy at all?
#
# <details><summary>Answers</summary>
#
# 1. Open by default: a low-impact set may still be Public when no law forbids disclosure and the benefits outweigh the harm.
# 2. Highest level of protection: combined data takes the highest level of its parts, so Restricted.
# 3. The policy is written for public entities; Rawafid's own data policy adopts it, and the PDPL binds Rawafid by law in any case.
# </details>
#
# **Carry forward.** Lab 2.2 starts from the reference register in `data/reference/lab21_register.json`.
