"""Shared helpers for the FN-106 labs (Rawafid Schools Group, synthetic data).

    import rawafid as U

U.DATA          the data folder (labs/data)
U.TODAY         the labs' "today", 2026-11-12
U.QUICK         True when FN106_QUICK=1: smaller runs
U.pick(a, b)    a normally, b in quick mode
U.load(name)    a CSV of labs/data as a pandas DataFrame (strings kept as strings)
U.jsonl(name)   a JSON Lines file of labs/data as a list of dicts
U.json(name)    a JSON file of labs/data
U.reference(n)  the reference result of an exercise, for the safety-net cells
U.check(ok, m)  prints a tick or raises AssertionError with the message
"""

from __future__ import annotations

import json as _json
import os
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REF = DATA / "reference"
TODAY = date(2026, 11, 12)
QUICK = os.environ.get("FN106_QUICK", "0") == "1"


def pick(full, quick):
    return quick if QUICK else full


def load(name: str):
    import pandas as pd
    return pd.read_csv(DATA / name, dtype=str, keep_default_na=False)


def jsonl(name: str) -> list[dict]:
    return [_json.loads(line) for line in (DATA / name).read_text(encoding="utf-8").splitlines() if line.strip()]


def json(name: str):
    return _json.loads((DATA / name).read_text(encoding="utf-8"))


def reference(name: str):
    """The reference result of exercise `name`, so later cells run when it is not done yet."""
    print(f"(safety net: using the reference result for {name})")
    return _json.loads((REF / f"{name}.json").read_text(encoding="utf-8"))


def check(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError("not yet: " + message)
    print("✅", message)


def table(rows, columns=None):
    """A list of dicts as a DataFrame, for display."""
    import pandas as pd
    return pd.DataFrame(rows, columns=columns)
