---
name: code-review
description: Reviews pull requests for readability, maintainability, architecture fit, duplication, complexity, testing, docs, and scalability risks; produces actionable feedback without drive-by refactors. Use when reviewing pull requests, validating implementation quality, checking architecture consistency, evaluating maintainability, analyzing complex implementations, or reviewing production-ready code.
---

# Code Review

Load this skill when:

- reviewing pull requests
- validating implementation quality
- checking architecture consistency
- evaluating maintainability
- analyzing complex implementations
- reviewing production-ready code

## Workflow

1. Analyze pull request changes and impacted components.
2. Validate readability, maintainability, and consistency.
3. Detect anti-patterns, duplicated logic, and excessive complexity.
4. Verify compliance with architecture and engineering conventions.
5. Evaluate naming conventions and modularity.
6. Detect potential scalability or maintainability risks.
7. Validate testing completeness and documentation quality.
8. Produce actionable and constructive review comments.
9. Recommend improvements without unnecessary refactoring.
10. Avoid approving low-quality or risky implementations.

Code Review Rules:
- Prefer readability over cleverness.
- Avoid unnecessary complexity.
- Respect existing architecture conventions.
- Detect duplicated logic and anti-patterns.
- Ensure sufficient testing coverage.

Required Review Areas:

Readability
Maintainability
Architecture Consistency
Testing Quality
Scalability Risks

## Review output (non-normative)

- Structure comments by **Required Review Areas** when useful; each item should state what was observed, why it matters, and a concrete next step.
- Separate **must-fix** (correctness, security, broken contracts, missing critical tests) from **should-fix** and **optional** improvements; avoid scope creep beyond the PR’s intent.
