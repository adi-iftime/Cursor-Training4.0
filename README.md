# Cursor-Training4.0

The fourth iteration of an AI SDLC training repository.

## Cursor hooks and orchestration

This repo includes **project hooks** under [`.cursor/hooks.json`](.cursor/hooks.json) and [`.cursor/hooks/`](.cursor/hooks/) (security, PySpark static checks, orchestration locks, Jira/PR follow-ups, Databricks deploy guardrails). See [`.cursor/de-orchestration/README.md`](.cursor/de-orchestration/README.md) for `last_story.json` and branch lock files.

Run hook policy unit tests locally:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```
