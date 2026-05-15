"""Load raw orders JSON into a pandas DataFrame (pre-Bronze ingest).

Fixture layout (`demo_medallion/data/raw/orders.json`):
  JSON **array** of objects. Each object must include the columns in
  ``REQUIRED_ORDER_COLUMNS``. Optional keys (e.g. ``notes``) are preserved as
  DataFrame columns when present.

Public API:
  ``load_orders(path)`` — read file at ``path``, validate schema keys per row,
  return ``pandas.DataFrame`` with one row per order (no business transforms).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

# Columns that every order record must contain (stable contract for Bronze).
REQUIRED_ORDER_COLUMNS: tuple[str, ...] = (
    "order_id",
    "customer_id",
    "order_ts",
    "line_total",
    "currency",
    "status",
)


def load_orders(path: str | Path) -> pd.DataFrame:
    """Load orders from a local JSON file into a DataFrame.

    Parameters
    ----------
    path:
        Filesystem path to a UTF-8 JSON file containing an array of order objects.

    Returns
    -------
    pandas.DataFrame
        One row per order; includes all keys present in the source objects.

    Raises
    ------
    FileNotFoundError
        If ``path`` does not exist (message includes the resolved path).
    ValueError
        If JSON is not a non-empty list of dicts, or a row is missing a
        required column.
    """
    p = Path(path).expanduser()
    if not p.is_file():
        msg = f"orders JSON not found: {p.resolve()}"
        raise FileNotFoundError(msg)

    raw_text = p.read_text(encoding="utf-8")
    try:
        payload: Any = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in orders file {p!s}: {exc}") from exc

    if not isinstance(payload, list):
        raise ValueError("orders JSON root must be a JSON array of objects")
    if len(payload) == 0:
        raise ValueError("orders JSON array must contain at least one order")

    rows: list[dict[str, Any]] = []
    for i, item in enumerate(payload):
        if not isinstance(item, dict):
            got = type(item).__name__
            raise ValueError(f"orders[{i}] must be an object, got {got}")
        missing = [c for c in REQUIRED_ORDER_COLUMNS if c not in item]
        if missing:
            raise ValueError(
                f"orders[{i}] missing required keys {missing!s}; "
                f"required: {list(REQUIRED_ORDER_COLUMNS)}"
            )
        rows.append(item)

    return pd.DataFrame.from_records(rows)
