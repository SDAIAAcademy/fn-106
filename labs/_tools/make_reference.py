"""Write labs/data/reference/*.json, the results the safety-net cells fall back on.

    cd labs
    uv run python _tools/make_reference.py            # every lab
    uv run python _tools/make_reference.py D1_2       # the labs whose name starts so

Each lab source in _src/ is run with its solutions, as the solution notebook runs, and the
values named below are read from it and saved. Run it after changing a lab or the data.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

LABS = Path(__file__).resolve().parents[1]
REF = LABS / "data" / "reference"

# lab source -> {reference name: expression evaluated after the lab ran}
REFS = {
    "D1_1_map_every_field": {
        "lab11_inventory": "inv.drop(columns=['kind']).to_dict('records')",
        "lab11_flags": "{f: flag(f) for f in inv['field']}",
        "lab11_mermaid": "{'text': dfd}",
        "lab11_obligations": "obligations",
    },
    "D1_2_set_lawful_basis": {
        "lab12_basis": "basis",
        "lab12_needed": "needed",
        "lab12_fields": "{'before': before, 'after': after}",
    },
    "D1_3_pseudonymise_guardian_student": {
        "lab13_pseudo": "pseudo.to_dict('records')",
        "lab13_matches": "{'rate': rate, 'unique': int(unique)}",
        "lab13_general": "general.to_dict('records')",
    },
    "D1_4_write_retention_rule": {
        "lab14_rules": "rules",
        "lab14_breach": "size",
        "lab14_notice": "notice",
    },
    "D2_1_classify_six_data": {
        "lab21_impact": "impact",
        "lab21_register": "register.to_dict('records')",
        "lab21_small": "small.to_dict('records')",
    },
    "D2_2_decide_each_data": {
        "lab22_register": "dest.to_dict('records')",
        "lab22_fields": "field_dest",
    },
    "D2_3_assess_partner_entity": {
        "lab23_assessment": "assessment",
        "lab23_needed": "needed",
        "lab23_extract": "extract.to_dict('records')",
        "lab23_conditions": "conds",
    },
    "D2_4_check_licences_two": {
        "lab24_register": "register.to_dict('records')",
        "lab24_fit": "fit",
        "lab24_instruments": "answers",
    },
    "D3_1_write_three_checks": {
        "lab31_fairness": "fair",
        "lab31_transparency": "transp",
        "lab31_accountability": "acc",
    },
    "D3_2_run_forty_scripted": {
        "lab32_results": "results.to_dict('records')",
        "lab32_bias": "bias",
    },
    "D3_3_place_assistant_risk": {
        "lab33_tier": "tier",
        "lab33_ratings": "ratings",
        "lab33_register": "register.to_dict('records')",
    },
    "D3_4_draft_notice_parents": {
        "lab34_notice": "{'text': notice}",
        "lab34_router": "{'keywords': keywords}",
    },
}


def run(name: str, wanted: dict[str, str]) -> None:
    src = LABS / "_src" / f"{name}.py"
    ns: dict = {"__name__": "__lab__"}
    cwd = os.getcwd()
    os.chdir(LABS)
    try:
        exec(compile(src.read_text(encoding="utf-8"), str(src), "exec"), ns)
    finally:
        os.chdir(cwd)
    for ref, expr in wanted.items():
        value = eval(expr, ns)
        (REF / f"{ref}.json").write_text(json.dumps(value, ensure_ascii=False, indent=1, default=str) + "\n",
                                         encoding="utf-8", newline="\n")
        print("wrote", ref)


if __name__ == "__main__":
    sys.path.insert(0, str(LABS))
    REF.mkdir(parents=True, exist_ok=True)
    prefixes = sys.argv[1:]
    for name, wanted in REFS.items():
        if not prefixes or any(name.startswith(p) for p in prefixes):
            run(name, wanted)
