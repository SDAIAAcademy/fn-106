<!-- academy:title -->
# Responsible Data and AI Practice in the Kingdom

الممارسة المسؤولة للبيانات والذكاء الاصطناعي في المملكة

Data & AI Foundations Track · SDAIA Academy · FN-106 · Level 100

REPLACE: one line under the title: what participants can do after the course

Participants make one small build lawful and responsible: a parent-enquiry assistant for a fictional private school group that drafts replies from attendance and fee records with a language model. They map its personal data and minimise it under the Personal Data Protection Law (PDPL), classify each data set under the National Data Management Office (NDMO) policy, decide what may reach an external model, turn the SDAIA AI Ethics Principles into tests, assess risk with the National AI Risk Management Framework, and write the disclosure and records the build needs.

**Format:** Intensive: 3 teaching days of four sessions and a capstone day, with guided pre-work and a tracked follow-up task

**Course page:** https://sdaiaacademy.github.io/fn-106/
<!-- /academy:title -->

## Outcomes

| | Outcomes | Level | Evidence |
|---|---|---|---|
| LO1 | Explain the PDPL obligations that govern a build, from lawful basis and minimisation to rights, retention, transfer and breach handling, given the assistant's data flow diagram | Awareness | an annotated diagram naming the obligation at each step, checked against the reference |
| LO2 | Distinguish what the data classification, data sharing and open data policies and the SDAIA Generative AI Guidelines each decide, given six questions about the build | Awareness | a decision table naming the governing instrument, matching the reference on at least five of six |
| LO3 | Classify each data set of the build under the four NDMO classification levels and derive the rule for sending it to an external model service, given the school group's data inventory and the policy's impact categories | Applied | a classification register with level, reason and permitted destinations per data set |
| LO4 | Apply minimisation and pseudonymisation to the data the assistant sends, and test whether records can be re-identified, given synthetic student and guardian records | Applied | a before-and-after field list, a pseudonymisation script and a re-identification test result |
| LO5 | Prepare a risk assessment that places the assistant in an ethics risk tier and works through the four phases of the national risk framework, given the build description and five candidate harms | Applied | a risk register with tier, likelihood and impact ratings, an owner, a treatment and a review date per risk |
| LO6 | Test the assistant against the ethics principles for fairness across Arabic and English enquiries, transparency and human review, and draft the disclosure parents see, given forty scripted enquiries | Applied | a test report with results per check, the changes made and the disclosure text |

<!-- academy:units -->
## Units

| Unit | Title | Sessions | Slides |
|---|---|---|---|
| Day 1 | Personal data and the law | Where personal data flows in a build; Lawful basis and minimisation; Pseudonymisation and its limits; Rights, retention and breaches | [`slides/day1.html`](slides/day1.html) |
| Day 2 | Classify, share and send | Data classification levels; What may reach an external model; Sharing with another entity; Licences and provenance | [`slides/day2.html`](slides/day2.html) |
| Day 3 | Ethics and risk in practice | Principles into tests; Testing the assistant; Risk tier and risk register; Disclosure and human review | [`slides/day3.html`](slides/day3.html) |
| Capstone | Capstone project presentations |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**REPLACE: the name of the fictional organisation every lab works on.** REPLACE: two sentences on the case study and its synthetic data

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Map every field the assistant reads, sends, logs and stores on a data flow diagram | [`D1_1_map_every_field.ipynb`](labs/D1_1_map_every_field.ipynb) |
| 1.2 | Day 1 · Session 2 | Set a lawful basis and purpose for each flow and remove the fields the purpose does not need | [`D1_2_set_lawful_basis.ipynb`](labs/D1_2_set_lawful_basis.ipynb) |
| 1.3 | Day 1 · Session 3 | Pseudonymise the guardian and student records and attempt to re-identify them by linkage | [`D1_3_pseudonymise_guardian_student.ipynb`](labs/D1_3_pseudonymise_guardian_student.ipynb) |
| 1.4 | Day 1 · Session 4 | Write a retention rule per store and walk a seeded breach through the PDPL breach guideline | [`D1_4_write_retention_rule.ipynb`](labs/D1_4_write_retention_rule.ipynb) |
| 2.1 | Day 2 · Session 1 | Classify the six data sets with the policy's impact categories and record the reasons | [`D2_1_classify_six_data.ipynb`](labs/D2_1_classify_six_data.ipynb) |
| 2.2 | Day 2 · Session 2 | Decide for each data set whether it may go to a hosted model, a locally served model or neither | [`D2_2_decide_each_data.ipynb`](labs/D2_2_decide_each_data.ipynb) |
| 2.3 | Day 2 · Session 3 | Assess a partner entity's request for attendance data against the Data Sharing Policy and draft the conditions | [`D2_3_assess_partner_entity.ipynb`](labs/D2_3_assess_partner_entity.ipynb) |
| 2.4 | Day 2 · Session 4 | Check the licences of two candidate open-weight models and one dataset and record the use restrictions | [`D2_4_check_licences_two.ipynb`](labs/D2_4_check_licences_two.ipynb) |
| 3.1 | Day 3 · Session 1 | Write three checks that turn fairness, transparency and accountability into pass or fail results | [`D3_1_write_three_checks.ipynb`](labs/D3_1_write_three_checks.ipynb) |
| 3.2 | Day 3 · Session 2 | Run forty scripted enquiries in Arabic and English, compare reply quality and escalation rates, and name the bias types from the national guide that explain any gap | [`D3_2_run_forty_scripted.ipynb`](labs/D3_2_run_forty_scripted.ipynb) |
| 3.3 | Day 3 · Session 3 | Place the assistant in a risk tier and rate five harms by likelihood and impact | [`D3_3_place_assistant_risk.ipynb`](labs/D3_3_place_assistant_risk.ipynb) |
| 3.4 | Day 3 · Session 4 | Draft the notice parents see and the rule that sends sensitive replies to staff | [`D3_4_draft_notice_parents.ipynb`](labs/D3_4_draft_notice_parents.ipynb) |
<!-- /academy:labs -->

## Capstone

A responsible build pack for the assistant or the participant's own build (registers, minimisation code with its re-identification test, ethics test report, a record of processing entry, a breach checklist and the disclosure), submitted as a public repository and defended in a ten-minute review

**Submission:** REPLACE: what participants submit and how: a public repository link, or a shared folder for a course without code

## Prerequisites

- FN-101 Python for Data and AI Work
- FN-105 How Machine Learning and Language Models Work
- Reads a short Python program that calls a web API

<!-- academy:tools -->
## Tools

Each line is a capability; the examples are interchangeable.

- **Language model for the build:** a small open-weight model served locally, a free hosted endpoint used only with synthetic data
- **Personal data detection:** Presidio, regular-expression rules
- **De-identification and linkage testing:** ARX, dataframe joins on quasi-identifiers
- **Licence references:** the SPDX licence list, model and dataset cards
- **Diagramming:** draw.io, Mermaid
<!-- /academy:tools -->

<!-- academy:sources -->
## Sources

- REPLACE: every source the course cites, with its address, in course.json under "sources"; this list is written from there
<!-- /academy:sources -->

### National references

- Personal Data Protection Law and its implementing regulations: REPLACE: the address of the official text
- Regulation on Personal Data Transfer outside the Kingdom: REPLACE: the address of the official text
- PDPL guidelines on minimum data, records of processing, pseudonymisation and breach procedure: REPLACE: the address of the official text
- NDMO Data Classification Policy: REPLACE: the address of the official text
- NDMO Data Sharing Policy: REPLACE: the address of the official text
- NDMO Open Data Policy: REPLACE: the address of the official text
- SDAIA AI Ethics Principles: REPLACE: the address of the official text
- SDAIA Generative AI Guidelines: REPLACE: the address of the official text
- National AI Risk Management Framework: REPLACE: the address of the official text
- SDAIA AI Bias Reference Guide: REPLACE: the address of the official text
