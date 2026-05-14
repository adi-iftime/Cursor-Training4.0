# Cursor hook stdin reference

Cursor sends JSON on stdin. Prefer **`tool_name`** and **`tool_input`** (see [Hooks docs](https://cursor.com/docs/hooks)).

## `subagentStop` matcher tuning

This repo leaves **`subagentStop` without a matcher** so every subagent completion is checked for `last_story.json`. After you capture real payloads from the Hooks output channel, add a `matcher` on that hook entry to limit noise (for example by `subagent_type`).

## `preToolUse` / `postToolUse`

Match on tool names such as `Shell`, `Write`, `StrReplace`, `Task`, and `MCP:...` prefixes.

## Spark quality prompt hook (optional)

A `type: "prompt"` hook on `^(Write|StrReplace)` runs for **every** edit matching that tool name, which blocks non-PySpark files when the model refuses. This repo ships **command-only** `de_spark_quality_static.py` by default. Re-add a prompt hook from the design doc only if you can scope it (for example via a future Cursor feature or a wrapper command hook that no-ops outside pipeline paths).
