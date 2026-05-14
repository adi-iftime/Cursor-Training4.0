---
name: security-review
description: Analyzes changes for attack surface, insecure patterns, authn/z, secrets, dependency and supply-chain risk, injection and unsafe input, PII handling, and log safety; produces actionable findings and remediation without approving unresolved high-severity risk. Use when reviewing pull requests, modifying authentication or authorization logic, exposing APIs or external endpoints, handling sensitive data or PII, introducing dependencies, modifying infrastructure or security-sensitive code, or validating production readiness.
---

# Security Review

Load this skill when:

- reviewing pull requests
- modifying authentication or authorization logic
- exposing APIs or external endpoints
- handling sensitive data or PII
- introducing dependencies
- modifying infrastructure or security-sensitive code
- validating production readiness

## Workflow

1. Analyze implementation changes and exposed attack surfaces.
2. Detect insecure coding patterns and potential vulnerabilities.
3. Validate authentication, authorization, and access control mechanisms.
4. Detect hardcoded secrets, tokens, or credentials.
5. Review dependency vulnerabilities and supply chain risks.
6. Validate secure handling of sensitive data and PII.
7. Detect injection vulnerabilities and unsafe input handling.
8. Verify logging does not expose sensitive information.
9. Produce actionable security findings and remediation guidance.
10. Avoid approving implementations with unresolved high-severity risks.

Security Review Rules:
- Never hardcode credentials or secrets.
- Validate all external inputs.
- Apply least privilege principles.
- Avoid exposing sensitive data in logs.
- Detect insecure dependencies and vulnerable patterns.

Required Security Review Areas:

Authentication
Authorization
Secrets Management
Dependency Security
Input Validation
Sensitive Data Handling

## Findings output (non-normative)

- For each issue: affected location, **Required Security Review Area**, severity rationale, exploitability or impact where known, and concrete remediation (config, code pattern, or process).
- Treat missing evidence of safe handling (e.g. unvalidated input on a trust boundary) as a finding to resolve or document with an accepted risk and owner.
