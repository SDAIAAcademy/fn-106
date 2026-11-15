# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 3.4 · Notice and routing rule
#
# Day 3 · Session 4 (Disclosure and human review) · 25 min.
#
# Two things stand between Wafi and the parents of four campuses: a notice that tells them the
# truth, and a rule that sends every sensitive message to a person in either language. You draft the
# notice, check it against the items the law and the guidelines require, write the routing rule,
# test it on the forty enquiries, and choose the build for your capstone.
#
# **Reference state.** `data/enquiries_40.jsonl` and `wafi.py` (Dana's router `ROUTER_V1`). Nothing
# from your own earlier labs.
#
# **Tasks**
# - [ ] 1 · Draft the notice parents see (7')
# - [ ] 2 · Check it against the required items (4')
# - [ ] 3 · Write the routing rule for sensitive replies (6')
# - [ ] 4 · Test the rule on the forty enquiries per language (5')
# - [ ] 5 · Choose your capstone build (3')
# - [ ] ✱ Stretch · Write the Arabic notice and check both say the same

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

import pandas as pd
import rawafid as U
import wafi

enquiries = U.jsonl("enquiries_40.jsonl")

# %% [markdown]
# ## 1 · The notice (7')
#
# What it must say, from three sources:
# - **PDPL Article 13**, before collecting data from the data subject: the purpose and its legal
#   basis, how the data is collected, the controller's identity and contact, who receives it, the
#   consequences of not providing it, and the rights of Article 4.
# - **The Generative AI Guidelines**: tell people when content is produced with generative AI, and
#   offer a channel that does not go through the AI.
# - **The AI Ethics Principles** (transparency, humanity): a person reviews what matters.
#
# ✏️ **Exercise** · Write the notice in plain English, at most 150 words. It appears once when a
# guardian first writes to Wafi and at the foot of the parent portal.

# %%
def draft_notice() -> str:
    # BEGIN SOLUTION
    return (
        "Wafi is Rawafid Schools Group's assistant. It uses generative AI to draft replies to your questions "
        "about your child's attendance, lateness and fees. To answer, it reads your child's first name and "
        "this term's counts from our records; nothing else is sent. Questions about health, safety, custody, "
        "complaints or a disputed fee always go to a member of staff, who replies to you. We use your messages "
        "only to answer them, under our agreement with you as a parent, keep them for 90 days and share them "
        "with no one outside Rawafid. You may ask a person at any time: call your campus office or write "
        "\"staff\". You have the right to know about, see, correct and ask us to delete your data. "
        "Questions: our data protection officer, Nasser Al-Mansour, privacy@rawafid.example."
    )
    # END SOLUTION

# %%
try:
    notice = draft_notice()
except NotImplementedError:
    notice = U.reference("lab34_notice")["text"]
print(notice, f"\n\n({len(notice.split())} words)")

# %% [markdown]
# ## 2 · The required items (4')
#
# Each item is a question a reader should be able to answer from the notice. The check below looks
# for words; you look for meaning. Read the failures, then fix the notice, not the check.

# %%
ITEMS = {
    "says it is AI": ["generative ai", "artificial intelligence"],
    "names who is responsible": ["rawafid"],
    "says what data it uses": ["first name", "counts", "records"],
    "says why, and on what basis": ["to answer", "only to answer", "agreement"],
    "says who receives it": ["share", "outside"],
    "says how long it is kept": ["days", "keep"],
    "offers a person": ["member of staff", "a person", "staff"],
    "names the rights": ["right"],
    "gives a contact": ["@", "officer"],
}
low = notice.lower()
items = {k: any(w in low for w in ws) for k, ws in ITEMS.items()}
U.table([{"item": k, "found": v} for k, v in items.items()])

# %%
U.check(all(items.values()) and len(notice.split()) <= 150, "every required item, in at most 150 words")

# %% [markdown]
# ## 3 · The routing rule (6')
#
# Dana's router knows English words and two Arabic ones. Lab 3.2 measured what that does to Arabic
# guardians. ✏️ **Exercise** · Write `keywords`: a list of words and stems, in English, Modern
# Standard Arabic and Gulf Arabic, that mark an enquiry about health, bullying or harm, a fee
# dispute, a complaint or custody. A word that appears in routine questions ("رسوم", "fee") would
# send every fees question to staff: leave it out.

# %%
def routing_keywords() -> list[str]:
    # BEGIN SOLUTION
    english = ["medication", "allerg", "sick", "nurse", "insulin", "injur", "hurt", "bull", "harass",
               "charged twice", "dispute", "refund", "complain", "custody", "collect", "court"]
    msa = ["دواء", "حساسية", "مريض", "مرض", "ممرض", "إنسولين", "انسولين", "تنمر", "إيذاء", "ضرب",
           "شكوى", "اعتراض", "مرتين", "استرداد", "حضانة", "يستلم"]
    gulf = ["تعبان", "يضايق", "مضايق", "عيال يضربون", "أبي حقي", "خصمتوا", "صك", "محد يستلم"]
    return english + msa + gulf
    # END SOLUTION

def route_v2(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in keywords)

# %%
try:
    keywords = routing_keywords()
except NotImplementedError:
    keywords = U.reference("lab34_router")["keywords"]
print(len(keywords), "keywords")

# %% [markdown]
# ## 4 · Recall and false alarms per language (5')
#
# **Recall**: of the sensitive enquiries, the share the rule sends to staff. **False alarms**: routine
# enquiries it sends to staff. Compare Dana's rule with yours.

# %%
rows = []
for name, rule in [("ROUTER_V1 (Dana)", wafi.route_v1), ("route_v2 (yours)", route_v2)]:
    for lang in ("en", "ar"):
        qs = [q for q in enquiries if q["lang"] == lang]
        sens = [q for q in qs if q["sensitive"]]
        rout = [q for q in qs if not q["sensitive"]]
        rows.append({"rule": name, "lang": lang,
                     "recall": f"{sum(rule(q['text']) for q in sens)}/{len(sens)}",
                     "false alarms": f"{sum(rule(q['text']) for q in rout)}/{len(rout)}",
                     "missed": ", ".join(q["enquiry_id"] for q in sens if not rule(q["text"]))})
recall = pd.DataFrame(rows)
recall

# %%
mine = recall[recall["rule"].str.startswith("route_v2")]
U.check(all(r.split("/")[0] == r.split("/")[1] for r in mine["recall"]), "every sensitive enquiry reaches a person, in both languages")
U.check(all(r.startswith("0/") for r in mine["false alarms"]), "no routine enquiry is sent to staff")

# %% [markdown]
# **Look at** what this test cannot tell you: forty enquiries are the ones you wrote. A keyword list
# that catches all of them has learned this set. Keep a log of the messages staff re-route by hand
# and add to the list from it; the test set grows with it (Lab 3.2's evaluation bias).

# %% [markdown]
# ## 5 · Your capstone build (3')
#
# The capstone pack is about one build: Wafi, as in the course, or an assistant from your own work
# that handles personal data. Write one line: which build, whose data it holds, and the one fact of
# it you are least sure about. The assessor will change a fact of your case in the review.

# %%
CAPSTONE_BUILD = "Wafi, Rawafid's parent-enquiry assistant: guardians' and students' records; least sure of where the hosted model processes prompts."
print(CAPSTONE_BUILD)

# %% [markdown]
# ## ✱ Stretch · The Arabic notice
#
# Write the notice in Arabic for the parent portal. Then check both versions against the same nine
# items: an item present in one language and missing in the other is a transparency failure for half
# of Rawafid's guardians.

# %% [markdown]
# ## Check yourself
#
# 1. Which PDPL article lists what a guardian must be told before data is collected?
# 2. Why must the notice offer a route that does not go through Wafi?
# 3. Why is "رسوم" a poor routing keyword?
#
# <details><summary>Answers</summary>
#
# 1. Article 13: purpose and basis, how it is collected, who is responsible and how to reach them, recipients, the consequences of not providing it, and the rights.
# 2. The Generative AI Guidelines ask for a non-automated channel, and some matters (health, custody) need a person.
# 3. It appears in routine fee questions, so every balance question would go to staff; the router must separate disputes from questions.
# </details>
#
# **Carry forward.** The notice and the routing rule with its recall table are the disclosure part of the capstone pack.
