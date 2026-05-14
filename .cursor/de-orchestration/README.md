# Orchestration artifacts (hooks)

These files support **orchestration and Jira discipline** hooks:

- **`last_story.json`** — Written by the Technical Planning or Orchestrator flow before worker agents run. Validated on `subagentStop` by `de_jira_story_gate_subagent.py`. Required fields: `acceptance_criteria` (string), `worker_agent` (string), `dependencies` (list or string).

- **`locks.json`** — Auto-managed by `de_orch_path_lock.py` when editing paths under `pipelines/`. **Gitignored** locally to avoid committing machine-specific locks. Schema: [locks.schema.json](locks.schema.json).

Copy [last_story.example.json](last_story.example.json) to `last_story.json` when bootstrapping.
