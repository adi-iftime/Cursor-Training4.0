# Orchestration artifacts (hooks)

These files support **orchestration and Jira discipline** hooks:

- **`last_story.json`** — Written by the Technical Planning or Orchestrator flow before worker agents run. Validated on `subagentStop` by `de_jira_story_gate_subagent.py`. Required fields: `acceptance_criteria` (string), `worker_agent` (string), `dependencies` (list or string).

- **`locks.json`** — Auto-managed by `de_orch_path_lock.py` when editing paths under `pipelines/`. **Gitignored** locally to avoid committing machine-specific locks. Schema: [locks.schema.json](locks.schema.json).

## Task tool: planning vs implementation

The `de_orch_one_story_one_pr.py` hook reads [`../hooks/policies/orchestration_agents.json`](../hooks/policies/orchestration_agents.json). **Planning** subagent types may run `Task` without a Jira key or `OWNERSHIP=` in the prompt. **Implementation** types (and unknown/missing `subagent_type`) must include exactly one allowed Jira key and `OWNERSHIP=...` for overlap-safe execution.

Copy [last_story.example.json](last_story.example.json) to `last_story.json` when bootstrapping.
