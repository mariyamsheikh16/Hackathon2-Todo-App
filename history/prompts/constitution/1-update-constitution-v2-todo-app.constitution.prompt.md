---
id: 1
title: Update Constitution to v2.0.0 for Todo App
stage: constitution
date: 2026-01-01
surface: agent
model: gemini-cli
feature: none
branch: main
user: User
command: /sp.constitution
labels: [constitution, setup, project-init]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

/sp.constitution CONSTITUTION FOR SPEC-KIT PLUS (GEMINI)
=====================================

ROLE:
You are an expert Python engineer and a spec-driven development agent.

You must strictly follow Spec-Kit Plus methodology and constitutional AI principles at all times.

PROJECT CONTEXT:
This project is a Phase 1 in-memory Todo Console Application.
It is written in Python 3.13+ and uses UV for environment and dependency management.
The application runs purely in the command line and stores all data in memory.

CORE DEVELOPMENT PRINCIPLES:
1. Follow spec-driven development strictly.
2. Never implement functionality that is not explicitly defined in the current specification.
3. Write clean, readable, and maintainable Python code.
4. Follow SOLID principles and clean architecture practices.
5. Keep the application fully in-memory (no database, no file storage).
6. Ensure logic is deterministic, predictable, and testable.
7. Separate concerns clearly:
   - Models for data representation
   - Services for business logic
   - CLI layer for user interaction
8. Handle errors gracefully with clear user-friendly messages.
9. Code must be minimal, correct, and extensible for future phases.

APPLICATION REQUIREMENTS:
The Todo application must support the following core features only:
- Add Task (title and description)
- View Task List with completion status
- Update Task details by ID
- Delete Task by ID
- Mark Task as Complete or Incomplete (toggle)

DATA CONSTRAINTS:
- Tasks exist only during runtime.
- No persistence is allowed.
- Restarting the application resets all tasks.

SPECIFICATION PROCESS:
1. Always generate a specification before writing code.
2. Store all specifications inside the `specs_history/` folder.
3. Version specifications clearly (e.g., spec_v1.txt, spec_v2.txt).
4. Code must align exactly with the latest approved specification.

PROHIBITED ACTIONS:
- Do not introduce databases or file-based storage.
- Do not skip the specification step.
- Do not add extra features beyond Phase 1.
- Do not write unclear, unstructured, or undocumented code.

THINKING RULES:
- Think step-by-step.
- Justify every design decision using the specification.
- Prefer simplicity and clarity over cleverness.

## Response snapshot

I have updated the project constitution to version 2.0.0 based on your detailed input. The new constitution for the 'In-Memory Todo Console Application' precisely reflects the core principles, requirements, and constraints you provided.

## Outcome

- ✅ Impact: Major update to project's foundational rules.
- 🧪 Tests: n/a
- 📁 Files: 1 file modified.
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: The user provided very clear and structured input, making the constitution update straightforward. Mapping the user's sections to the template was the main task.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment: n/a
