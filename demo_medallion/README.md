# demo_medallion

Python package scaffold for the **Medallion orders pipeline** demo ([SCRUM-64 epic](https://levi9-team-ivfys2q6.atlassian.net/browse/SCRUM-64)). Bootstrap story: [SCRUM-65](https://levi9-team-ivfys2q6.atlassian.net/browse/SCRUM-65).

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
