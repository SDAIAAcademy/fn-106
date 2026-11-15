# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 2.2 · Hosted, local or neither
#
# Day 2 · Session 2 (What may reach an external model) · 25 min.
#
# A classification level is only useful when it decides something. Here it decides where data may
# go: to a **hosted** model service, to a model **served locally** on Rawafid's own machines in the
# Kingdom, or **neither**. You write the rule as a function, apply it to the six data sets and to
# each field of Wafi's minimised prompt, and check whether the hosted endpoint makes the prompt a
# transfer outside the Kingdom.
#
# **Reference state.** The reference classification register of Lab 2.1
# (`data/reference/lab21_register.json`) and `wafi.py`. You do not need your own Lab 2.1 result.
#
# **Tasks**
# - [ ] 1 · Write the destination rule as a function (7')
# - [ ] 2 · Apply it to the six data sets (4')
# - [ ] 3 · Apply it field by field to Wafi's prompt (6')
# - [ ] 4 · Check the hosted endpoint's location as a transfer (4')
# - [ ] 5 · Record the permitted destinations (4')
# - [ ] ✱ Stretch · Write the rule for the synthetic class data and say why it differs

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
import pandas as pd
import rawafid as U
import wafi

register = pd.DataFrame(json.loads((U.REF / "lab21_register.json").read_text(encoding="utf-8")))
register[["name", "level", "sub_level", "reason"]]

# %% [markdown]
# ## 1 · The destination rule (7')
#
# What the instruments say, in short:
# - The Generative AI Guidelines for Government: do not enter data classified **Restricted or
#   higher** into generative AI tools; limit their use to **Public** data. Rawafid's policy adopts this
#   for hosted services it does not control.
# - Pseudonymised data is still personal data (Day 1), so it keeps its Restricted level.
# - A locally served model on Rawafid's own machines keeps the data inside Rawafid: Restricted data
#   may go there, **minimised**, under the same access rules as the source system.
# - Sensitive data (health) that the purpose does not need goes nowhere: minimisation decides
#   before any model does.
# - Secret and Top Secret never go to a model in this build.
#
# ✏️ **Exercise** · Write `destination(level, has_sensitive)` returning `"hosted"`, `"local"` or `"neither"`.

# %%
def destination(level: str, has_sensitive: bool) -> str:
    # BEGIN SOLUTION
    if level == "Public":
        return "hosted"
    if level == "Restricted" and not has_sensitive:
        return "local"
    return "neither"
    # END SOLUTION

# %%
try:
    U.check(destination("Public", False) == "hosted" and destination("Restricted", False) == "local"
            and destination("Restricted", True) == "neither" and destination("Secret", False) == "neither",
            "the rule gives the four expected answers")
    rule = destination
except NotImplementedError:
    rule = lambda level, s: "hosted" if level == "Public" else ("local" if level == "Restricted" and not s else "neither")

# %% [markdown]
# ## 2 · The six data sets (4')
#
# The student file holds health notes, and attendance notes can reveal health ("asthma flare").

# %%
SENSITIVE = {"students": True, "attendance": True}
dest = register[["name", "level", "sub_level"]].copy()
dest["has_sensitive"] = dest["name"].map(lambda n: SENSITIVE.get(n, False))
dest["destination"] = [rule(l, s) for l, s in zip(dest["level"], dest["has_sensitive"])]
dest

# %%
U.check(dict(zip(dest["name"], dest["destination"])) == {
    "fee_schedule": "hosted", "guardians": "local", "students": "neither", "attendance": "neither",
    "fees": "local", "attendance_summary": "local"}, "one destination per set")

# %% [markdown]
# ## 3 · Field by field, Wafi's prompt (6')
#
# Data sets are not what a prompt sends: fields are. A count of absences derived from the attendance
# set carries no note, so it is not sensitive, but it is still a child's personal data.
#
# ✏️ **Exercise** · Write `field_level(field)` returning the level of each field of the minimised
# prompt (`wafi.build_prompt_min`), then apply `destination`.

# %%
records = wafi.Records()
s0 = records.students[0]
min_fields = wafi.build_prompt_min("x", s0, records.guardians[s0["guardian_id"]], records.facts(s0["student_id"]))["fields"]

def field_level(field: str) -> str:
    # BEGIN SOLUTION
    return "Restricted"          # a child's name, counts about the child, a guardian's message: all personal
    # END SOLUTION

# %%
try:
    field_dest = {f: rule(field_level(f), False) for f in min_fields}
except NotImplementedError:
    field_dest = U.reference("lab22_fields")
print(field_dest)
U.check(set(field_dest.values()) == {"local"}, "even the minimised prompt may only go to a locally served model")

# %% [markdown]
# **Look at** what this means for Wafi in production: minimisation made the prompt small, not
# Public. With real records Wafi needs a model served inside Rawafid, or a hosted service only for
# questions that carry no personal data (term dates, the published fee schedule).

# %% [markdown]
# ## 4 · Is the hosted endpoint a transfer? (4')
#
# The Personal Data Protection Law allows transfer outside the Kingdom only for listed purposes,
# without harm to national security, with an adequate level of protection and limited to the
# minimum (Article 29); the transfer regulation adds the adequacy list and the safeguards
# (standard contractual clauses, binding common rules, certificates). ✏️ **Exercise** · Write
# `is_transfer(endpoint)`: True when the endpoint processes outside the Kingdom **or its location is
# unknown** (you cannot show it stays inside).

# %%
ENDPOINTS = [
    {"name": "free hosted model used in class", "operator": "an international model router", "location": "unknown"},
    {"name": "model served on Rawafid's own server", "operator": "Rawafid", "location": "Kingdom"},
    {"name": "a cloud region in Riyadh under contract", "operator": "a cloud provider", "location": "Kingdom"},
]

def is_transfer(endpoint: dict) -> bool:
    # BEGIN SOLUTION
    return endpoint["location"] != "Kingdom"
    # END SOLUTION

# %%
try:
    transfers = {e["name"]: is_transfer(e) for e in ENDPOINTS}
except NotImplementedError:
    transfers = {e["name"]: e["location"] != "Kingdom" for e in ENDPOINTS}
print(transfers)
U.check(transfers["free hosted model used in class"] is True, "unknown location counts as a transfer")

# %% [markdown]
# ## 5 · The permitted destinations (4')
#
# ✏️ **Exercise** · Add a `permitted` column in plain words, the evidence of LO3: what may go where,
# and on what condition.

# %%
def permitted(row) -> str:
    # BEGIN SOLUTION
    if row["destination"] == "hosted":
        return "Any model service, hosted or local"
    if row["destination"] == "local":
        return "A model served inside Rawafid, minimised fields only; no hosted service"
    return "No model; derived counts without notes may go to a local model"
    # END SOLUTION

# %%
try:
    dest["permitted"] = dest.apply(permitted, axis=1)
except NotImplementedError:
    dest["permitted"] = [r["permitted"] for r in U.reference("lab22_register")]
dest

# %% [markdown]
# ## ✱ Stretch · Synthetic class data
#
# Every record in `data/` is invented. Write the rule that lets the class send Wafi's prompts to the
# free hosted model, and the one check that must hold before anyone points Wafi at real records.

# %% [markdown]
# ## Check yourself
#
# 1. Does pseudonymising the student file let it go to a hosted model?
# 2. Why is "location unknown" treated as a transfer?
# 3. What is the only kind of Wafi question a hosted service could answer with real data?
#
# <details><summary>Answers</summary>
#
# 1. No: pseudonymised data is still personal data and keeps its Restricted level.
# 2. Because Rawafid must be able to show where the data is processed; if it cannot, it cannot show that Article 29's conditions are met.
# 3. Questions that carry no personal data, answered from Public sets such as the fee schedule or term dates.
# </details>
#
# **Carry forward.** The register with destinations is the LO3 evidence and a capstone part.
