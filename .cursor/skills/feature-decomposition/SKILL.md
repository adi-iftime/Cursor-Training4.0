---
name: feature-decomposition
description: Analyzes features and requirements, splits work by technical boundaries and ownership domains (frontend, backend, data, infrastructure, testing), maps dependencies, and surfaces parallelization with minimal cross-unit overlap. Use when planning new features, decomposing implementation requests, creating execution plans, preparing sprint work, identifying parallelization opportunities, planning multi-agent execution, or breaking large requests into smaller tasks.
---

# Feature Decomposition

Load this skill when:

- planning new features
- decomposing implementation requests
- creating execution plans
- preparing sprint work
- identifying parallelization opportunities
- planning multi-agent execution
- breaking large requests into smaller tasks

## Workflow

1. Analyze the requested feature or business requirement.
2. Break implementation work into small independently executable units.
3. Identify technical boundaries and ownership domains.
4. Separate frontend, backend, data engineering, infrastructure, and testing responsibilities.
5. Define dependencies between implementation tasks.
6. Ensure work items support isolated pull requests and parallel execution.
7. Minimize cross-team or cross-agent overlap.
8. Identify areas requiring additional architecture analysis.
9. Detect oversized implementation scopes and split them further.
10. Produce implementation-ready work decomposition outputs.

Feature Decomposition Rules:
- Prefer small independently executable tasks.
- Minimize overlap between implementation units.
- Separate concerns by ownership domain.
- Avoid oversized stories and large PRs.
- Design work for parallel execution whenever possible.

Required Output Sections:

Feature Summary
Work Breakdown
Dependency Mapping
Recommended Ownership
Parallelization Opportunities

## Guidance (non-normative)

### Feature Summary

- Restate the user-visible outcome and constraints.
- Note open questions, unknowns, and assumptions explicitly.

### Work Breakdown

- Emit a flat or shallowly nested list of units; each unit should have one primary responsibility and a clear “done” definition.
- Tag each unit with primary domain: `frontend` | `backend` | `data` | `infrastructure` | `testing` (pick one primary; secondary tags only when unavoidable).
- Flag units that need **architecture-analysis** before implementation.

### Dependency Mapping

- Use directed relationships: `A blocks B`, `A soft-depends on B` (ordering preference, not a hard block).
- Call out shared artifacts (schemas, contracts, feature flags, migrations) as coordination points.

### Recommended Ownership

- Map units to owning role or system (team, service, repo area) without inventing org facts; use placeholders if unknown (`Owner: TBD (platform team)`).

### Parallelization Opportunities

- Group units that can proceed concurrently when dependencies allow.
- List **serialization points** (same file, same migration chain, same API contract version) that force ordering or merge ownership.

### Quality bar

- If a unit still implies multiple PRs or mixed unrelated concerns, split again until the Feature Decomposition Rules hold.
- Prefer contracts and interfaces first, then parallel implementations against those contracts.
