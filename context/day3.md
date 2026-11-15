---
course: "Responsible Data and AI Practice in the Kingdom"
code: "FN-106"
version: "2027.1.0"
deck: "day3"
day: 3
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fn-106/slides/day3.html"
---

# Responsible Data and AI Practice in the Kingdom

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
