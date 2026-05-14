# Cursor hook stdin reference

Cursor sends JSON on stdin. Prefer **`tool_name`** and **`tool_input`** (see [Hooks docs](https://cursor.com/docs/hooks)).

## `subagentStop` matcher tuning

This repo leaves **`subagentStop` without a matcher** so every subagent completion is checked for `last_story.json`. After you capture real payloads from the Hooks output channel, add a `matcher` on that hook entry to limit noise (for example by `subagent_type`).

## `preToolUse` / `postToolUse`

Match on tool names such as `Shell`, `Write`, `StrReplace`, `Task`, and `MCP:...` prefixes.

## Task orchestration: planning vs implementation

`de_orch_one_story_one_pr.py` distinguishes **planning** vs **implementation** using `subagent_type` on the Task payload (see `policies/orchestration_agents.json`).

- **Planning** (`technical-planning-agent`, `orchestrator-agent`, `qa-agent`, `security-agent`, `documentation-agent`): Task calls **do not** require a Jira key or `OWNERSHIP=` in the prompt.
- **Implementation** (`data-engineering-agent`, `backend-agent`, `frontend-agent`, `data-scientist-agent`, `data-analyst-agent`): Task calls **must** include exactly one allowed Jira key and `OWNERSHIP=path/` in the prompt.
- **Unknown or missing `subagent_type`**: treated as **implementation** (strict) so new agents do not bypass gates by accident. Add new planning types explicitly in `orchestration_agents.json` if they should be exempt.

Fallback: include `subagent_type: orchestrator-agent` (or similar) in the Task **prompt** text if the IDE does not send `tool_input.subagent_type`.

## Spark quality prompt hook (optional)

A `type: "prompt"` hook on `^(Write|StrReplace)` runs for **every** edit matching that tool name, which blocks non-PySpark files when the model refuses. This repo ships **command-only** `de_spark_quality_static.py` by default. Re-add a prompt hook from the design doc only if you can scope it (for example via a future Cursor feature or a wrapper command hook that no-ops outside pipeline paths).
