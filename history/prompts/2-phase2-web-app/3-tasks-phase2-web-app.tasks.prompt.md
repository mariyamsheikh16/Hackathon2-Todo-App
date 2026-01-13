---
id: 3
title: Generate Tasks for Phase II Web App
stage: tasks
date: 2026-01-14
surface: agent
model: gemini
feature: 2-phase2-web-app
branch: 2-phase2-web-app
user: {{USER}}
command: /sp.tasks
labels: [tasks, hackathon-phase-2]
links:
  spec: specs/2-phase2-web-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-phase2-web-app/tasks.md
tests:
  - 
---

## Prompt

You are an expert AI Technical Project Manager operating under Spec-Kit Plus and Agentic Development methodology. You are now in the TASK stage for Hackathon II – Phase II. The following documents are FINAL and APPROVED: • constitution.txt • overview.md • architecture.md • features/task-crud.md • features/authentication.md • plan.md ──────────────────────────────────────── OBJECTIVE OF TASK STAGE ──────────────────────────────────────── Break down the approved PLAN into small, atomic, implementation-ready tasks that can be executed by an AI coding agent (Gemini). Each task must be: • Clear • Independent • Testable • Ordered • Mapped to a specific system area ──────────────────────────────────────── STRICT RULES ──────────────────────────────────────── • DO NOT write code • DO NOT repeat the plan verbatim • DO NOT introduce new features • DO NOT merge multiple concerns into one task • DO NOT skip authentication or security tasks Only define WHAT to build, not HOW to code it. ──────────────────────────────────────── TASK CATEGORIES ──────────────────────────────────────── Organize tasks under the following sections: 1️⃣ Project Setup Tasks 2️⃣ Database & Models Tasks 3️⃣ Authentication Tasks 4️⃣ Backend API Tasks 5️⃣ Frontend UI Tasks 6️⃣ Integration Tasks 7️⃣ Security & Access Control Tasks 8️⃣ Testing & Validation Tasks ──────────────────────────────────────── TASK FORMAT (MANDATORY) ──────────────────────────────────────── For each task, use this exact format: • Task ID: • Task Title: • Description: • Dependencies: • Acceptance Criteria: ──────────────────────────────────────── TASK GRANULARITY RULE ──────────────────────────────────────── Each task should represent approximately: • 30–60 minutes of focused development work • ONE clear outcome • ONE responsibility ──────────────────────────────────────── OUTPUT REQUIREMENTS ──────────────────────────────────────── • Output ONE markdown document only • Title the document: tasks.md • Use professional, implementation-ready language • Maintain logical execution order ──────────────────────────────────────── FINAL INSTRUCTION ──────────────────────────────────────── This is the TASK definition stage only. Do not implement. Do not generate code. Do not explain decisions. Produce a clean, structured task breakdown that can be directly executed by Gemini in the next phase.

## Response snapshot

Generated the task breakdown for the Phase II Web App.

## Outcome

- ✅ Impact: High - Generated detailed tasks for the project.
- 🧪 Tests: N/A
- 📁 Files: 1 file created
- 🔁 Next prompts: /sp.implement
- 🧠 Reflection: The manual generation of tasks was successful.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (if applicable): N/A
