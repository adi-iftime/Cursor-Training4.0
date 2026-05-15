"""Paths and defaults for pipeline outputs (extended in later stories)."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Final

PACKAGE_ROOT: Final[Path] = Path(__file__).resolve().parent

# Default bundled fixture: `demo_medallion/data/raw/orders.json` (SCRUM-66).
DEFAULT_RAW_ORDERS_FIXTURE: Final[Path] = PACKAGE_ROOT / "data" / "raw" / "orders.json"

# Configurable via env for CI / local runs; default matches root `.gitignore` `out/`.
DEFAULT_OUTPUT_ROOT: Final[str] = os.environ.get("DEMO_MEDALLION_OUTPUT_ROOT", "out")
