---
name: api-development
description: Guides API and backend work: align with architecture, routing, and validation patterns; typed contracts and versioning; secure handling, authz, observability, tests, docs, and focused endpoints. Use when implementing APIs, modifying backend services, exposing external endpoints, implementing CRUD operations, modifying authentication or authorization logic, integrating external systems, implementing async processing workflows, or validating production backend readiness.
---

# API Development

Load this skill when:

- implementing APIs
- modifying backend services
- exposing external endpoints
- implementing CRUD operations
- modifying authentication or authorization logic
- integrating external systems
- implementing async processing workflows
- validating production backend readiness

## Workflow

1. Analyze existing API architecture, routing conventions, and service boundaries.
2. Follow existing backend patterns, validation standards, and error handling conventions.
3. Design APIs with clear contracts, typed request and response models, and versioning considerations.
4. Implement robust input validation and secure request handling.
5. Ensure authentication and authorization mechanisms are respected.
6. Add logging, observability, and error tracking for production readiness.
7. Generate unit tests and integration tests for API behavior.
8. Optimize for maintainability, scalability, and readability.
9. Document API behavior, contracts, and dependencies.
10. Avoid tightly coupled business logic and oversized endpoints.

API Development Rules:
- Validate all external inputs.
- Use typed request and response models whenever possible.
- Follow existing routing and service conventions.
- Keep endpoints focused and maintainable.
- Add logging and observability for production APIs.
- Add unit tests and integration tests for all endpoints.

Required Validation Areas:

Input Validation
Authentication and Authorization
Error Handling
Logging and Observability
API Contract Consistency
Scalability Risks

## Notes (non-normative)

- Before adding routes or handlers, locate existing OpenAPI/GraphQL/schema definitions and mirror error shapes, status codes, and pagination patterns.
- When reviewing changes, walk each endpoint against the **Required Validation Areas** and cite gaps explicitly.
