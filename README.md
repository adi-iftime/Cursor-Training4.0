# Cursor-Training4.0

The fourth iteration of an AI SDLC training repository.

## Cursor hooks and orchestration

This repo registers **advisory-only** Cursor hooks in [.cursor/hooks.json](.cursor/hooks.json) (`postToolUse`, `failClosed: false`): PySpark/pipeline hints ([`de_spark_quality_static.py`](.cursor/hooks/de_spark_quality_static.py)), PR checklist injection ([`de_pr_quality_inject.py`](.cursor/hooks/de_pr_quality_inject.py)), and pipeline test coaching ([`de_pipeline_tests_coach.py`](.cursor/hooks/de_pipeline_tests_coach.py)). They **do not** block tools, Task, Shell, or MCP. Other hook scripts in [.cursor/hooks/](.cursor/hooks/) are **not** enabled unless you add them. See [PAYLOAD_SAMPLES.md](.cursor/hooks/PAYLOAD_SAMPLES.md).

**Jira:** When the Atlassian integration is enabled, agents must use the **Atlassian MCP** for all Jira operations (see [jira-atlassian-mcp.mdc](.cursor/rules/jira-atlassian-mcp.mdc)).

Run hook policy unit tests locally:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## demo_medallion (data engineering demo)

See [demo_medallion/README.md](demo_medallion/README.md) for package setup, `ruff` / `pytest`, and CI.

