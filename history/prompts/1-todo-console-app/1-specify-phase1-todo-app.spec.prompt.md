---
id: 1
title: Specify Phase 1 Todo App
stage: spec
date: 2026-01-01
surface: agent
model: gemini-cli
feature: 1-todo-console-app
branch: 1-todo-console-app
user: User
command: /sp.specify
labels: [spec, feature-init]
links:
  spec: specs/1-todo-console-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-todo-console-app/spec.md
 - specs/1-todo-console-app/checklists/requirements.md
tests:
 - none
---

## Prompt

SPECIFICATION PROMPT – PHASE 1 TODO APPLICATION =============================================== ROLE: You are a Spec-Kit Plus specification generator. You must strictly follow the Constitution defined for this project. Do NOT write any code. Your task is to produce a clear, complete, and testable specification. PROJECT OVERVIEW: This is a Phase 1 in-memory Todo Console Application written in Python 3.13+. The application runs in a command-line environment and stores all tasks in memory. SCOPE LIMITATION: This specification must cover ONLY Phase 1 (Basic Level). No advanced or future features are allowed. FUNCTIONAL REQUIREMENTS: The application MUST support the following features: 1. ADD TASK - The user can create a new task. - Each task must have: - A unique integer ID (auto-incremented) - A title (required, non-empty string) - A description (optional string) - A completion status (default: incomplete) 2. VIEW TASK LIST - The user can view all existing tasks. - Each task display must include: - Task ID - Title - Completion status indicator ([ ] for incomplete, [✓] for complete) 3. UPDATE TASK - The user can update an existing task by providing its ID. - The user may update: - Title - Description - If the ID does not exist, an appropriate error message must be shown. 4. DELETE TASK - The user can delete a task using its ID. - If the ID does not exist, an appropriate error message must be shown. 5. MARK TASK AS COMPLETE / INCOMPLETE - The user can toggle the completion status of a task using its ID. - Completed tasks become incomplete and vice versa. NON-FUNCTIONAL REQUIREMENTS: - The application must run entirely in memory. - No data persistence is allowed. - The application must be deterministic and predictable. - The user interface must be simple and text-based. - All user errors must be handled gracefully. USER INTERACTION RULES: - The application must show a menu of options. - The user must select actions via numeric input. - Invalid inputs must not crash the application. DATA MODEL: - Tasks are stored in a list during runtime. - Each task is represented by a structured object or dictionary. OUT OF SCOPE: - File storage - Databases - User authentication - Search or filtering - Due dates or priorities ACCEPTANCE CRITERIA: - A user can add, view, update, delete, and toggle tasks. - All features work during a single runtime session. - Restarting the app resets all data. - No functionality exists outside this specification. DELIVERABLE: Produce a finalized Phase 1 specification suitable for implementation. DO NOT: - Write code - Suggest future improvements - Expand scope beyond Phase 1

## Response snapshot

The specification for the 'Phase 1 In-Memory Todo Application' has been successfully created. I have established a new feature branch `1-todo-console-app` and generated the specification document at `specs/1-todo-console-app/spec.md`. All requirements from your prompt have been mapped to user stories, functional requirements, and success criteria. The associated quality checklist has been created and marked as complete.

## Outcome

- ✅ Impact: Successfully created a new feature specification and all associated artifacts.
- 🧪 Tests: n/a
- 📁 Files: 2 files created.
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: The initial script failure required a manual workaround. The process of creating the branch, directories, and files manually was successful. The user's prompt was extremely detailed, which made spec generation very straightforward.

## Evaluation notes (flywheel)

- Failure modes observed: PowerShell execution policy blocked the helper script.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment: n/a
