---
course: "Responsible Data and AI Practice in the Kingdom"
code: "FN-106"
version: "2027.1.0"
deck: "day1"
day: 1
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fn-106/slides/day1.html"
---

# Responsible Data and AI Practice in the Kingdom

## Day 1: Personal data and the law

Map, justify, minimise, pseudonymise and keep the data of one build

#### [day1#title] Personal data and the law

*SDAIA Academy · Responsible Data and AI Practice in the Kingdom*

Day 1: Map, justify, minimise, pseudonymise and keep the data of one build

Data & AI Foundations Track · 3 teaching days + capstone day · 4 sessions · 4 labs · FN-106

#### [day1#three-days-one-build] Three days on one build, then a review of your build pack

*The course at a glance*

- **Day 1 · The law.** Where personal data flows, the legal basis, minimisation, pseudonyms, retention and breaches.
- **Day 2 · Classify and share.** Classification levels, what may reach an external model, sharing, licences.
- **Day 3 · Ethics and risk.** Principles as tests, Arabic and English fairness, the risk register, the disclosure.
- **Day 4 · Capstone.** A responsible build pack in a public repository, defended in ten minutes.

> **Every lab adds a page to the pack.** By Day 3 you hold the registers, the code, the test report and the disclosure the capstone asks for.

#### [day1#rawafid-and-wafi] Rawafid Schools Group and Wafi, its parent-enquiry assistant

*One case all week*

A fictional private school group: four campuses, about 1,200 students, parents who write in Arabic and English. Its systems lead built **Wafi** (وافي), which drafts replies from attendance and fee records with a language model.

- **Dr. Amal Al-Sayari.** Group director of schools. Owns the build and its risks.
- **Nasser Al-Mansour.** Data protection officer. Your client this week.
- **Dana Al-Saleh.** Systems lead. Built Wafi fast, and it shows.

#### [day1#how-this-course-works] Read the official text, then turn it into code and records

*How this course works*

- **Primary sources.** Every rule on a slide comes from the instrument itself, named in the notes. Commentary is not a source.
- **Evidence, not opinion.** A finding is a number from a lab run: fields sent, names re-identified, a gap between languages.
- **Synthetic data only.** No real person enters any lab, prompt or assistant. That is what lets us use a free hosted model.

> **AI policy.** AI off for the scenario check and each first classification. An assistant may help you read the instruments; check every answer against the official text. No real personal data in any assistant.

#### [day1#setup-check] Open the labs and run the setup check before the first lab

*Lab environment*

1. **Colab:** open a notebook from the course page; its first cell clones the repository.
2. **Laptop:** clone, then `uv sync` in `labs/` and open Jupyter.
3. No key is needed: Wafi answers through a **scripted stand-in model** unless you set a free OpenRouter key.
4. Every lab starts from supplied files. None needs another lab's result.

```bash
# file: terminal (laptop)
git clone https://github.com/SDAIAAcademy/fn-106
cd fn-106/labs
uv sync
uv run jupyter lab
```

#### [day1#agenda] Personal data and the law

*Today*

- **Session 1 · Where personal data flows in a build**: Prompts, logs, caches and the model provider are all places where personal data goes
- **Session 2 · Lawful basis and minimisation**: Every flow needs a legal basis and a purpose, and every field must earn its place against that purpose
- **Session 3 · Pseudonymisation and its limits**: A pseudonym hides a name, not a person: quasi-identifiers link records back
- **Session 4 · Rights, retention and breaches**: Rights, retention rules and the breach procedure turn the law into dates and duties

### Session 1: Where personal data flows in a build

#### [day1#s1] Where personal data flows in a build

*Session 1*

- Identify the personal and sensitive data a build reads, sends, logs and stores
- Draw a data flow diagram of an AI assistant with every store and external party
- Name the PDPL obligation that applies at each step of the flow

#### [day1#what-personal-data-is] Personal data is anything that can identify a person, directly or not

*The law's starting point*

- **Directly:** a name, a national ID number, a mobile number.
- **Indirectly:** a campus, a grade and a date of birth together.
- **Sensitive data** is a named list in the law: racial or ethnic origin, beliefs, criminal and security data, biometric and genetic data, health data, and data showing a parent is unknown.
- It applies to processing in the Kingdom, and from abroad for people living here.

- **At Rawafid.** A note "asthma flare" on an absence is health data about a child. So is "insulin at lunch" in a student file.

#### [day1#who-is-who] The controller decides, the processor acts for it, the data subject has the rights

*Three roles*

| Role | In the law | At Rawafid |
| --- | --- | --- |
| **Controller** | Decides why and how data is processed; carries the obligations | Rawafid Schools Group |
| **Processor** | Processes for the controller; chosen only if it gives the necessary guarantees | The model provider, the hosting company |
| **Data subject** | The person the data is about, or their legal guardian | Each student, represented by a guardian; each guardian |

> **A minor's rights are exercised by the guardian,** and the guardian's authority must be verified.

#### [day1#stores-you-forget] Prompts, logs and caches are stores of personal data too

*Where an AI build keeps data*

- **Records.** The systems the build reads: students, guardians, attendance, fees.
- **Prompts.** Everything the build sends to the model leaves your systems.
- **Logs.** Often the full prompt and the reply, kept "for debugging", for ever.
- **Caches and queues.** Replies kept for reuse; drafts waiting for staff.

> **What goes wrong.** Teams map the database and forget the log. The log usually holds more personal data per row than any table.

#### [day1#wafi-pipeline] One parent message passes through nine steps

*The build as Dana wrote it*

1. **1 · Intake** mobile and message
2. **2 to 4 · Look up** guardian, child, attendance, fees
3. **5 · Prompt** to the model provider
4. **6 · Draft** back from the model
5. **7 to 9 · Keep** review queue, log, cache

Lab 1.1 runs one enquiry through this pipeline with a tracer that records every field at every step.

#### [day1#twenty-one-fields] One question about absences sends 21 fields out of Rawafid

*Measured in Lab 1.1*

- **21** fields in one prompt
- **8** of them identifiers
- **1** sensitive: the health notes

The prompt carries the whole student record, the guardian's name, national ID and mobile, and three counts. The question needed one count.

#### [day1#data-flow-diagram] A data flow diagram shows every place data goes and what goes there

*The tool for this session*

```
# file: Mermaid (part)
flowchart LR
  Wafi([Wafi])
  ModelProvider["model provider"]
  WafiEnquiryLog["Wafi enquiry log"]
  Wafi -->|"5 send prompt: send 21"| ModelProvider
  Wafi -->|"8 log: log 4"| WafiEnquiryLog
```

- Nodes: the build, each store, each outside party.
- Edges: one per step, labelled with what moves.
- Annotate each edge with the obligation that applies there.
- Mermaid is text: it lives in the repository and changes with the code. draw.io is the drawing alternative.

#### [day1#obligations-on-the-diagram] Each step of the flow carries its own obligation

*From diagram to duties*

| Step | Obligation (Personal Data Protection Law) |
| --- | --- |
| Intake | Tell the guardian the basis, the purpose and who receives the data (Article 13) |
| Look up | A legal basis and purpose (Articles 5, 6, 10); accuracy (Article 14) |
| Prompt | Minimum content (Article 11); security (Article 19); transfer abroad (Article 29) |
| Draft | Accuracy before anything is sent to the guardian (Article 14) |
| Log and cache | Destruction when no longer needed (Article 18); security (Article 19) |
| Whole activity | A record of processing (Article 31) |

#### [day1#check-where-data-lives] Which store did Dana forget?

*Checkpoint*

**Question:** Dana's data map lists the student system, the fee system and the model provider. Wafi writes every prompt to its enquiry log. What does the map miss?

- A. Nothing: the provider is the only other store
- B. The log, which holds the full prompt of every enquiry
- C. Only debug output, which the law does not cover
- D. The cache, but caches hold no personal data

#### [day1#lab-1-1] Trace Wafi's personal data

Lab 1.1 · 25 min

Map every field the assistant reads, sends, logs and stores on a data flow diagram.

[D1_1_map_every_field.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D1_1_map_every_field.ipynb)

- [ ] Run one enquiry through the instrumented Wafi (4 min)
- [ ] List every field read, sent, logged and stored (7 min)
- [ ] Flag the identifiers and the sensitive fields (4 min)
- [ ] Draw the data flow diagram in Mermaid (5 min)
- [ ] Name the PDPL obligation at each step (5 min)
- [ ] ✱ Stretch: Add the hosted provider's own logs as a store you do not control

### Session 2: Lawful basis and minimisation

#### [day1#s2] Lawful basis and minimisation

*Session 2*

- Choose a legal basis and a purpose for each flow of a build
- Test each field against the purpose and remove what it does not need
- Rewrite a prompt builder so it sends the minimum

#### [day1#consent-is-the-default] Consent is the default; the law lists when processing runs without it

*The rule and its exceptions*

- **Consent (Article 5).** No processing and no change of purpose without the data subject's consent, which can be withdrawn at any time. For a minor, the guardian consents.

- **Without consent (Article 6).** The data subject's actual interest when contact is impossible; another law or an agreement the data subject is party to; a public entity's security or judicial needs; the controller's legitimate interest.
- **The catch.** Legitimate interest never covers sensitive data.

#### [day1#five-flows-five-bases] Each flow gets its own basis and purpose

*Wafi's five flows*

| Flow | Basis | Purpose |
| --- | --- | --- |
| F1 · answer the guardian | contract | The enrolment contract the guardian signed |
| F2 · draft with a model | contract | The provider acts as processor for F1 |
| F3 · keep a log | legitimate interest | Quality and complaints, **without sensitive data** |
| F4 · cache replies | legitimate interest | Avoid repeated model calls |
| F5 · add summer-camp offers | consent | Advertising needs prior consent and a way to stop |

#### [day1#purpose-limits-content] The purpose decides which fields may be collected and sent

*Minimisation*

- The purpose must relate directly to the controller's purposes (Article 11).
- Content is limited to **the minimum the purpose needs**.
- Data not needed any more is no longer collected, and what was collected is destroyed.
- Data is processed only for the purpose it was collected for, with listed exceptions (Article 10).

- **The guideline's test, per field.** Actual need, purpose, method of collection, content, destruction, retention. If a field fails "actual need", it goes.

#### [day1#field-by-field] Five of the 21 fields are needed to answer the question

*Measured in Lab 1.2*

- **Keep.** The child's first name, absences this term, late arrivals this term, the fee balance, the message.
- **Drop: 16 fields.** Both national IDs, the guardian's mobile and name, date of birth, nationality, campus, section, bus route, health notes and the internal IDs.

| Item | Value |
| --- | --- |
| Before | 678 characters |
| After | 286 characters |

#### [day1#minimised-builder] Send facts, not records

*The change in code*

```python
# file: build_prompt_min (Lab 1.2)
name = (student["full_name_ar"] if is_arabic(text) else student["full_name"]).split()[0]
data = {"first_name": name, **facts}   # three counts, nothing else
prompt = ("You are Wafi ... using only these facts.\n"
          f"Facts: {json.dumps(data, ensure_ascii=False)}\n"
          f"Guardian message: {text}")
```

> **Pattern.** Compute what the question needs inside your systems; send the answer's ingredients, never the source rows.

#### [day1#children-and-guardians] For a child, the guardian consents and exercises the rights

*A school's special case*

- When a data subject lacks full legal capacity, the legal guardian acts in the child's best interest.
- The controller takes appropriate steps to **verify the guardianship** before relying on it.
- The guardian's consent may not harm the child's interests.
- When the child reaches legal capacity, they exercise their rights themselves.

> **What goes wrong.** Wafi finds the family by mobile number. A number shared between two families, or a parent without custody, gets another child's data.

#### [day1#check-basis-and-health] Can the log run on legitimate interest?

*Checkpoint*

**Question:** Dana says the enquiry log runs on Rawafid's legitimate interest in quality checks. The log keeps full prompts, health notes included. Is that basis available?

- A. Yes: quality checking is a legitimate interest
- B. Yes: the enrolment contract covers all of Wafi
- C. No: every flow needs the guardian's consent
- D. No: legitimate interest excludes sensitive data

#### [day1#lab-1-2] Lawful basis and minimum fields

Lab 1.2 · 25 min

Set a lawful basis and purpose for each flow and remove the fields the purpose does not need.

[D1_2_set_lawful_basis.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D1_2_set_lawful_basis.ipynb)

- [ ] Set a basis and purpose for each of the five flows (6 min)
- [ ] Test each prompt field against the purpose (6 min)
- [ ] Write the minimised prompt builder (7 min)
- [ ] Check ten prompts and print the before-and-after list (6 min)
- [ ] ✱ Stretch: Draft the consent wording for the one optional flow

### Session 3: Pseudonymisation and its limits

#### [day1#s3] Pseudonymisation and its limits

*Session 3*

- Pseudonymise identifiers with a keyed hash and keep the key apart
- Attempt re-identification by joining on quasi-identifiers
- Generalise quasi-identifiers and measure the remaining risk

#### [day1#three-words] Minimised, pseudonymised and anonymised are three different promises

*Three words people mix up*

- **Minimised.** Fewer fields. What is left still identifies the person.
- **Pseudonymised.** Identifiers replaced by codes; the extra information that links back is kept apart. **Still personal data.**
- **Anonymised.** Irreversibly unidentifiable, directly and indirectly. Outside the law, **once tested** for re-identification.

#### [day1#keyed-hash] Use a keyed hash, and keep the key away from the data

*How to pseudonymise*

```python
# file: Lab 1.3
def code(value, key):
    mac = hmac.new(key.encode(), value.encode(),
                   hashlib.sha256)
    return "P" + mac.hexdigest()[:10]

out = df.drop(columns=["full_name",
                       "full_name_ar", "national_id"])
out["student_id"] = out["student_id"].map(
    lambda v: code(v, KEY))
```

- Same person, same code: joins across files still work.
- Without the key nobody can recompute a code.
- A **plain** hash is not a pseudonym: anyone can hash every student number and look it up.

#### [day1#quasi-identifiers] Quasi-identifiers link a record back to a name

*The attacker's tool*

1. **Pseudonymised file** campus, grade, gender, date of birth, health notes
2. **Join** on the four shared columns
3. **Public page** sports-day results: name, campus, grade, gender, date of birth

No single column identifies a child. Together they almost always do.

#### [day1#ninety-six-percent] A join re-identifies 96% of the names on the sports-day page

*Measured in Lab 1.3*

- **308 / 320** page names matched to one record
- **26** children whose health note is now known
- **0** names in the pseudonymised file

> **What goes wrong.** "We removed the names" is the most common description of a file that is still personal data.

#### [day1#generalise] Generalising cuts the attack to almost nothing, and leaves the rare child exposed

*The fix, and its limit*

| Item | Value |
| --- | --- |
| Exact birth date and grade | 96% |
| Birth year and grade band | 0.3% |

- Birth date becomes birth year; grade becomes a band of three.
- One page name still matches one record.
- The smallest group holds **one** child: k = 1.
- 33 of 121 groups hold fewer than five children.

#### [day1#test-before-you-claim] Claim anonymity only after you have tried to break it

*The rule for any release*

1. **1 · Remove** direct identifiers
2. **2 · Attack** join with what is public
3. **3 · Generalise** and suppress small groups
4. **4 · Measure** rate and k, written down

> **Your evidence for LO4:** the before-and-after field list, the pseudonymisation script and the re-identification result.

#### [day1#check-hashed-id] Is the contractor's file still personal data?

*Checkpoint*

**Question:** Dana sends a contractor the student file with names and national IDs removed and student numbers replaced by HMAC codes. Rawafid keeps the key. Under the PDPL guidelines, what is the file?

- A. Personal data, because it can be linked back
- B. Anonymous data, because no names remain
- C. Outside the law, because the codes are encrypted
- D. Personal data only while Rawafid holds it

#### [day1#lab-1-3] Pseudonymise, then attack

Lab 1.3 · 25 min

Pseudonymise the guardian and student records and attempt to re-identify them by linkage.

[D1_3_pseudonymise_guardian_student.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D1_3_pseudonymise_guardian_student.ipynb)

- [ ] Replace identifiers with keyed pseudonyms (6 min)
- [ ] Join with the sports-day page on quasi-identifiers (6 min)
- [ ] Measure the re-identification rate (4 min)
- [ ] Generalise birth date and grade, measure again (6 min)
- [ ] Record k and the residual risk (3 min)
- [ ] ✱ Stretch: Show that an unkeyed hash of a student number is reversed by trying every number

### Session 4: Rights, retention and breaches

#### [day1#s4] Rights, retention and breaches

*Session 4*

- Explain the data subject's rights and who exercises them for a minor
- Write a retention rule per store and find what is kept too long
- Walk a breach through notice, containment and documentation

#### [day1#five-rights] Five rights, answered within 30 days

*What the data subject may ask*

1. To be told the legal basis and purpose.
2. To access their data.
3. To obtain it in a readable, clear format.
4. To have it corrected, completed or updated.
5. To have it destroyed when no longer needed.

**30 days** to act on a request, extendable by 30 with notice and reasons

- **For Wafi.** A guardian's request covers the log and the cache, not only the student system.

#### [day1#destroy-when-done] Destroy data once its purpose is met, unless a law says keep it

*Retention*

- Destroy without undue delay once the purpose no longer needs the data (Article 18).
- Keep it only for a legal basis with a set period, or a case before a court.
- Data with nothing that identifies the person may be kept.
- Destroy every copy, backups included, and tell those you disclosed it to.

- **A rule has three parts.** **Period** (90 days), **start** (the date of the enquiry), **method** (scheduled deletion of rows and backups).

#### [day1#log-past-its-rule] Under a 90-day rule, 78% of Wafi's log should not exist

*Measured in Lab 1.4*

**1,027** of 1,315 log rows older than 90 days

- The oldest row is from the pilot's first week, 2025-09-14.
- Each row holds a full prompt: a child's record.
- The rule is 60 days for complaints to arrive plus 30 to investigate them.

#### [day1#breach-three-stages] A breach has three stages: notify, contain, document

*The breach guide*

1. **1 · Notify SDAIA** within 72 hours of becoming aware, when harm is expected
2. **2 · Contain** stop it, change what can be changed, tell the data subjects
3. **3 · Document** keep the notice, the actions and the lessons

> **The clock starts at awareness,** not on the day of the breach and not when the investigation ends.

#### [day1#five-contents] Five contents, written while the clock runs

*What the notice to SDAIA holds*

|  | Content | For Rawafid's incident |
| --- | --- | --- |
| 1 | What happened, when, how, and when you became aware | Log export on a shared drive; found 2026-11-09 |
| 2 | Categories and numbers of data subjects; kinds of data | 434 students, 396 guardians; IDs, health notes |
| 3 | Risks, remedial actions, measures against recurrence | Link removed; prompts minimised; log at 90 days |
| 4 | Whether data subjects are or will be notified | Yes, without undue delay |
| 5 | Contact of the controller or its DPO | Nasser Al-Mansour |

#### [day1#records-of-processing] A record of processing lists what you have just mapped

*The record that ties it together*

- Controller and DPO contacts; the purpose.
- Categories of data subjects and of data.
- Who receives it; transfers outside the Kingdom.
- Retention period per category; security measures.

- **Kept in writing, up to date.** Available to the competent authority on request, and kept five years after the activity ends.

#### [day1#check-seventy-two-hours] When must Rawafid have notified SDAIA?

*Checkpoint*

**Question:** The export went on the shared drive on 2026-10-21. Dana found the public link and told the DPO on 2026-11-09. Harm to the children is expected. By when must SDAIA be notified?

- A. By 2026-10-24, three days after the upload
- B. When the investigation is finished
- C. Within 72 hours of 2026-11-09, so by 2026-11-12
- D. Only if someone is shown to have misused the data

#### [day1#lab-1-4] Retention and a seeded breach

Lab 1.4 · 25 min

Write a retention rule per store and walk a seeded breach through the PDPL breach guideline.

[D1_4_write_retention_rule.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D1_4_write_retention_rule.ipynb)

- [ ] Write a retention rule per store (6 min)
- [ ] Count log rows past the rule (4 min)
- [ ] Read the incident and size the breach (5 min)
- [ ] Draft the notice to SDAIA with its five contents (6 min)
- [ ] Decide the notice to guardians (4 min)
- [ ] ✱ Stretch: Add the breach to the documentation record with its corrective actions

#### [day1#wrap-up] Map everything, send the minimum, and test before you call it anonymous

*Day 1 · Three things to keep*

- **The log is a store.** Prompts, logs, caches and the provider all hold personal data, with all the obligations.
- **Facts, not records.** One question needed 5 of 21 fields. Basis and purpose decide which.
- **Pseudonymised is personal.** 96% came back by a join. Measure k, write it down, and keep the key apart.

#### [day1#next] Tomorrow: classify the data, then decide where it may go

*Before Day 2*

- Read the Data Classification Policy's table of levels and its impact categories (about 15 minutes).
- Keep your Lab 1.1 diagram and Lab 1.2 field list: Lab 2.2 applies tomorrow's rule to the same prompt.
- Finish any Day 1 lab: the reference results in `data/reference/` let you start Day 2 without them.
