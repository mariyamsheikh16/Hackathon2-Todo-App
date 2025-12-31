<!--
Sync Impact Report

- Version change: 1.0.0 -> 2.0.0
- List of modified principles:
    - All principles redefined based on user-provided project context.
- Added sections:
    - Application Requirements & Data Constraints
    - Specification Process & Prohibited Actions
- Removed sections:
    - Development Workflow
    - Quality Gates
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md (no changes needed)
    - ✅ .specify/templates/spec-template.md (no changes needed)
    - ✅ .specify/templates/tasks-template.md (no changes needed)
- Follow-up TODOs:
    - None
-->
# In-Memory Todo Console Application Constitution

## Core Principles

### I. Strict Spec-Driven Development
Follow spec-driven development strictly. Never implement functionality that is not explicitly defined in the current specification. All code must align exactly with the latest approved specification.

### II. Clean, Maintainable Python
Write clean, readable, and maintainable Python code. The code must be minimal, correct, and extensible for future phases.

### III. Clean Architecture
Follow SOLID principles and clean architecture practices. Separate concerns clearly into Models (data representation), Services (business logic), and a CLI layer (user interaction).

### IV. In-Memory Data Store
Keep the application fully in-memory. No database or file storage is permitted. Tasks exist only during runtime, and restarting the application resets all data.

### V. Deterministic and Testable Logic
Ensure all business logic is deterministic, predictable, and eminently testable. This is paramount for reliability.

### VI. Graceful Error Handling
Handle errors gracefully with clear, user-friendly messages. The user should understand what went wrong and why.

### VII. No Unsolicited Features
Do not add extra features beyond the current phase (Phase 1). Stick strictly to the defined application requirements.

### VIII. Simplicity and Clarity
Prefer simplicity and clarity over cleverness. Justify every design decision using the specification as the single source of truth.

### IX. Unstructured Code Prohibited
Do not write unclear, unstructured, or undocumented code. All code should be self-explanatory or appropriately commented where complex logic exists.

## Application Requirements & Data Constraints

The Phase 1 Todo application must support the following core features ONLY:
- Add Task (title and description)
- View Task List with completion status
- Update Task details by ID
- Delete Task by ID
- Mark Task as Complete or Incomplete (toggle)

Data Constraints:
- Tasks exist only during the application's runtime.
- No persistence is allowed. Restarting the application resets all tasks.

## Specification Process & Prohibited Actions

A specification MUST be generated and approved before writing any code.
- Store all specifications inside the `specs_history/` folder.
- Version specifications clearly (e.g., `spec_v1.txt`, `spec_v2.txt`).

Prohibited Actions:
- Do not introduce databases or file-based storage.
- Do not skip the specification step.
- Do not add any features beyond the defined Phase 1 requirements.

## Governance

This Constitution is the authoritative source for all project principles and practices. It supersedes any other conventions or ad-hoc practices. Amendments to this document require a formal review, documentation of the change, and an approved migration plan if necessary. All development activities and reviews must ensure compliance with this constitution.

**Version**: 2.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
