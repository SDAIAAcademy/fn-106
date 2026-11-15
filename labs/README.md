# Responsible Data and AI Practice in the Kingdom: labs

## Quick start

- Google Colab: open a notebook from the course page; its first cell clones this repository.
- Locally: clone the repository, then open the notebooks in `labs/` with Jupyter.

| Unit | Session | Notebook |
|---|---|---|
| Day 1 | Session 1 · Where personal data flows in a build | [`D1_1_map_every_field.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D1_1_map_every_field.ipynb) |
| Day 1 | Session 2 · Lawful basis and minimisation | [`D1_2_set_lawful_basis.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D1_2_set_lawful_basis.ipynb) |
| Day 1 | Session 3 · Pseudonymisation and its limits | [`D1_3_pseudonymise_guardian_student.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D1_3_pseudonymise_guardian_student.ipynb) |
| Day 1 | Session 4 · Rights, retention and breaches | [`D1_4_write_retention_rule.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D1_4_write_retention_rule.ipynb) |
| Day 2 | Session 1 · Data classification levels | [`D2_1_classify_six_data.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D2_1_classify_six_data.ipynb) |
| Day 2 | Session 2 · What may reach an external model | [`D2_2_decide_each_data.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D2_2_decide_each_data.ipynb) |
| Day 2 | Session 3 · Sharing with another entity | [`D2_3_assess_partner_entity.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D2_3_assess_partner_entity.ipynb) |
| Day 2 | Session 4 · Licences and provenance | [`D2_4_check_licences_two.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D2_4_check_licences_two.ipynb) |
| Day 3 | Session 1 · Principles into tests | [`D3_1_write_three_checks.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D3_1_write_three_checks.ipynb) |
| Day 3 | Session 2 · Testing the assistant | [`D3_2_run_forty_scripted.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D3_2_run_forty_scripted.ipynb) |
| Day 3 | Session 3 · Risk tier and risk register | [`D3_3_place_assistant_risk.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D3_3_place_assistant_risk.ipynb) |
| Day 3 | Session 4 · Disclosure and human review | [`D3_4_draft_notice_parents.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fn-106/blob/main/labs/D3_4_draft_notice_parents.ipynb) |

**Before Day 1** work through [`PREWORK.md`](PREWORK.md): a reading guide to the core instruments that ends in an entry quiz of ten questions (about three hours).

## The case and its data

Every lab works on Wafi, the parent-enquiry assistant of Rawafid Schools Group, a fictional private school group. All records in `data/` are synthetic: `prepare_data.py` writes them (seed 106, standard library only), so no real person is described. `rawafid.py` holds the shared helpers and `wafi.py` the assistant as Dana built it.

Every lab starts from a supplied reference state: its inputs are in `data/`, and where it builds on an earlier lab it reads that lab's reference result from `data/reference/`. A safety-net cell after each exercise falls back on the reference result, so an unfinished exercise never blocks the next one.

## The model

No lab downloads a model. Wafi drafts replies with one of two models:

| Setting | Model | Use |
|---|---|---|
| `WAFI_MODEL=standin`, or no `OPENROUTER_API_KEY` | A scripted stand-in: fixed templates filled from the prompt | Default. Everyone gets the same results; it imitates one weakness on purpose (it reads Modern Standard Arabic phrasings better than Gulf ones) |
| `OPENROUTER_API_KEY` set | A free hosted model on OpenRouter (`WAFI_HOSTED_MODEL`, default `google/gemma-4-31b-it:free`) | Optional, synthetic data only: a hosted endpoint whose location is unknown is a transfer outside the Kingdom |

If a hosted call fails (no key, 401, 429, no network), the stand-in answers and the result says so. Labs 1.1 and 1.2 always use the stand-in, because they compare prompts rather than replies; Lab 3.2 is the only lab that uses the hosted model when a key is set. The other labs call no model.

## For trainers

- Reference results: `uv run python _tools/make_reference.py` (or a prefix such as `D3`) runs each solution source and writes `data/reference/`. Run it after changing a lab or the data, in lab order.
- To run a notebook headless on Windows, set `PYTHONUTF8=1` first, or the Arabic in the sources is misread.

The notebooks are generated from the percent-format sources in `labs/_src/` by `labs/_tools/py2nb.py` (`uv run python _tools/py2nb.py` from `labs/`), which also writes the solutions to `labs/solutions/`. Edit the sources, not the notebooks.
