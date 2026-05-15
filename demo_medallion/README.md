# demo_medallion

Python package scaffold for the **Medallion orders pipeline** demo ([SCRUM-64 epic](https://levi9-team-ivfys2q6.atlassian.net/browse/SCRUM-64)). Bootstrap story: [SCRUM-65](https://levi9-team-ivfys2q6.atlassian.net/browse/SCRUM-65). Raw ingest: [SCRUM-66](https://levi9-team-ivfys2q6.atlassian.net/browse/SCRUM-66).

## Raw fixture and ingest (SCRUM-66)

- **Fixture path:** `demo_medallion/data/raw/orders.json` — UTF-8 JSON **array** of order objects. Bundled via `setuptools` `package-data` for installs.
- **Required columns (per row):** `order_id`, `customer_id`, `order_ts`, `line_total`, `currency`, `status`. Extra keys (e.g. `notes`) are kept as DataFrame columns.
- **API:** `demo_medallion.ingest.load_orders(path)` returns a `pandas.DataFrame` (pre-Bronze; parsing and validation only). Default fixture path: `demo_medallion.paths.DEFAULT_RAW_ORDERS_FIXTURE`.
- **Errors:** missing file → `FileNotFoundError` with resolved path; bad JSON shape or missing required keys → `ValueError` with index/key detail.

## Setup

Requires **Python 3.11+**. From the repository root:

```bash
pip install -e ".[dev]"
```

## Tests

Runs the same suites as CI (`ruff check` + `pytest`):

```bash
ruff check demo_medallion
pytest
```

## CI

[![demo_medallion CI](https://github.com/adi-iftime/Cursor-Training4.0/actions/workflows/demo-medallion-ci.yml/badge.svg)](https://github.com/adi-iftime/Cursor-Training4.0/actions/workflows/demo-medallion-ci.yml)
