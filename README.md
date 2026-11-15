<!-- academy:title -->
# Responsible Data and AI Practice in the Kingdom

الممارسة المسؤولة للبيانات والذكاء الاصطناعي في المملكة

Data & AI Foundations Track · SDAIA Academy · FN-106 · Level 100

Make one AI build lawful and responsible: map and minimise its personal data, classify and share it under the national policies, test it against the ethics principles and write its risk register and disclosure

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
| Capstone | Capstone: the responsible build pack |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**Rawafid Schools Group** is a fictional private school group with four campuses (Riyadh North, Riyadh East, Jeddah, Dammam) and about 1,200 students. Its systems lead built **Wafi** (وافي), an assistant that drafts replies to parents from attendance and fee records with a language model; its data protection officer must now make the build lawful and responsible.

All records are synthetic, written by `labs/prepare_data.py` with a fixed seed: 860 guardians, 1,200 students, a term of attendance events, fees, Wafi's enquiry log, a public sports-day results page, a partner's data request, licence facts for two models and one dataset, forty scripted enquiries in Arabic and English and five candidate harms. Identification numbers, mobile numbers and bank account numbers have the right shape and belong to nobody. The data is planted with the problems the labs find.

People: Dr. Amal Al-Sayari (group director of schools), Nasser Al-Mansour (data protection officer), Layla Haddad (head of parent relations), Osama Al-Qurashi (fees manager), Dana Al-Saleh (systems lead).

## How the course runs

Three teaching days of four sessions. Each session has about 20 minutes of ideas, a checkpoint, and a 25-minute lab notebook that starts from supplied files, so no lab depends on another. Guided pre-work (a reading guide to the core instruments, ending in an entry quiz: `labs/PREWORK.md`) comes before Day 1; a follow-up task applies the build pack to a second case after the course.

Labs run on a laptop processor or in Google Colab. Wafi drafts its replies with a scripted stand-in model that needs no key; with a free OpenRouter key it uses a free hosted model instead. Only synthetic data is ever sent to a hosted model.

**AI policy.** AI off for the supervised scenario check and for the first classification of each data set. An assistant may tutor you through the instruments, and every answer is checked against the official text. Anything goes for drafting the build pack, provided no real personal data enters any assistant.

## Assessment

- A supervised scenario check on the national instruments, without AI (30%).
- The capstone build pack, on the five-criterion rubric below (50%).
- A ten-minute review in which the assessor changes one fact of the case (20%).

Passing needs 70% overall and at least 60% on the scenario check. The certificate is a completion certificate with assessed work. The practice questions in `assessments/bank.json` rehearse the scenario check; the check's own items are not in this repository.

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Day 1 · Session 1 | Trace Wafi's personal data | [`D1_1_map_every_field.ipynb`](labs/D1_1_map_every_field.ipynb) |
| 1.2 | Day 1 · Session 2 | Lawful basis and minimum fields | [`D1_2_set_lawful_basis.ipynb`](labs/D1_2_set_lawful_basis.ipynb) |
| 1.3 | Day 1 · Session 3 | Pseudonymise, then attack | [`D1_3_pseudonymise_guardian_student.ipynb`](labs/D1_3_pseudonymise_guardian_student.ipynb) |
| 1.4 | Day 1 · Session 4 | Retention and a seeded breach | [`D1_4_write_retention_rule.ipynb`](labs/D1_4_write_retention_rule.ipynb) |
| 2.1 | Day 2 · Session 1 | Classify six data sets | [`D2_1_classify_six_data.ipynb`](labs/D2_1_classify_six_data.ipynb) |
| 2.2 | Day 2 · Session 2 | Hosted, local or neither | [`D2_2_decide_each_data.ipynb`](labs/D2_2_decide_each_data.ipynb) |
| 2.3 | Day 2 · Session 3 | A partner's data request | [`D2_3_assess_partner_entity.ipynb`](labs/D2_3_assess_partner_entity.ipynb) |
| 2.4 | Day 2 · Session 4 | Licences and provenance | [`D2_4_check_licences_two.ipynb`](labs/D2_4_check_licences_two.ipynb) |
| 3.1 | Day 3 · Session 1 | Three checks | [`D3_1_write_three_checks.ipynb`](labs/D3_1_write_three_checks.ipynb) |
| 3.2 | Day 3 · Session 2 | Forty enquiries | [`D3_2_run_forty_scripted.ipynb`](labs/D3_2_run_forty_scripted.ipynb) |
| 3.3 | Day 3 · Session 3 | Tier and register | [`D3_3_place_assistant_risk.ipynb`](labs/D3_3_place_assistant_risk.ipynb) |
| 3.4 | Day 3 · Session 4 | Notice and routing rule | [`D3_4_draft_notice_parents.ipynb`](labs/D3_4_draft_notice_parents.ipynb) |
<!-- /academy:labs -->

## Capstone

A responsible build pack for the assistant or the participant's own build (registers, minimisation code with its re-identification test, ethics test report, a record of processing entry, a breach checklist and the disclosure), submitted as a public repository and defended in a ten-minute review

**Submission:** a public GitHub repository holding the build pack, with a README that links each part. The review: six minutes to walk through the pack, then four in which the assessor changes one fact (a new data field, a transfer abroad) and you revise the classification and risk entries live. The commit history is inspected.

| Criterion | Weight |
|---|---|
| Data protection | 25 |
| Classification and sharing | 20 |
| Risk assessment | 20 |
| Ethics tests | 20 |
| Disclosure and records | 15 |

## Prerequisites

- FN-101 Python for Data and AI Work
- FN-105 How Machine Learning and Language Models Work
- Reads a short Python program that calls a web API

<!-- academy:tools -->
## Tools

Each line is a capability; the examples are interchangeable.

- **Language model for the build:** a free hosted endpoint used only with synthetic data (an OpenRouter free model), a scripted stand-in model that runs without a key, a small open-weight model served locally, for real data (not used in the labs)
- **Personal data detection:** regular-expression rules, Presidio
- **De-identification and linkage testing:** dataframe joins on quasi-identifiers (pandas), ARX
- **Licence references:** the SPDX licence list, model and dataset cards
- **Diagramming:** Mermaid, draw.io
<!-- /academy:tools -->

<!-- academy:sources -->
## Sources

### National references: personal data

- [Personal Data Protection Law (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf)
- [Implementing Regulation of the Personal Data Protection Law (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf)
- [Regulation on Personal Data Transfer outside the Kingdom, version 2.0 (SDAIA)](https://sdaia.gov.sa/Documents/RegulationonPersonalDataEN.pdf)
- [Minimum Personal Data Guideline (SDAIA)](https://sdaia.gov.sa/Documents/MinmumPDGuideline.pdf)
- [Personal Data Processing Activities Records Guideline (SDAIA)](https://sdaia.gov.sa/Documents/PersonalDataProcessingActivitiesRecordsGuideline.pdf)
- [Personal Data Destruction, Anonymization and Pseudonymisation Guideline (SDAIA)](https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf)
- [Personal Data Breach Incidents Procedural Guide (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataBreachIncidents.pdf)

### National references: data management (NDMO)

- [Data Classification Policy (NDMO, SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf)
- [Data Sharing Policy (NDMO, SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/DataSharingPolicyEN.pdf)
- [Open Data Policy (NDMO, SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/OpenDataPolicy.pdf)

### National references: AI ethics, generative AI and risk

- [AI Ethics Principles (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf)
- [Generative AI Guidelines for Government (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf)
- [Generative AI Guidelines for the Public (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Files/GenerativeAIPublicEN.pdf)
- [National AI Risk Management Framework, full text in Arabic (SDAIA, April 2026)](https://sdaia.gov.sa/ar/MediaCenter/KnowledgeCenter/ResearchLibrary/ExecutiveSummaryAr.pdf)
- [National AI Risk Management Framework, English executive summary (SDAIA, April 2026)](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/ExecutiveSummaryEn.pdf)
- [AI Bias Reference Guide, first edition (SDAIA, May 2026)](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/EN-AI-BIAS.pdf)
- [Regulations and policies index (SDAIA)](https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx)

### Licences, cards and tools

- [SPDX License List](https://spdx.org/licenses/)
- [Qwen3-4B model card and licence (Hugging Face)](https://huggingface.co/Qwen/Qwen3-4B)
- [Gemma Terms of Use (Google)](https://ai.google.dev/gemma/terms)
- [Gemma 3 4B instruction-tuned model card (Hugging Face)](https://huggingface.co/google/gemma-3-4b-it)
- [Alpaca dataset card (Hugging Face)](https://huggingface.co/datasets/tatsu-lab/alpaca)
- [OpenRouter models list](https://openrouter.ai/models)
- [Presidio, personal data detection and anonymisation framework](https://presidio.dataprivacystack.org/)
- [ARX Data Anonymization Tool](https://arx.deidentifier.org/)
- [Mermaid flowchart syntax](https://mermaid.js.org/syntax/flowchart.html)
<!-- /academy:sources -->

### National references

All were opened on 2026-11-15 from SDAIA's regulations and policies page and its research library. The NDMO policies are written for government entities; Rawafid, a private group, adopts them in its own data policy, while the PDPL binds it by law.


- Personal Data Protection Law: https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf, and its Implementing Regulation: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf
- Regulation on Personal Data Transfer outside the Kingdom: https://sdaia.gov.sa/Documents/RegulationonPersonalDataEN.pdf
- PDPL guidelines: minimum personal data https://sdaia.gov.sa/Documents/MinmumPDGuideline.pdf; records of processing activities https://sdaia.gov.sa/Documents/PersonalDataProcessingActivitiesRecordsGuideline.pdf; destruction, anonymisation and pseudonymisation https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf; breach incidents https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataBreachIncidents.pdf
- NDMO Data Classification Policy: https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf
- NDMO Data Sharing Policy: https://sdaia.gov.sa/en/SDAIA/about/Documents/DataSharingPolicyEN.pdf
- NDMO Open Data Policy: https://sdaia.gov.sa/en/SDAIA/about/Documents/OpenDataPolicy.pdf
- SDAIA AI Ethics Principles: https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf
- SDAIA Generative AI Guidelines: for government https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf; for the public https://sdaia.gov.sa/en/SDAIA/about/Files/GenerativeAIPublicEN.pdf
- National AI Risk Management Framework (April 2026): the full text, in Arabic, https://sdaia.gov.sa/ar/MediaCenter/KnowledgeCenter/ResearchLibrary/ExecutiveSummaryAr.pdf; the English executive summary https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/ExecutiveSummaryEn.pdf
- SDAIA AI Bias Reference Guide (first edition, May 2026): https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/EN-AI-BIAS.pdf
