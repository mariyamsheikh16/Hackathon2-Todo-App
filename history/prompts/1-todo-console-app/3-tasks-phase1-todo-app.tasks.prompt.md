---
id: 3
title: Generate Tasks for Todo App
stage: tasks
date: 2026-01-01
surface: agent
model: gemini-cli
feature: 1-todo-console-app
branch: 1-todo-console-app
user: User
command: /sp.tasks
labels: [tasks, planning]
links:
  spec: specs/1-todo-console-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-todo-console-app/tasks.md
tests:
 - none
---

## Prompt

IMPLEMENTATION TASK PROMPT – PHASE 1 TODO APPLICATION ==================================================== ROLE: You are a Python implementation agent following Spec-Kit Plus methodology. You must strictly follow: - The project Constitution (constitution.txt) - The finalized specification (spec_v1.txt) - The approved implementation plan OBJECTIVE: Implement the Phase 1 in-memory Todo Console Application exactly as specified. GLOBAL RULES: 1. Do not violate the Constitution. 2. Do not deviate from spec_v1.txt. 3. Do not add features not listed in Phase 1. 4. Follow the implementation plan step-by-step. 5. Write clean, readable, and maintainable Python 3.13+ code. 6. Keep all data in memory only. 7. Handle all user input errors gracefully. 8. The application must never crash due to invalid input. PROJECT STRUCTURE TASKS: TASK 1: models.py - Define the Task data structure. - Include: - id - title - description - completion status - Keep the model simple and clear. TASK 2: todo_service.py - Implement in-memory task storage. - Implement business logic for: - Adding a task - Listing all tasks - Updating a task by ID - Deleting a task by ID - Toggling task completion status - Ensure ID uniqueness and proper error handling. TASK 3: cli.py - Implement all user interaction logic. - Display a clear text-based menu. - Accept numeric user input for actions. - Validate user input before passing it to the service layer. - Display user-friendly success and error messages. TASK 4: main.py - Act as the application entry point. - Initialize required components. - Start the CLI loop. - Ensure clean application exit. BEHAVIORAL REQUIREMENTS: - Tasks must display with status indicators: [ ] Incomplete [✓] Complete - Task IDs must be visible to the user. - Invalid task IDs must show clear error messages. - Restarting the app resets all tasks. DELIVERABLE EXPECTATIONS: - Fully working console application. - Code organized inside `/src`. - No unused code or dead logic. - Code must exactly match the specification. DO NOT: - Add persistence (files, database) - Add tests - Add advanced features - Refactor beyond what the plan allows

## Response snapshot

I have generated the `tasks.md` file, breaking down the project into a series of actionable, dependency-ordered tasks organized by feature phase. The file is located at `specs/1-todo-console-app/tasks.md`.

## Outcome

- ✅ Impact: Successfully generated a detailed task list for the feature.
- 🧪 Tests: n/a
- 📁 Files: 1 file created.
- 🔁 Next prompts: /sp.implement
- 🧠 Reflection: The process was smooth. The detailed design documents allowed for a clear and logical breakdown of tasks. Grouping tasks by user story priority ensures a focus on delivering the MVP first.

## Evaluation notes (flywheel)

- Failure modes observed: PowerShell execution policy blocked helper scripts, requiring a manual workaround.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment: n/a
