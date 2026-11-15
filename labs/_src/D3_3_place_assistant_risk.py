# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 3.3 · Tier and register
#
# Day 3 · Session 3 (Risk tier and risk register) · 25 min.
#
# Dr. Amal asks one question before Wafi goes to all four campuses: how risky is it, and who is
# answering for each risk? You place Wafi in a risk level of the AI Ethics Principles, then work
# through the National AI Risk Management Framework: rate five harms by likelihood and impact,
# compute their levels, choose a treatment, an owner and a review date, and rate what remains.
#
# **Reference state.** `data/harms.json`: five candidate harms with the facts behind each, drawn
# from the earlier labs. Nothing from your own earlier labs.
#
# **Tasks**
# - [ ] 1 · Place Wafi in an ethics risk tier with reasons (5')
# - [ ] 2 · Rate five harms by likelihood and impact (8')
# - [ ] 3 · Compute levels and bands (3')
# - [ ] 4 · Choose a treatment, owner and review date per harm (6')
# - [ ] 5 · Rate the residual risk again (3')
# - [ ] ✱ Stretch · Change one fact (replies sent without review) and redo the tier

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

harms = U.json("harms.json")
for h in harms:
    print(f"{h['id']}  {h['harm']}\n     facts: {h['facts']}")

# %% [markdown]
# ## 1 · The ethics risk tier (5')
#
# The AI Ethics Principles set four levels: **little or no risk** (no restrictions, ethics
# recommended), **limited risk** (the principles apply), **high risk** to basic rights (conformity
# assessments before and after deployment, and the statutory requirements), and **unacceptable risk**
# (not allowed, for example exploitation of children).
#
# What Wafi does today: it drafts replies to guardians from records of minors; routine replies are
# sent without review; sensitive enquiries are meant to go to a person before any reply.
#
# ✏️ **Exercise** · Return the tier and three reasons, one of which says what would move it up.

# %%
TIERS = ["little or no risk", "limited risk", "high risk", "unacceptable risk"]

def place_tier() -> dict:
    # BEGIN SOLUTION
    return {"tier": "limited risk", "reasons": [
        "Wafi answers factual questions from records; it decides nothing about a child's admission, grades, discipline or fees.",
        "Every enquiry about health, safety, custody, complaints or disputed fees is meant to reach a person before any reply.",
        "It would move to high risk if sensitive replies were sent without review, or if it began to decide anything about a child.",
    ]}
    # END SOLUTION

# %%
try:
    tier = place_tier()
except NotImplementedError:
    tier = U.reference("lab33_tier")
U.check(tier["tier"] in TIERS and len(tier["reasons"]) >= 3, "a tier with three reasons")
print(tier["tier"]); [print(" -", r) for r in tier["reasons"]]

# %% [markdown]
# **Look at** the condition in the third reason. Lab 3.2 showed that some Arabic sensitive
# enquiries are not escalated today: the tier holds only if the routing works.

# %% [markdown]
# ## 2 · Rate the five harms (8')
#
# The framework's scales (four points each):
#
# | | 1 | 2 | 3 | 4 |
# |---|---|---|---|---|
# | **Likelihood** | rare | unlikely | likely | almost certain |
# | **Impact** | low | medium | high | catastrophic |
#
# Its catastrophic examples include a large leak of minors' or health data. ✏️ **Exercise** · Return
# `{harm id: {"likelihood": n, "impact": n, "why": "..."}}` for the five harms, reading each harm's facts.

# %%
def rate() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "H1": {"likelihood": 2, "impact": 3, "why": "Three shared numbers out of 860 guardians; another family's data to the wrong parent."},
        "H2": {"likelihood": 2, "impact": 4, "why": "One export already leaked; the log holds minors' IDs and health notes at scale."},
        "H3": {"likelihood": 4, "impact": 2, "why": "Measured on every Arabic run; weaker service, not yet a decision about a child."},
        "H4": {"likelihood": 3, "impact": 2, "why": "A hosted model can misquote numbers; the guardian can check with the school."},
        "H5": {"likelihood": 3, "impact": 3, "why": "Review takes under ten seconds; the reviewed replies are the sensitive ones."},
    }
    # END SOLUTION

# %%
try:
    ratings = rate()
except NotImplementedError:
    ratings = U.reference("lab33_ratings")
U.check(set(ratings) == {h["id"] for h in harms} and all(1 <= v[k] <= 4 for v in ratings.values() for k in ("likelihood", "impact")),
        "five harms rated on the 1 to 4 scales")

# %% [markdown]
# ## 3 · Levels and bands (3')
#
# Level = likelihood × impact. The framework's bands: **1 to 2 low**, **3 to 6 medium**, **8 to 12
# high**, **16 catastrophic**. ✏️ **Exercise** · Write `band(level)`.

# %%
def band(level: int) -> str:
    # BEGIN SOLUTION
    return "low" if level <= 2 else "medium" if level <= 6 else "high" if level <= 12 else "catastrophic"
    # END SOLUTION

# %%
try:
    band(1)
    to_band = band
except NotImplementedError:
    to_band = lambda n: "low" if n <= 2 else "medium" if n <= 6 else "high" if n <= 12 else "catastrophic"
register = pd.DataFrame([{"id": h["id"], "harm": h["harm"], **{k: ratings[h["id"]][k] for k in ("likelihood", "impact")}}
                         for h in harms])
register["level"] = register["likelihood"] * register["impact"]
register["band"] = register["level"].map(to_band)
U.check(to_band(16) == "catastrophic" and to_band(8) == "high" and to_band(6) == "medium", "the bands follow the framework")
register[["id", "likelihood", "impact", "level", "band"]]

# %% [markdown]
# ## 4 · Treatment, owner, review date (6')
#
# The framework's four treatments: **avoid** (stop the activity), **mitigate** (reduce likelihood or
# impact), **transfer** (share it, for example by contract or insurance), **accept** (with a reason,
# by someone with the authority). ✏️ **Exercise** · Return, per harm, a treatment, the control in one
# line, an owner from Rawafid's people (Dr. Amal Al-Sayari, Nasser Al-Mansour, Layla Haddad, Osama
# Al-Qurashi, Dana Al-Saleh), and the likelihood and impact you expect after the control.

# %%
def treat() -> dict[str, dict]:
    # BEGIN SOLUTION
    return {
        "H1": {"treatment": "mitigate", "control": "Answer only when the mobile matches one guardian and the child is named; otherwise send to staff.",
               "owner": "Dana Al-Saleh", "after": [1, 3]},
        "H2": {"treatment": "mitigate", "control": "Minimised prompts, no health notes, log rows deleted after 90 days, the old export traced and deleted.",
               "owner": "Nasser Al-Mansour", "after": [1, 4]},
        "H3": {"treatment": "mitigate", "control": "Arabic routing words in both varieties; the forty-enquiry test rerun before each release.",
               "owner": "Layla Haddad", "after": [2, 2]},
        "H4": {"treatment": "mitigate", "control": "Numbers copied from the records into fixed reply sentences, never written by the model.",
               "owner": "Osama Al-Qurashi", "after": [1, 2]},
        "H5": {"treatment": "mitigate", "control": "A three-point review checklist and a weekly sample of approved drafts read by a second person.",
               "owner": "Dr. Amal Al-Sayari", "after": [2, 3]},
    }
    # END SOLUTION

# %%
try:
    plan = treat()
except NotImplementedError:
    plan = {r["id"]: {"treatment": r["treatment"], "control": r["control"], "owner": r["owner"],
                      "after": [r["residual_likelihood"], r["residual_impact"]]} for r in U.reference("lab33_register")}
REVIEW_EVERY = {"high": 30, "medium": 90, "low": 180, "catastrophic": 7}   # days, Rawafid's choice
register["treatment"] = register["id"].map(lambda i: plan[i]["treatment"])
register["control"] = register["id"].map(lambda i: plan[i]["control"])
register["owner"] = register["id"].map(lambda i: plan[i]["owner"])
register["review_by"] = register["band"].map(lambda b: str(U.TODAY + timedelta(days=REVIEW_EVERY[b])))
U.check(register["owner"].ne("").all() and register["treatment"].isin(["avoid", "mitigate", "transfer", "accept"]).all(),
        "every risk has a treatment and an owner")

# %% [markdown]
# ## 5 · Residual risk (3')
#
# After treatment the framework rates the risk again. A residual risk that is still high is either
# treated further or accepted by someone with the authority, with a reason, and escalated.

# %%
register["residual_likelihood"] = register["id"].map(lambda i: plan[i]["after"][0])
register["residual_impact"] = register["id"].map(lambda i: plan[i]["after"][1])
register["residual_level"] = register["residual_likelihood"] * register["residual_impact"]
register["residual_band"] = register["residual_level"].map(to_band)
register["decision"] = register["residual_band"].map(lambda b: "escalate to the group director" if b in ("high", "catastrophic") else "accept and monitor")
U.check((register["residual_level"] <= register["level"]).all(), "no treatment makes a risk worse")
register[["id", "level", "band", "treatment", "owner", "review_by", "residual_level", "residual_band", "decision"]]

# %% [markdown]
# **Look at** H2. Its impact stays catastrophic after treatment: minimising the prompt lowers how
# likely a leak is and how much it holds, but a log of children's records is still a log of
# children's records. That is why deletion is part of the control.

# %% [markdown]
# ## ✱ Stretch · Replies sent without review
#
# Dana proposes to send sensitive replies straight away and let staff read them afterwards. Redo the
# tier and H5. Which conformity steps would then apply before deployment?

# %% [markdown]
# ## Check yourself
#
# 1. Why is Wafi "limited risk" today, and what single change would make it "high risk"?
# 2. What is the level and band of a harm rated likely (3) and catastrophic (4)?
# 3. When may a high residual risk be accepted?
#
# <details><summary>Answers</summary>
#
# 1. It informs and decides nothing, and sensitive enquiries reach a person; sending sensitive replies without review, or deciding about a child, would make it high risk.
# 2. 12, high: one step under catastrophic, which is 16.
# 3. Only by someone with the authority to accept it, with a recorded reason, after the treatment options were weighed; otherwise it is escalated.
# </details>
#
# **Carry forward.** The tier and the register are the risk part of the capstone pack.
