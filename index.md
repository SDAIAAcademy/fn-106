---
course: "Responsible Data and AI Practice in the Kingdom"
code: "FN-106"
version: "2027.1.0"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fn-106/index.html"
---

# Responsible Data and AI Practice in the Kingdom

الممارسة المسؤولة للبيانات والذكاء الاصطناعي في المملكة

Data & AI Foundations Track · 3 teaching days + capstone day · 21 hours · Level 100

Make one AI build lawful and responsible: map and minimise its personal data, classify and share it under the national policies, test it against the ethics principles and write its risk register and disclosure

Participants make one small build lawful and responsible: a parent-enquiry assistant for a fictional private school group that drafts replies from attendance and fee records with a language model. They map its personal data and minimise it under the Personal Data Protection Law (PDPL), classify each data set under the National Data Management Office (NDMO) policy, decide what may reach an external model, turn the SDAIA AI Ethics Principles into tests, assess risk with the National AI Risk Management Framework, and write the disclosure and records the build needs.

**Who it is for:** Beginners. Graduates and career changers entering the AI Engineering or Data Science track; computing and data graduates who pass the placement test skip the courses it covers.

**Format:** Intensive: 3 teaching days of four sessions and a capstone day, with guided pre-work and a tracked follow-up task

## The case study

**Rawafid Schools Group.** Rawafid Schools Group is a fictional private school group with four campuses and about 1,200 students. Its systems lead built Wafi, an assistant that drafts replies to parents from attendance and fee records with a language model, and its data protection officer must now make that build lawful and responsible. Every record is synthetic, generated with a fixed seed, and planted with the problems the labs find: a prompt that carries the whole student file, a log kept too long, linkable quasi-identifiers, a partner asking for too much, a non-commercial dataset and a routing rule that only knows English.

## The course

### Day 1: Personal data and the law

Slides: https://sdaiaacademy.github.io/fn-106/slides/day1.md

- **Session 1: Where personal data flows in a build**
  - Identify the personal and sensitive data a build reads, sends, logs and stores
  - Draw a data flow diagram of an AI assistant with every store and external party
  - Name the PDPL obligation that applies at each step of the flow
  - [Lab 1.1: Trace Wafi's personal data (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D1_1_map_every_field.ipynb)
- **Session 2: Lawful basis and minimisation**
  - Choose a legal basis and a purpose for each flow of a build
  - Test each field against the purpose and remove what it does not need
  - Rewrite a prompt builder so it sends the minimum
  - [Lab 1.2: Lawful basis and minimum fields (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D1_2_set_lawful_basis.ipynb)
- **Session 3: Pseudonymisation and its limits**
  - Pseudonymise identifiers with a keyed hash and keep the key apart
  - Attempt re-identification by joining on quasi-identifiers
  - Generalise quasi-identifiers and measure the remaining risk
  - [Lab 1.3: Pseudonymise, then attack (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D1_3_pseudonymise_guardian_student.ipynb)
- **Session 4: Rights, retention and breaches**
  - Explain the data subject's rights and who exercises them for a minor
  - Write a retention rule per store and find what is kept too long
  - Walk a breach through notice, containment and documentation
  - [Lab 1.4: Retention and a seeded breach (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D1_4_write_retention_rule.ipynb)

### Day 2: Classify, share and send

Slides: https://sdaiaacademy.github.io/fn-106/slides/day2.md

- **Session 1: Data classification levels**
  - Assess the impact category and level of a data set's disclosure
  - Assign a classification level with an evidence-based reason
  - Spot aggregates that still reveal individuals
  - [Lab 2.1: Classify six data sets (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D2_1_classify_six_data.ipynb)
- **Session 2: What may reach an external model**
  - Derive a destination rule from the classification level and the data's nature
  - Apply the rule to data sets and to the fields of a prompt
  - Recognise a hosted endpoint abroad as a transfer outside the Kingdom
  - [Lab 2.2: Hosted, local or neither (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D2_2_decide_each_data.ipynb)
- **Session 3: Sharing with another entity**
  - Assess a data request against the Data Sharing Policy principles
  - Cut a request down to the minimum data its purpose needs
  - Draft the conditions under which data may be shared
  - [Lab 2.3: A partner's data request (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D2_3_assess_partner_entity.ipynb)
- **Session 4: Licences and provenance**
  - Read the licence of a model and of a dataset from its card
  - Record use restrictions and obligations in a licence register
  - Name the national instrument that decides a given question
  - [Lab 2.4: Licences and provenance (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D2_4_check_licences_two.ipynb)

### Day 3: Ethics and risk in practice

Slides: https://sdaiaacademy.github.io/fn-106/slides/day3.md

- **Session 1: Principles into tests**
  - Translate an ethics principle into a measurable check
  - Set a threshold and a pass rule for each check
  - Run checks over a recorded run and read the failures
  - [Lab 3.1: Three checks (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D3_1_write_three_checks.ipynb)
- **Session 2: Testing the assistant**
  - Run a scripted test set through an assistant
  - Compare reply quality and escalation rates per language
  - Name the bias types that explain a measured gap
  - [Lab 3.2: Forty enquiries (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D3_2_run_forty_scripted.ipynb)
- **Session 3: Risk tier and risk register**
  - Place an AI system in an ethics risk tier with reasons
  - Rate harms by likelihood and impact and compute the risk level
  - Write a register entry with treatment, owner and review date
  - [Lab 3.3: Tier and register (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D3_3_place_assistant_risk.ipynb)
- **Session 4: Disclosure and human review**
  - Draft a disclosure that names the assistant, the data and the human route
  - Write a rule that sends sensitive replies to staff
  - Test the rule for recall in both languages
  - [Lab 3.4: Notice and routing rule (25 min)](https://sdaiaacademy.github.io/fn-106/labs/D3_4_draft_notice_parents.ipynb)

### Capstone: Capstone: the responsible build pack

Slides: https://sdaiaacademy.github.io/fn-106/slides/capstone.md

## Capstone

A responsible build pack for the assistant or the participant's own build (registers, minimisation code with its re-identification test, ethics test report, a record of processing entry, a breach checklist and the disclosure), submitted as a public repository and defended in a ten-minute review

**What you submit:** A public GitHub repository holding the build pack: the classification and risk registers, the minimisation and pseudonymisation code with its re-identification test, the ethics test report, a record of processing entry, a breach checklist and the disclosure, with a README that links each part. Then a ten-minute review in which the assessor changes one fact of the case and the participant revises the classification and risk entries live.

**Rubric:**

- Data protection: 25%
- Classification and sharing: 20%
- Risk assessment: 20%
- Ethics tests: 20%
- Disclosure and records: 15%

## Outcomes

- **LO1** Explain the PDPL obligations that govern a build, from lawful basis and minimisation to rights, retention, transfer and breach handling, given the assistant's data flow diagram (Awareness) Evidence: an annotated diagram naming the obligation at each step, checked against the reference
- **LO2** Distinguish what the data classification, data sharing and open data policies and the SDAIA Generative AI Guidelines each decide, given six questions about the build (Awareness) Evidence: a decision table naming the governing instrument, matching the reference on at least five of six
- **LO3** Classify each data set of the build under the four NDMO classification levels and derive the rule for sending it to an external model service, given the school group's data inventory and the policy's impact categories (Applied) Evidence: a classification register with level, reason and permitted destinations per data set
- **LO4** Apply minimisation and pseudonymisation to the data the assistant sends, and test whether records can be re-identified, given synthetic student and guardian records (Applied) Evidence: a before-and-after field list, a pseudonymisation script and a re-identification test result
- **LO5** Prepare a risk assessment that places the assistant in an ethics risk tier and works through the four phases of the national risk framework, given the build description and five candidate harms (Applied) Evidence: a risk register with tier, likelihood and impact ratings, an owner, a treatment and a review date per risk
- **LO6** Test the assistant against the ethics principles for fairness across Arabic and English enquiries, transparency and human review, and draft the disclosure parents see, given forty scripted enquiries (Applied) Evidence: a test report with results per check, the changes made and the disclosure text

## Tools

- **Language model for the build:** a free hosted endpoint used only with synthetic data (an OpenRouter free model), a scripted stand-in model that runs without a key, a small open-weight model served locally, for real data (not used in the labs)
- **Personal data detection:** regular-expression rules, Presidio
- **De-identification and linkage testing:** dataframe joins on quasi-identifiers (pandas), ARX
- **Licence references:** the SPDX licence list, model and dataset cards
- **Diagramming:** Mermaid, draw.io

## Prerequisites

- FN-101 Python for Data and AI Work
- FN-105 How Machine Learning and Language Models Work
- Reads a short Python program that calls a web API

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

---

SDAIA Academy · Data & AI Foundations Track · Responsible Data and AI Practice in the Kingdom

Course version 2027.1.0 · engine 1.0.0 · built 2026-11-15 · commit b84fcbb
