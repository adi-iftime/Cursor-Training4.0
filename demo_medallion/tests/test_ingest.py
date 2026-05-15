"""Tests for SCRUM-66 raw JSON ingest."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from demo_medallion.ingest import REQUIRED_ORDER_COLUMNS, load_orders
from demo_medallion.paths import DEFAULT_RAW_ORDERS_FIXTURE


def test_load_orders_happy_path_fixture():
    df = load_orders(DEFAULT_RAW_ORDERS_FIXTURE)
    assert len(df) == 4
    assert list(df.columns) == list(REQUIRED_ORDER_COLUMNS) + ["notes"]
    assert set(REQUIRED_ORDER_COLUMNS).issubset(set(df.columns))
    assert df["order_id"].tolist()[0] == "ord-1001"


def test_load_orders_missing_file(tmp_path: Path):
    missing = tmp_path / "nope.json"
    with pytest.raises(FileNotFoundError) as exc:
        load_orders(missing)
    assert str(missing.resolve()) in str(exc.value)


def test_load_orders_schema_missing_required_key(tmp_path: Path):
    bad = tmp_path / "bad.json"
    bad.write_text(
        json.dumps([{c: "x" for c in REQUIRED_ORDER_COLUMNS if c != "status"}]),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="missing required keys"):
        load_orders(bad)
