"""Paths and defaults for pipeline outputs (extended in later stories)."""

from __future__ import annotations

import os
from typing import Final

# Configurable via env for CI / local runs; default matches root `.gitignore` `out/`.
DEFAULT_OUTPUT_ROOT: Final[str] = os.environ.get("DEMO_MEDALLION_OUTPUT_ROOT", "out")
