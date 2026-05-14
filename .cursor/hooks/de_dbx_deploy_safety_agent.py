#!/usr/bin/env python3
import sys
from pathlib import Path

HOOKS_DIR = Path(__file__).resolve().parent
if str(HOOKS_DIR) not in sys.path:
    sys.path.insert(0, str(HOOKS_DIR))

from de_hook_policies import main_dbx_deploy_agent

if __name__ == "__main__":
    main_dbx_deploy_agent()
