# Contributing

## Pull requests

New pull requests use the template in [.github/pull_request_template.md](.github/pull_request_template.md) (GitHub loads it automatically for this repo).

Before opening a PR, confirm:

1. **Jira key** in the title and description for traceability.
2. **One story per PR** — [.cursor/rules/one-story-per-pr.mdc](.cursor/rules/one-story-per-pr.mdc).
3. **Tests** where the change touches production logic — [.cursor/rules/mandatory-tests.mdc](.cursor/rules/mandatory-tests.mdc).
4. **`OWNERSHIP=path/prefix/`** on Cursor **Task** prompts when implementing under this repo’s orchestration rules — [.cursor/rules/jira-atlassian-mcp.mdc](.cursor/rules/jira-atlassian-mcp.mdc).

## Agents and Jira

When the Atlassian integration is enabled, use the **Atlassian MCP** for Jira operations — see [.cursor/rules/jira-atlassian-mcp.mdc](.cursor/rules/jira-atlassian-mcp.mdc).

## Local verification

- Hook policy tests: `python3 -m unittest discover -s tests -p "test_*.py" -v`
- Package-specific checks: see [demo_medallion/README.md](demo_medallion/README.md) for `ruff` / `pytest` and CI notes.
