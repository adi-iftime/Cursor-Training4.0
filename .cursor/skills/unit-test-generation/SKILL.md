---
name: unit-test-generation
description: Analyzes implementation and expected behavior, generates isolated deterministic unit tests for happy paths, edges, boundaries, nulls, and errors, mocks externals when appropriate, and surfaces coverage gaps with concise cases. Use when implementing new functionality, modifying business logic, creating APIs, modifying pipelines, adding utility functions, validating edge cases, or improving test coverage.
---

# Unit Test Generation

Load this skill when:

- implementing new functionality
- modifying business logic
- creating APIs
- modifying pipelines
- adding utility functions
- validating edge cases
- improving test coverage

## Workflow

1. Analyze the implementation logic and expected behavior.
2. Generate unit tests covering normal scenarios and edge cases.
3. Validate boundary conditions, null handling, and error handling.
4. Ensure tests are isolated and deterministic.
5. Mock external systems and dependencies when appropriate.
6. Ensure tests remain maintainable and readable.
7. Verify expected outputs and side effects.
8. Detect missing test coverage areas.
9. Prefer concise and focused test cases.
10. Avoid flaky or environment-dependent tests.

Unit Testing Rules:
- Every production change requires tests.
- Cover positive and negative scenarios.
- Cover boundary conditions and edge cases.
- Avoid flaky tests.
- Mock external dependencies whenever possible.

Required Test Areas:

Happy Path
Edge Cases
Error Handling
Null Handling
Boundary Conditions

## Notes (non-normative)

- Match the project’s test framework, fixtures, and naming; mirror existing patterns in the same package.
- For time, randomness, and I/O: inject or stub dependencies so outcomes do not depend on wall clock, network, or global mutable state unless the test explicitly owns that setup.
