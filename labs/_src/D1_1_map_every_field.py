# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2"]
# ///
# %% [markdown]
# # Lab 1.1 · Trace Wafi's personal data
#
# Day 1 · Session 1 (Where personal data flows in a build) · 25 min.
#
# Wafi drafts replies to parents from the school's records. Before anything can be made lawful you
# need to know **every field it reads, sends, logs and stores**, and where each one goes. You run
# Wafi with a tracer, turn the trace into a field inventory, draw the data flow diagram and name the
# PDPL obligation at each step.
#
# **Reference state.** Wafi as Dana built it (`wafi.py`) and the synthetic records in `data/`.
# Nothing from another lab.
#
# **Tasks**
# - [ ] 1 · Run one enquiry through the instrumented Wafi (4')
# - [ ] 2 · List every field read, sent, logged and stored (7')
# - [ ] 3 · Flag the identifiers and the sensitive fields (4')
# - [ ] 4 · Draw the data flow diagram in Mermaid (5')
# - [ ] 5 · Name the PDPL obligation at each step (5')
# - [ ] ✱ Stretch · Add the hosted provider's own logs as a store you do not control
#
# **AI policy.** You may ask an assistant to explain Mermaid syntax. Every obligation you name is
# checked against the law's text, not an assistant's summary.

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

# %% [markdown]
# ## 1 · Run one enquiry through the instrumented Wafi (4')
#
# The tracer records each step: what Wafi **reads**, what it **sends** to the model provider, what it
# **logs** and what it **stores**. Run the cell and read the nine steps.

# %%
tracer = wafi.Tracer()
bot = wafi.Wafi(tracer=tracer, model="standin")
guardian = bot.records.guardians["G0007"]
child = bot.records.children["G0007"][0]
text = f"How many days has {child['full_name'].split()[0]} missed this term?"
out = bot.handle(guardian["mobile"], text)
print("reply:", out["reply"])
for e in tracer.events:
    print(f"{e['step']:<22} {e['action']:<6} {e['where']:<42} {len(e['fields'])} fields")

# %% [markdown]
# ## 2 · List every field read, sent, logged and stored (7')
#
# ✏️ **Exercise** · Write `field_inventory(events)`: one row per field, with four True or False
# columns `read`, `sent`, `logged`, `stored` and a column `where` listing the places it reached.
# The action of each event (`read`, `send`, `log`, `store`) sets one column.

# %%
def field_inventory(events: list[dict]) -> pd.DataFrame:
    # BEGIN SOLUTION
    col = {"read": "read", "send": "sent", "log": "logged", "store": "stored"}
    rows: dict[str, dict] = {}
    for e in events:
        for f in e["fields"]:
            r = rows.setdefault(f, {"field": f, "read": False, "sent": False, "logged": False, "stored": False, "where": set()})
            r[col[e["action"]]] = True
            r["where"].add(e["where"])
    out = pd.DataFrame(rows.values())
    out["where"] = out["where"].map(lambda s: "; ".join(sorted(s)))
    return out.sort_values("field").reset_index(drop=True)
    # END SOLUTION

# %%
# Check, with a safety net: the cells below still run when the exercise is not done yet
try:
    inv = field_inventory(tracer.events)
except NotImplementedError:
    inv = pd.DataFrame(U.reference("lab11_inventory"))
sent = inv[inv["sent"]]
print(len(inv), "fields in the trace;", len(sent), "sent to the model provider")
U.check(len(sent) == 21, "21 fields leave Rawafid in one prompt")
U.check(bool(inv.loc[inv["field"] == "student.national_id", "sent"].iloc[0]), "the student's national ID is in the prompt")
inv.head(12)

# %% [markdown]
# **Look at** the `where` column of `prompt.text`: the full prompt, with everything in it, also
# lands in the enquiry log. A log is a store of personal data like any other.

# %% [markdown]
# ## 3 · Flag the identifiers and the sensitive fields (4')
#
# The PDPL lists the kinds of **sensitive data**, health data among them. A free-text note can carry
# health data too. ✏️ **Exercise** · Write `flag(field)` returning `"sensitive"`, `"identifier"`,
# `"personal"` or `"other"`:
# - sensitive: `student.health_notes`, `attendance.note`
# - identifier: names, national IDs, mobiles, email, IBAN, student and guardian IDs
# - personal: any other `student.`, `guardian.`, `attendance.`, `fees.` or `derived.` field, and the enquiry,
#   prompt and reply texts (they are about a person)
# - other: what is left (the prompt hash)

# %%
IDENTIFIERS = {"full_name", "full_name_ar", "national_id", "mobile", "email", "iban", "student_id", "guardian_id"}

def flag(field: str) -> str:
    # BEGIN SOLUTION
    if field in ("student.health_notes", "attendance.note"):
        return "sensitive"
    if field.split(".", 1)[-1] in IDENTIFIERS:
        return "identifier"
    if field.split(".")[0] in ("student", "guardian", "attendance", "fees", "derived", "enquiry", "prompt", "reply") \
            and field != "prompt.hash":
        return "personal"
    return "other"
    # END SOLUTION

# %%
try:
    inv["kind"] = inv["field"].map(flag)
except NotImplementedError:
    inv["kind"] = inv["field"].map(U.reference("lab11_flags"))
print(inv.groupby(["kind", "sent"]).size().unstack(fill_value=0))
U.check(set(inv.loc[(inv["kind"] == "sensitive") & inv["sent"], "field"]) == {"student.health_notes"},
        "one sensitive field goes to the provider: the health notes")
U.check(int(((inv["kind"] == "identifier") & inv["sent"]).sum()) == 8, "eight identifiers go to the provider")

# %% [markdown]
# ## 4 · Draw the data flow diagram in Mermaid (5')
#
# ✏️ **Exercise** · Write `mermaid(events)` returning a Mermaid `flowchart LR` with one node per
# place (`where`) and one edge per event from `Wafi` to the place for `send`, `log` and `store`, and
# from the place to `Wafi` for `read`. Label each edge with the action and the number of fields.
# Paste the output into <https://mermaid.live> or a Markdown file to see it.

# %%
def node_id(place: str) -> str:
    return "".join(ch for ch in place.title() if ch.isalnum())

def mermaid(events: list[dict]) -> str:
    # BEGIN SOLUTION
    lines = ["flowchart LR", "  Wafi([Wafi])"]
    for place in dict.fromkeys(e["where"] for e in events):
        lines.append(f'  {node_id(place)}["{place}"]')
    for e in events:
        a, b = ("Wafi", node_id(e["where"])) if e["action"] != "read" else (node_id(e["where"]), "Wafi")
        lines.append(f'  {a} -->|"{e["step"]}: {e["action"]} {len(e["fields"])}"| {b}')
    return "\n".join(lines)
    # END SOLUTION

# %%
try:
    dfd = mermaid(tracer.events)
except NotImplementedError:
    dfd = U.reference("lab11_mermaid")["text"]
print(dfd)
U.check(dfd.startswith("flowchart") and "model provider" in dfd and "Wafi enquiry log" in dfd,
        "the diagram shows the provider and the log")

# %% [markdown]
# ## 5 · Name the PDPL obligation at each step (5')
#
# ✏️ **Exercise** · Fill `obligations_by_step()`: for each step, the letters of the obligations from the menu
# that apply there. Then the cell writes them onto the diagram's edges. The trainer's reference
# is checked on the two steps that matter most.
#
# | | Obligation (Personal Data Protection Law) |
# |---|---|
# | A | A legal basis and a purpose for the processing (Articles 5, 6, 10) |
# | B | Content limited to the minimum the purpose needs (Article 11) |
# | C | Tell the data subject, at collection, the basis, the purpose and who receives the data (Article 13) |
# | D | Protect the data with organisational and technical measures (Article 19) |
# | E | Destroy it when no longer needed for the purpose (Article 18) |
# | F | Transfer outside the Kingdom only under the conditions of Article 29 |
# | G | Keep a record of the processing activity (Article 31) |
# | H | Verify accuracy before processing (Article 14) |

# %%
STEPS = [e["step"] for e in tracer.events]

def obligations_by_step() -> dict[str, str]:
    # BEGIN SOLUTION
    return {
    "1 intake": "C",
    "2 find guardian": "AB",
    "3 find student": "AB",
    "4 attendance and fees": "ABH",
    "5 send prompt": "BDF",
    "6 receive draft": "H",
    "7 staff review": "D",
    "8 log": "BDE",
    "9 cache": "DE",
    }
    # END SOLUTION

# %%
try:
    obligations = obligations_by_step()
except NotImplementedError:
    obligations = U.reference("lab11_obligations")
U.check(set(STEPS) <= set(obligations), "every step in the trace has its obligations")
U.check("F" in obligations["5 send prompt"] and "B" in obligations["5 send prompt"],
        "sending to a hosted model is a minimisation and a transfer question")
U.check("E" in obligations["8 log"], "the log must have a destruction rule")
annotated = dfd
for step, letters in obligations.items():
    annotated = annotated.replace(f'"{step}:', f'"{step} [{letters}]:')
print(annotated)

# %% [markdown]
# ## ✱ Stretch · The provider's own logs
#
# A hosted model service may keep prompts on its side under its own terms. Add a node
# `provider logs (not ours)` fed from `model provider`, and say which obligation still applies to
# Rawafid for data it no longer controls.

# %% [markdown]
# ## Check yourself
#
# 1. Which store holds the most personal data per enquiry, and why is that a surprise?
# 2. Why is `attendance.note` flagged sensitive although it is free text?
# 3. Which step is a transfer outside the Kingdom when the endpoint is hosted abroad?
#
# <details><summary>Answers</summary>
#
# 1. The enquiry log: it keeps the full prompt, so the whole student record, for every enquiry.
# 2. Notes such as "asthma flare" or "hospital appointment" are health data about a child.
# 3. Step 5, sending the prompt: everything the prompt carries leaves the Kingdom.
# </details>
#
# **Carry forward.** Lab 1.2 starts from the same 21 sent fields and cuts them down.
