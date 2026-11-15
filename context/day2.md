---
course: "Responsible Data and AI Practice in the Kingdom"
code: "FN-106"
version: "2027.1.0"
deck: "day2"
day: 2
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fn-106/slides/day2.html"
---

# Responsible Data and AI Practice in the Kingdom

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
