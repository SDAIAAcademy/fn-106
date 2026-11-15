---
course: "Responsible Data and AI Practice in the Kingdom"
code: "FN-106"
version: "2027.1.0"
scope: "course"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fn-106/"
---

# Responsible Data and AI Practice in the Kingdom

Make one AI build lawful and responsible: map and minimise its personal data, classify and share it under the national policies, test it against the ethics principles and write its risk register and disclosure

Participants make one small build lawful and responsible: a parent-enquiry assistant for a fictional private school group that drafts replies from attendance and fee records with a language model. They map its personal data and minimise it under the Personal Data Protection Law (PDPL), classify each data set under the National Data Management Office (NDMO) policy, decide what may reach an external model, turn the SDAIA AI Ethics Principles into tests, assess risk with the National AI Risk Management Framework, and write the disclosure and records the build needs.

- **Audience:** Beginners. Graduates and career changers entering the AI Engineering or Data Science track; computing and data graduates who pass the placement test skip the courses it covers.
- **Prerequisites:** FN-101 Python for Data and AI Work; FN-105 How Machine Learning and Language Models Work; Reads a short Python program that calls a web API
- **Case study:** Rawafid Schools Group: Rawafid Schools Group is a fictional private school group with four campuses and about 1,200 students. Its systems lead built Wafi, an assistant that drafts replies to parents from attendance and fee records with a language model, and its data protection officer must now make that build lawful and responsible. Every record is synthetic, generated with a fixed seed, and planted with the problems the labs find: a prompt that carries the whole student file, a log kept too long, linkable quasi-identifiers, a partner asking for too much, a non-commercial dataset and a routing rule that only knows English.

## Outcomes

- LO1 (Awareness): Explain the PDPL obligations that govern a build, from lawful basis and minimisation to rights, retention, transfer and breach handling, given the assistant's data flow diagram
- LO2 (Awareness): Distinguish what the data classification, data sharing and open data policies and the SDAIA Generative AI Guidelines each decide, given six questions about the build
- LO3 (Applied): Classify each data set of the build under the four NDMO classification levels and derive the rule for sending it to an external model service, given the school group's data inventory and the policy's impact categories
- LO4 (Applied): Apply minimisation and pseudonymisation to the data the assistant sends, and test whether records can be re-identified, given synthetic student and guardian records
- LO5 (Applied): Prepare a risk assessment that places the assistant in an ethics risk tier and works through the four phases of the national risk framework, given the build description and five candidate harms
- LO6 (Applied): Test the assistant against the ethics principles for fairness across Arabic and English enquiries, transparency and human review, and draft the disclosure parents see, given forty scripted enquiries

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

## Day 2: Classify, share and send

Classify each data set, decide where it may go, and check what you reuse

#### [day2#title] Classify, share and send

*SDAIA Academy · Responsible Data and AI Practice in the Kingdom*

Day 2: Classify each data set, decide where it may go, and check what you reuse

Data & AI Foundations Track · 3 teaching days + capstone day · 4 sessions · 4 labs · FN-106

#### [day2#agenda] Classify, share and send

*Today*

- **Session 1 · Data classification levels**: Classification follows the impact of disclosure: four levels, and sub-levels inside Restricted
- **Session 2 · What may reach an external model**: The classification level decides whether data may go to a hosted model, a locally served one, or neither
- **Session 3 · Sharing with another entity**: A request to share data is judged on purpose, minimum data, access, transparency and destruction
- **Session 4 · Licences and provenance**: Weights, code and data each carry terms, and each instrument decides a different question

#### [day2#review-day1] Which change does the most for Wafi's log?

*Review of Day 1*

**Question:** Wafi's log keeps every full prompt since the pilot began. Nasser can make one change this week. Which one reduces the exposure the most?

- A. Encrypt the log file on disk
- B. Remove the names from old rows
- C. Send minimised prompts and delete rows past 90 days
- D. Add the log to the privacy notice

### Session 1: Data classification levels

#### [day2#s1] Data classification levels

*Session 1*

- Assess the impact category and level of a data set's disclosure
- Assign a classification level with an evidence-based reason
- Spot aggregates that still reveal individuals

#### [day2#why-classify] A classification level is a decision about handling, made once

*What classification is for*

- Every data set gets a level when it is created or received.
- The level decides access, storage, sharing, publication and, today, which model may see it.
- Data not yet classified is treated as **Restricted** until it is.
- The level is reviewed within a month of the first classification.

- **Whose policy?** The NDMO Data Classification Policy is written for public entities. Rawafid, a private group, adopts it in its own data policy; the PDPL binds it by law.

#### [day2#four-levels] The level follows the impact of unauthorised disclosure

*Four levels*

| Level | Impact | Example in the policy |
| --- | --- | --- |
| **Top Secret** | High: exceptionally serious, irreparable | National security information |
| **Secret** | Medium: serious | Information on vital installations |
| **Restricted** | Low: limited | Personal identifiers, a medical file, individual transactions |
| **Public** | None | Published statistics, public announcements |

Restricted has sub-levels by scale: **A** a whole sector, **B** several entities or a group of individuals, **C** one entity or one individual.

#### [day2#impact-categories] Ask what disclosure would harm, then how badly and for how long

*How to assess impact*

- **National interest.** Reputation, security, economy, infrastructure, government functions.
- **Entity activities.** Profits and functions of entities.
- **Individuals.** Health and safety; **privacy**.
- **Environment.** Environmental and natural resources.

The level weighs the duration of the damage, the time to recover and its scale. Every impact named must be specific and evidence-based.

#### [day2#low-impact-two-steps] A low impact still has two questions before it becomes a level

*The policy's process*

1. **Impact Low** limited, short-term, controllable
2. **Step 4** Would disclosure break a law? Yes: Restricted
3. **Step 5** Do the benefits outweigh the harm? Yes: Public. No: Restricted

> **Open by default.** The two steps exist so that data is not locked away when nothing forbids its release.

#### [day2#highest-level-wins] A set built from several levels takes the highest of them

*Combining data*

- **Principle 4 · highest level of protection.** If a data set integrates parts with different levels, the highest level applies.
- **At Rawafid.** The fee schedule (Public) joined with each family's balance (Restricted) is Restricted. So is a prompt that carries one Restricted field.

#### [day2#small-cells] An aggregate table can still describe one child

*Measured in Lab 2.1*

**12 / 95** cells of the attendance summary hold fewer than five students

- Each cell is campus, grade and gender, with an absence rate.
- A cell of one student **is** that student's attendance.
- Until small cells are suppressed or merged, the table is Restricted.

#### [day2#register-day2] Six sets, two levels, one reason each

*The register*

| Set | Level | Reason |
| --- | --- | --- |
| fee_schedule | Public | Already published |
| guardians | Restricted B | Names, national IDs, mobiles, IBANs |
| students | Restricted B | Children's identities and health notes |
| attendance | Restricted B | Absences, with notes that can reveal health |
| fees | Restricted B | Detailed statements of individual transactions |
| attendance_summary | Restricted B | Cells under five students |

#### [day2#check-classify-combined] What level does Dana's new report take?

*Checkpoint*

**Question:** Dana joins the published fee schedule with each family's balance to show who is behind on payments. What is the report's level?

- A. Restricted, the higher of its two parts
- B. Somewhere between Public and Restricted
- C. Public, because the fees are published
- D. Unclassified until someone reviews it

#### [day2#lab-2-1] Classify six data sets

Lab 2.1 · 25 min

Classify the six data sets with the policy's impact categories and record the reasons.

[D2_1_classify_six_data.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D2_1_classify_six_data.ipynb)

- [ ] Read the inventory and the impact categories (4 min)
- [ ] Assess impact category and level per set (8 min)
- [ ] Map impact to level and sub-level (5 min)
- [ ] Find the small cells in the aggregate table (5 min)
- [ ] Record reasons in the register (3 min)
- [ ] ✱ Stretch: Suppress the small cells and classify the aggregate table again

### Session 2: What may reach an external model

#### [day2#s2] What may reach an external model

*Session 2*

- Derive a destination rule from the classification level and the data's nature
- Apply the rule to data sets and to the fields of a prompt
- Recognise a hosted endpoint abroad as a transfer outside the Kingdom

#### [day2#three-destinations] Three destinations: a hosted service, a model you run, or no model

*Where a prompt can go*

- **Hosted.** A provider's model over an API. Fast to start; the data leaves you, under the provider's terms and location.
- **Locally served.** An open-weight model on your own machines in the Kingdom. The data stays under your controls.
- **Neither.** Some data has no business in a prompt at all. Minimisation decides before any model does.

#### [day2#genai-guideline-rule] Generative AI tools get Public data only

*What the guidelines say*

- The Generative AI Guidelines for Government: do not enter data classified **Restricted or higher** into generative AI tools.
- Limit their use to data classified **Public**; check the tool's privacy, disclosure and sharing terms.
- Data analysis with generative AI is limited to Public or open data sets.

- **Rawafid's reading.** The rule covers hosted services Rawafid does not control. A model Rawafid runs itself, under the source system's access rules, may see minimised Restricted fields.

#### [day2#destination-rule-code] Three lines turn a level into a destination

*The rule as code*

```python
# file: Lab 2.2
def destination(level, has_sensitive):
    if level == "Public":
        return "hosted"
    if level == "Restricted" and not has_sensitive:
        return "local"
    return "neither"
```

Pseudonymised data keeps its Restricted level, so pseudonymising does not change the answer.

#### [day2#six-sets-destinations] Only the published fee schedule may go to a hosted model

*Measured in Lab 2.2*

| Item | Value |
| --- | --- |
| fee_schedule | hosted |
| guardians, fees, summary | local |
| students, attendance | neither |

Field by field, all five fields of the minimised prompt are Restricted: **local only**. Minimised is small, not Public.

#### [day2#hosted-is-transfer] A hosted endpoint outside the Kingdom makes every prompt a transfer

*The other half of the question*

- Transfer only for listed purposes, without harm to national security or vital interests.
- With an adequate level of protection abroad, and the **minimum** data needed.
- Otherwise safeguards: standard contractual clauses, binding common rules or a certificate.

- **Location unknown?** Treat it as abroad. If you cannot show where prompts are processed, you cannot show the conditions are met.

#### [day2#class-data-is-synthetic] Synthetic records describe nobody, so they may go anywhere

*Why the class may use a hosted model*

1. **In class** synthetic records, hosted free model
2. **The gate** before real records: classify again
3. **In production** Restricted fields, local model only

> **What goes wrong.** A prototype built on a hosted model is pointed at real data "just for a test". The test is the breach.

#### [day2#check-pseudonymised-hosted] Does pseudonymising open the hosted route?

*Checkpoint*

**Question:** Dana pseudonymises attendance counts with a keyed hash and asks to send them to the free hosted model for a monthly summary. Under Rawafid's rule, where may they go?

- A. To the hosted model, now that they are pseudonymised
- B. To the hosted model, because Rawafid keeps the key
- C. Nowhere: attendance data can never reach a model
- D. To a locally served model only

#### [day2#lab-2-2] Hosted, local or neither

Lab 2.2 · 25 min

Decide for each data set whether it may go to a hosted model, a locally served model or neither.

[D2_2_decide_each_data.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D2_2_decide_each_data.ipynb)

- [ ] Write the destination rule as a function (7 min)
- [ ] Apply it to the six data sets (4 min)
- [ ] Apply it field by field to Wafi's prompt (6 min)
- [ ] Check the hosted endpoint's location as a transfer (4 min)
- [ ] Record the permitted destinations (4 min)
- [ ] ✱ Stretch: Write the rule for the synthetic class data and say why it differs

### Session 3: Sharing with another entity

#### [day2#s3] Sharing with another entity

*Session 3*

- Assess a data request against the Data Sharing Policy principles
- Cut a request down to the minimum data its purpose needs
- Draft the conditions under which data may be shared

#### [day2#partner-request] A research centre asks for three years of attendance, with names

*The request*

- **Purpose:** commute distance and absence in primary and middle school.
- **Fields:** names, national IDs, birth dates, district, guardian's employer, daily records, absence notes, health notes.
- **Storage:** a cloud workspace outside the Kingdom.
- **Retention:** indefinitely; **onward:** research partners when needed.

- **The decision.** Not yes or no: **what**, in which form, **on what conditions**.

#### [day2#eight-principles] Eight principles decide whether and how data is shared

*The Data Sharing Policy*

- **Sharing culture.** Share by default, under the policy.
- **Single source.** The entity that produces data shares it.
- **Legitimate purpose.** A legal basis; used only for that purpose.
- **Authorised access.** Identified, verified people.
- **Transparency.** Data, level, storage, protection, destruction.
- **Accountability.** Shared, under an agreement.
- **Security.** Controls per the national rules.
- **Ethical use.** Fairness, integrity, trust.

#### [day2#pdpl-disclosure-research] The PDPL allows research sharing when the data does not identify the child

*The law's side*

- **Disclosure (Article 15).** Only in listed cases, among them consent, and later processing in a form that cannot identify the data subject directly or indirectly.
- **Research (Article 27).** Without consent when the data does not specifically identify the person, or identity evidence is destroyed first and the data is not sensitive.

> **The health notes fail both.** They are sensitive and they identify; a commute study does not need them.

#### [day2#cut-the-request] Six of eleven requested fields survive, in a coarser form

*Measured in Lab 2.3*

| Requested | Shared as |
| --- | --- |
| date of birth | birth year |
| grade | grade band, grades 1 to 9 only |
| gender, campus, district | as they are |
| daily attendance records | absence counts per month |
| names, national IDs, employer, notes, health notes | refused |

#### [day2#district-trade-off] The field the study needs most makes the smallest groups

*The trade-off in the extract*

- **k = 2** with the district: 4 of 96 groups under five
- **k = 11** without it: no group under five

- Share the district and suppress or merge the small groups before release.
- Or compute commute bands inside Rawafid and share those instead of the district.
- Either way, write the choice into the conditions.

#### [day2#conditions-of-sharing] Yes, on nine conditions

*The answer to the centre*

1. The stated study only.
2. The pseudonymised extract, coarse fields.
3. Labelled Restricted in the metadata.
4. Stored in the Kingdom, or a lawful transfer.
5. Named researchers only.
6. No onward sharing.
7. Destroyed at the end, with a signed confirmation.
8. A secure channel, not email.
9. An agreement signed before any data moves.

#### [day2#check-research-purpose] Is "for research" enough?

*Checkpoint*

**Question:** The centre says the purpose is research, so every requested field should be shared. What does the Data Sharing Policy's legitimate-purpose principle add?

- A. Nothing: research is always a legitimate purpose
- B. The data is used only for the stated purpose, and fields beyond it are not shared
- C. Only public entities may receive data
- D. Data must be stored on the requester's own servers

#### [day2#lab-2-3] A partner's data request

Lab 2.3 · 25 min

Assess a partner entity's request for attendance data against the Data Sharing Policy and draft the conditions.

[D2_3_assess_partner_entity.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D2_3_assess_partner_entity.ipynb)

- [ ] Read the request against the eight principles (6 min)
- [ ] Mark each requested field needed or not (5 min)
- [ ] Draft the conditions of sharing (6 min)
- [ ] Build the minimised extract (5 min)
- [ ] Check the extract for small groups (3 min)
- [ ] ✱ Stretch: Write the destruction confirmation the partner signs

### Session 4: Licences and provenance

#### [day2#s4] Licences and provenance

*Session 4*

- Read the licence of a model and of a dataset from its card
- Record use restrictions and obligations in a licence register
- Name the national instrument that decides a given question

#### [day2#three-things-licensed] Weights, code and data each carry their own terms

*What you reuse*

- **Weights.** An open-source licence, or the vendor's own terms with a use policy.
- **Code.** Usually a standard licence in the repository.
- **Data.** Often Creative Commons, and with a provenance of its own.

> **Open weights are not public domain.** Downloadable does not mean free of conditions.

#### [day2#spdx] An SPDX identifier names one exact licence text

*A shared vocabulary*

| Licence | SPDX identifier |
| --- | --- |
| Apache License 2.0 | `Apache-2.0` |
| Creative Commons Attribution Non Commercial 4.0 | `CC-BY-NC-4.0` |
| A vendor's own terms | `LicenseRef-` and a name |

- A register, a scanner and a lawyer then mean the same thing.
- Cards on model hubs carry a licence tag; read the licence file it points to.
- Record the date you checked: terms change.

#### [day2#three-cards] Two models and one dataset, three different answers

*Read in Lab 2.4*

| Artefact | Licence | For Wafi |
| --- | --- | --- |
| Qwen3-4B (weights) | Apache-2.0 | **Yes**: keep the licence and notices |
| Gemma 3 4B IT (weights) | Gemma Terms of Use | **Yes, with conditions**: use policy, notice file, pass restrictions on |
| Alpaca (dataset) | CC-BY-NC-4.0 | **No**: non-commercial, English only, generated by another company's model |

#### [day2#provenance] Provenance asks where the content came from, and what came with it

*Beyond the licence*

- **Who made it**, from what: a dataset generated by another model may carry that model's terms and errors.
- **Which languages**: an English-only dataset will not teach Gulf Arabic replies.
- **What is inside**: personal data in training text is still personal data.
- **When you checked**, and where the record of it lives.

#### [day2#open-data] Publishing open data means classifying it Public first, then licensing it

*Licences in the other direction*

- Open data is a subset of **Public** data: classify first, publish second.
- Open by default, unless the data needs protection.
- Machine-readable (CSV, JSON), free of charge, no registration.
- Released under a licence that states the conditions of reuse.

- **At Rawafid.** The fee schedule can be published today. The attendance summary only after its small cells are suppressed and it is classified again. The sports-day page was published with dates of birth: Lab 1.3 showed what that cost.

#### [day2#which-instrument] Each instrument decides its own question

*Closing the day*

| Instrument | Decides |
| --- | --- |
| Data Classification Policy | The level of a data set, and who reviews it |
| Data Sharing Policy | Whether and on what conditions data goes to another entity |
| Open Data Policy | How Public data is released for anyone to reuse |
| Generative AI Guidelines | What may enter a generative AI tool, and what users are told |
| Personal Data Protection Law | Everything about personal data, whichever policy also applies |

#### [day2#check-licence] Can Rawafid tune Wafi on the dataset?

*Checkpoint*

**Question:** Dana finds a public instruction dataset under CC-BY-NC-4.0 and wants to tune Wafi's replies with it. Rawafid is a fee-charging private school group. What does the licence allow?

- A. Any use, since it is public on the hub
- B. Any use, with attribution
- C. No use in Rawafid's commercial service
- D. Use only after classifying it as Public

#### [day2#lab-2-4] Licences and provenance

Lab 2.4 · 25 min

Check the licences of two candidate open-weight models and one dataset and record the use restrictions.

[D2_4_check_licences_two.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D2_4_check_licences_two.ipynb)

- [ ] Read two model cards and one dataset card (5 min)
- [ ] Record licence, SPDX identifier and obligations (7 min)
- [ ] Decide fit for Wafi per artefact (5 min)
- [ ] Answer six questions with the instrument that decides (8 min)
- [ ] ✱ Stretch: Trace where the dataset's text came from and what that adds

#### [day2#wrap-up] The level decides where data may go; the purpose decides what goes

*Day 2 · Three things to keep*

- **Level first.** Classify by impact; the highest level of the parts wins; unclassified is Restricted.
- **Hosted is a choice.** Only Public data goes to a hosted model. Real records need a model you run.
- **Yes, on conditions.** Sharing and reuse are decided field by field and term by term, and written down.

#### [day2#next] Tomorrow: the ethics principles as tests, and the risk register

*Before Day 3*

- Read the seven AI Ethics Principles' one-paragraph definitions and the four risk levels (about 15 minutes).
- Skim the English summary of the National AI Risk Management Framework.
- Optional: set a free OpenRouter key so Day 3's forty enquiries also run on a hosted model.

## Day 3: Ethics and risk in practice

Turn the principles into tests, rate the risks and tell parents the truth

#### [day3#title] Ethics and risk in practice

*SDAIA Academy · Responsible Data and AI Practice in the Kingdom*

Day 3: Turn the principles into tests, rate the risks and tell parents the truth

Data & AI Foundations Track · 3 teaching days + capstone day · 4 sessions · 4 labs · FN-106

#### [day3#agenda] Ethics and risk in practice

*Today*

- **Session 1 · Principles into tests**: A principle becomes useful when it is a check with a threshold that passes or fails
- **Session 2 · Testing the assistant**: Paired enquiries in Arabic and English show whether the assistant serves both groups equally
- **Session 3 · Risk tier and risk register**: The ethics tier sets the bar; the national framework rates, treats and reviews each risk
- **Session 4 · Disclosure and human review**: Parents are told what the assistant is and does, and sensitive replies go to a person

#### [day3#review-day2] Where may Wafi's minimised prompt go?

*Review of Day 2*

**Question:** After Lab 1.2 Wafi's prompt carries a child's first name, three counts and the guardian's message. Under Rawafid's rule, where may that prompt go with real records?

- A. To the free hosted model, since it is minimised
- B. To a model served inside Rawafid only
- C. Nowhere: it describes a child
- D. To any hosted model whose terms forbid training on it

### Session 1: Principles into tests

#### [day3#s1] Principles into tests

*Session 1*

- Translate an ethics principle into a measurable check
- Set a threshold and a pass rule for each check
- Run checks over a recorded run and read the failures

#### [day3#seven-principles] Seven principles, and three of them can be tested today

*The AI Ethics Principles*

- **Fairness.** No bias, discrimination or stigma.
- **Privacy and security.** Days 1 and 2.
- **Humanity.** Human-centred, human oversight.
- **Social and environmental benefits.** Serve people and the planet.
- **Reliability and safety.** Works as specified, safely.
- **Transparency and explainability.** People know and understand.
- **Accountability and responsibility.** Someone answers for it.

#### [day3#principle-to-check] A principle becomes useful when it is a check that can fail

*From a word to a test*

1. **Principle** "fair to all guardians"
2. **Measure** correct replies per language
3. **Threshold** gap at most 10 points, set first
4. **Result** pass or fail, with the cases to read

> **The principle asks for this.** Fairness metrics are chosen early, with a threshold that defines fair and unfair, and monitored in production.

#### [day3#recorded-run] A recorded run: 24 replies from the pilot, with what each one did

*What the checks read*

| Field | Feeds |
| --- | --- |
| language, sensitive, a reviewer's quality mark, escalated | Fairness |
| AI disclosure line, human route, sent | Transparency |
| model, prompt version, reviewed by | Accountability |

If the log does not record a field, the principle that needs it cannot be checked.

#### [day3#three-results] All three checks fail on the pilot's own log

*Measured in Lab 3.1*

- **58% / 100%** replies marked correct, Arabic against English
- **2 of 24** replies sent without the AI notice
- **5** replies with no model, no reviewer or no escalation

The two sensitive replies that were never escalated are both Arabic.

#### [day3#tolerance] Rates across groups need a tolerance; duties to each person do not

*Thresholds*

- **Fairness: ten points.** Rates move by chance across small groups. The gap is judged against a threshold set in advance.
- **Transparency: zero.** Each guardian is owed the notice. One reply without it is one guardian misled.

> **What goes wrong.** A threshold written after the results are known is fitted to pass.

#### [day3#check-threshold] Dana wants to change the threshold

*Checkpoint*

**Question:** The fairness check fails with a gap of 42 points. Dana proposes raising the threshold to 45 so the release can go ahead. What is wrong with that?

- A. Nothing, if the new threshold is written down
- B. Thresholds must always be five points
- C. The check only matters after release
- D. A threshold set after the results is fitted to pass

#### [day3#lab-3-1] Three checks

Lab 3.1 · 25 min

Write three checks that turn fairness, transparency and accountability into pass or fail results.

[D3_1_write_three_checks.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D3_1_write_three_checks.ipynb)

- [ ] Turn fairness into a measurable check with a threshold (8 min)
- [ ] Turn transparency into a check on every reply (6 min)
- [ ] Turn accountability into a check on the log (6 min)
- [ ] Run all three on the recorded run (5 min)
- [ ] ✱ Stretch: Add a fourth check for privacy: no identifier in any reply

### Session 2: Testing the assistant

#### [day3#s2] Testing the assistant

*Session 2*

- Run a scripted test set through an assistant
- Compare reply quality and escalation rates per language
- Name the bias types that explain a measured gap

#### [day3#paired-test] Ask the same thing twice, once in each language

*How to test for a language gap*

- Twenty enquiries guardians send, each in English and in Arabic.
- Arabic in the forms guardians write: Modern Standard and Gulf.
- Twelve routine questions with a known answer; eight sensitive ones that must reach a person.
- Same guardian, same child, same question: the only difference is the language.

- **Example pair.** "Can you tell me Yousef's absences so far?" كم مرة غاب يوسف لين الحين؟

#### [day3#standin-and-hosted] A scripted stand-in gives everyone the same numbers

*The model behind the test*

- **Stand-in (default).** Fixed templates filled from the prompt. It reads Modern Standard Arabic phrasings and misses Gulf ones, on purpose, so the method can be learned on a known gap.
- **Free hosted model (optional).** With a key, a real model drafts the replies. Results vary by model and day; synthetic data only.

> **Say it plainly.** The stand-in is not evidence about any real model. The method is what transfers.

#### [day3#forty-results] English is served fully; Gulf Arabic is served least

*Measured in Lab 3.2*

| Variety | Routine replies correct | Sensitive enquiries escalated |
| --- | --- | --- |
| English | 12 of 12 | 8 of 8 |
| Modern Standard Arabic | 6 of 6 | 2 of 4 |
| Gulf Arabic | 2 of 6 | 0 of 4 |

#### [day3#two-failures] A weak reply is visible; a missed escalation reaches nobody

*Which gap matters more*

- **Routine reply wrong.** The guardian sees a generic answer and asks again or calls. Annoying, recoverable.
- **Sensitive enquiry not escalated.** "Rahaf was unwell at school yesterday" gets a template reply and no person reads it. The school never knew.

#### [day3#bias-types] Three bias types explain what the test measured

*The AI Bias Reference Guide*

| Bias type | The guide's sense | At Rawafid |
| --- | --- | --- |
| **Language** | Trained on standard language, fails on dialect | Gulf phrasings fail where MSA succeeds |
| **Evaluation** | Tests do not reflect the real users | The pilot was tested in English only |
| **Automation** | People trust the system's output over their judgement | Staff read only what the router flags |

#### [day3#check-bias-type] Which bias type does the pilot's test show?

*Checkpoint*

**Question:** Dana's pilot report said Wafi answered 100% of test enquiries correctly. Every test enquiry was in English. Which bias type from the national guide does the report show?

- A. Automation bias
- B. Evaluation bias
- C. Measurement bias
- D. Language bias

#### [day3#lab-3-2] Forty enquiries

Lab 3.2 · 25 min

Run forty scripted enquiries in Arabic and English, compare reply quality and escalation rates, and name the bias types from the national guide that explain any gap.

[D3_2_run_forty_scripted.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D3_2_run_forty_scripted.ipynb)

- [ ] Run the forty enquiries through Wafi (6 min)
- [ ] Score reply quality per language (6 min)
- [ ] Compare escalation rates per language (5 min)
- [ ] Name the bias types that explain the gaps (5 min)
- [ ] Write the test report rows (3 min)
- [ ] ✱ Stretch: Rerun with the Arabic keywords added and measure the change

### Session 3: Risk tier and risk register

#### [day3#s3] Risk tier and risk register

*Session 3*

- Place an AI system in an ethics risk tier with reasons
- Rate harms by likelihood and impact and compute the risk level
- Write a register entry with treatment, owner and review date

#### [day3#four-risk-levels] Four risk levels set how much is required before use

*The AI Ethics Principles*

| Level | What follows |
| --- | --- |
| Little or no risk | No restrictions; ethical compliance recommended |
| Limited risk | The AI ethics principles apply |
| High risk | Conformity assessments before and after deployment, and the statutory requirements |
| Unacceptable risk | Not allowed; examples include exploitation of children |

#### [day3#wafi-tier] Limited risk, on one condition

*Placing Wafi*

- Wafi answers factual questions; it decides nothing about a child.
- Health, safety, custody, complaints and disputed fees are meant to reach a person first.
- So the principles apply, and Wafi is tested against them.

- **The condition.** If sensitive replies went out without review, or Wafi began to decide anything about a child, it would be high risk. Lab 3.2 showed the routing does not yet hold in Arabic.

#### [day3#framework-phases] Set the context, then four phases that repeat

*The National AI Risk Management Framework*

1. **Context and scope** the system, its users, the rules
2. **Identify** what could go wrong
3. **Assess** likelihood × impact
4. **Treat** avoid, mitigate, transfer, accept
5. **Monitor and review** re-rate, report

It rests on four pillars: general principles, AI regulations, data regulations and sector regulations.

#### [day3#likelihood-impact] Two four-point scales, multiplied, give four bands

*Assess*

|  | Likelihood | Impact |
| --- | --- | --- |
| 1 | Rare | Low |
| 2 | Unlikely | Medium |
| 3 | Likely | High |
| 4 | Almost certain | Catastrophic |

| Level | Band |
| --- | --- |
| 1 to 2 | Low |
| 3 to 6 | Medium |
| 8 to 12 | High |
| 16 | Catastrophic |

#### [day3#register-results] Three of five harms rate high before treatment

*Measured in Lab 3.3*

| Harm | L × I | Band | Owner | After |
| --- | --- | --- | --- | --- |
| H1 wrong family's data | 2 × 3 = 6 | medium | Dana Al-Saleh | 3 medium |
| H2 log leaks | 2 × 4 = 8 | high | Nasser Al-Mansour | 4 medium |
| H3 Gulf Arabic served less | 4 × 2 = 8 | high | Layla Haddad | 4 medium |
| H4 wrong number stated | 3 × 2 = 6 | medium | Osama Al-Qurashi | 2 low |
| H5 drafts approved unread | 3 × 3 = 9 | high | Dr. Amal Al-Sayari | 6 medium |

#### [day3#residual] Treatment lowers likelihood more easily than impact

*Treat, then rate again*

- **H2 after treatment: 1 × 4.** Minimised prompts and deletion after 90 days make a leak less likely and smaller. A leak of children's records is still catastrophic.
- **Still high after treatment?** Treat it further, or have someone with the authority accept it with a recorded reason, and escalate.

#### [day3#check-rating] Rate the new harm

*Checkpoint*

**Question:** Nasser adds a harm: an export of the full log, with health notes of 434 children, is shared outside Rawafid. He rates it unlikely (2) and catastrophic (4). What is its level and band?

- A. 6, medium
- B. Catastrophic, because the impact is catastrophic
- C. 8, high
- D. 4, medium

#### [day3#lab-3-3] Tier and register

Lab 3.3 · 25 min

Place the assistant in a risk tier and rate five harms by likelihood and impact.

[D3_3_place_assistant_risk.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D3_3_place_assistant_risk.ipynb)

- [ ] Place Wafi in an ethics risk tier with reasons (5 min)
- [ ] Rate five harms by likelihood and impact (8 min)
- [ ] Compute levels and bands (3 min)
- [ ] Choose a treatment, owner and review date per harm (6 min)
- [ ] Rate the residual risk again (3 min)
- [ ] ✱ Stretch: Change one fact (replies sent without review) and redo the tier

### Session 4: Disclosure and human review

#### [day3#s4] Disclosure and human review

*Session 4*

- Draft a disclosure that names the assistant, the data and the human route
- Write a rule that sends sensitive replies to staff
- Test the rule for recall in both languages

#### [day3#notice-sources] Three sources decide what the notice says

*What parents must be told*

- **PDPL Article 13.** Purpose and basis, how data is collected, who is responsible and how to reach them, recipients, rights.
- **Generative AI Guidelines.** Say when content is made with generative AI; offer a channel that does not go through it.
- **AI Ethics Principles.** Transparency, and humanity: a person reviews what matters.

#### [day3#genai-two-guidelines] Two documents: one for government staff, one for everyone who builds or uses

*The Generative AI Guidelines*

- **For government.** Public data only in generative AI tools. Tell beneficiaries when content is made with generative AI, offer a channel that is not automated, and proofread outputs for accuracy.
- **For the public.** Addressed to developers and users. Follow the Personal Data Protection Law, assess the tool on the four risk levels, label generated content, and verify outputs before relying on them.

> **For Wafi.** Rawafid builds and uses a generative AI service, so the public guidelines speak to it directly; it adopts the government ones as its house rule.

#### [day3#notice-draft] 131 words that answer nine questions

*The reference notice, shortened*

- "Wafi is Rawafid Schools Group's assistant. It uses generative AI to draft replies to your questions about your child's attendance, lateness and fees. To answer, it reads your child's first name and this term's counts from our records; nothing else is sent. Questions about health, safety, custody, complaints or a disputed fee always go to a member of staff, who replies to you. [...] You may ask a person at any time [...]"

The full text adds the basis, the 90-day retention, no sharing outside Rawafid, the rights and the data protection officer's contact.

#### [day3#routing-rule] The routing rule needs the words guardians actually write

*Human review that works in both languages*

- English, Modern Standard Arabic and Gulf Arabic forms for health, harm, disputes, complaints and custody.
- Leave out words routine questions use: "fee" and "رسوم" would send every balance question to staff.
- Measure recall per language, and false alarms.

- **Gulf forms that Dana's list missed.** تعبان · يضايقون · خصمتوا · صك حضانة

#### [day3#human-review] A review counts only if the reviewer can disagree with the draft

*Human review*

- **Sees the facts.** The reviewer reads the guardian's message and the record beside the draft, not the draft alone.
- **Is named.** Each escalated reply records who approved it. Lab 3.1's accountability check reads that field.
- **Has the time.** A queue cleared in seconds per reply is approval, not review. That is harm H5.

> **What goes wrong.** The draft reads well, so it is approved unread: automation bias, with a person's name on it.

#### [day3#recall-results] The new rule reaches a person for every sensitive enquiry

*Measured in Lab 3.4*

| Rule | English recall | Arabic recall | False alarms |
| --- | --- | --- | --- |
| Dana's router | 8 of 8 | 2 of 8 | 0 of 24 |
| The reference rule | 8 of 8 | 8 of 8 | 0 of 24 |

> **Read it carefully.** A list that catches all forty has learned these forty. Grow the test set from the messages staff re-route by hand.

#### [day3#check-notice] Which notice meets the guidelines?

*Checkpoint*

**Question:** Layla must choose one line for the foot of every Wafi reply. Which one meets the Generative AI Guidelines' transparency items?

- A. "Sent by Wafi, Rawafid's digital service."
- B. "This reply may contain errors."
- C. "Drafted with AI. Write 'staff' to reach a person."
- D. "See our privacy policy for details."

#### [day3#lab-3-4] Notice and routing rule

Lab 3.4 · 25 min

Draft the notice parents see and the rule that sends sensitive replies to staff.

[D3_4_draft_notice_parents.ipynb](https://sdaiaacademy.github.io/fn-106/labs/D3_4_draft_notice_parents.ipynb)

- [ ] Draft the notice parents see (7 min)
- [ ] Check it against the required items (4 min)
- [ ] Write the routing rule for sensitive replies (6 min)
- [ ] Test the rule on the forty enquiries per language (5 min)
- [ ] Choose your capstone build (3 min)
- [ ] ✱ Stretch: Write the Arabic notice and check both say the same

#### [day3#wrap-up] Test it, rate it, tell people the truth about it

*Day 3 · Three things to keep*

- **Checks with thresholds.** Set before the run; read the failing cases, not only the verdict.
- **A register with owners.** Likelihood × impact, a treatment, a person, a date, and a second rating.
- **A notice and a person.** Say it is AI, what it reads, and how to reach a human, in both languages.

#### [day3#next] Tomorrow: the responsible build pack, reviewed live

*Before the capstone*

- Put the registers, the minimisation code and its re-identification test, the test report, the record of processing, the breach checklist and the notice in one public repository.
- A README that links each part.
- Six minutes to present; four for the assessor's changed fact.

## Capstone: Capstone: the responsible build pack

Ten-minute reviews: six minutes to present the pack, four for the assessor's changed fact

#### [capstone#title] Capstone: the responsible build pack

*SDAIA Academy · Responsible Data and AI Practice in the Kingdom*

Capstone: Ten-minute reviews: six minutes to present the pack, four for the assessor's changed fact

Data & AI Foundations Track · 3 teaching days + capstone day · 6 min talk and demo · 4 min Q&A · FN-106

#### [capstone#agenda] How the presentations run

*Capstone*

- **Expectations and final prep**: the rubric, a last rehearsal, then the first presentations
- **Presentations**: each one timed, with questions after it
- **Review and closing**: peer feedback, the trainer's review, what next

#### [capstone#rubric] The rubric

*How presentations are scored*

| Item | Value |
| --- | --- |
| Data protection | 25% |
| Classification and sharing | 20% |
| Risk assessment | 20% |
| Ethics tests | 20% |
| Disclosure and records | 15% |

> **Show measured results.** A re-identification rate, a fairness gap, a recall per language: a claim without a number is a plan.

#### [capstone#format] Ten minutes each: six to present, four for a changed fact

*Format*

- **1 · The build.** Whose data, what it does, where prompts go. One slide or the README.
- **2 · The pack.** Walk the repository: registers, code, test report, records, notice. Show the numbers.
- **3 · The changed fact.** The assessor changes one fact; you revise the classification and risk entries live.

> **Peer feedback.** After each review, everyone writes one strength, one question and one risk they would add.

#### [capstone#running-order] Who presents when

*Running order*

| # | Presenter | Build |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |
| 8 |  |  |

#### [capstone#final-prep] Final prep · 20 minutes

*Before the first presentation*

Check your repository is public and holds no real data or keys, rehearse once, open the README on this screen.

#### [capstone#now-presenting] The pack

*Now presenting*

##### The changed fact

#### [capstone#review] What the presentations showed

*Trainer review*

- **Strongest patterns.** What several projects got right.
- **Common gaps.** What most projects would fix next.
- **One surprise.** Something nobody expected.

#### [capstone#what-next] Keep going

*After the course*

- **The follow-up task:** apply the build pack to a second case, ideally a build from your own work, and submit it as tracked
- **Keep the instruments current:** recheck licences, guidelines and the risk framework before each real release
- **Your pack stays yours:** it is the template for the next build you make lawful

#### [capstone#thanks] Thank you

*SDAIA Academy*

Responsible Data and AI Practice in the Kingdom
