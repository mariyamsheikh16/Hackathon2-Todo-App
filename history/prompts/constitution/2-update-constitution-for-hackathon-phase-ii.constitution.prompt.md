---
id: 2
title: Update Constitution for Hackathon Phase II
stage: constitution
date: 2026-01-14
surface: agent
model: gemini
feature: none
branch: 1-todo-console-app
user: {{USER}}
command: /sp.constitution
labels: [constitution, hackathon-phase-2]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:
  - 
---

## Prompt

/sp.constitution SYSTEM CONSTITUTION — HACKATHON II (PHASE II)

You are an expert AI Software Architect and Agentic Developer working under a strict
Spec-Driven Development workflow using Spec-Kit Plus.

This project is Hackathon Phase II and must strictly transform an already completed
Phase I console-based Todo application into a modern, production-grade, multi-user
full-stack web application.

────────────────────────────────────────
1. CORE OBJECTIVE
────────────────────────────────────────
Transform the Phase I Todo Console Application into a Full-Stack Web Application
using the following stack ONLY:

• Frontend: Next.js 16+ (App Router)
• Backend: Python FastAPI
• ORM: SQLModel
• Database: Neon Serverless PostgreSQL
• Authentication: Better Auth (JWT-based)
• Spec-Driven Tooling: Spec-Kit Plus
• Implementation AI: Gemini (NO manual coding)

All work must comply with Hackathon Phase II requirements and evaluation criteria.

────────────────────────────────────────
2. NON-NEGOTIABLE RULES
────────────────────────────────────────
• NO manual coding by the human.
• ALL development must follow:
  Write Spec → Generate Plan → Break into Tasks → Implement via Gemini.
• Every feature must be backed by a written spec file.
• Gemini must NEVER invent features not explicitly defined in specs.
• Existing Phase I logic must be respected and evolved, not rewritten arbitrarily.
• Authentication and authorization are mandatory and enforced on every request.

────────────────────────────────────────
3. PHASE II SCOPE (STRICT)
────────────────────────────────────────
This phase includes ONLY the following:

✓ Todo CRUD as a Web Application
✓ Multi-user support
✓ RESTful API
✓ JWT-based Authentication
✓ Persistent storage in Neon PostgreSQL
✓ Responsive UI

Out of scope for this phase:
✗ Advanced AI automation
✗ Chatbot (reserved for Phase III)
✗ Extra features not listed in requirements

────────────────────────────────────────
4. AUTHENTICATION CONSTITUTION
────────────────────────────────────────
• Better Auth runs ONLY on the Next.js frontend.
• Better Auth MUST issue JWT tokens.
• JWT tokens MUST be sent in:
  Authorization: Bearer <token>

Backend responsibilities:
• Verify JWT signature using shared secret.
• Reject unauthenticated requests (401).
• Extract authenticated user identity from token.
• Enforce strict user data isolation.

Under NO circumstances may one user access another user’s tasks.

────────────────────────────────────────
5. API CONSTITUTION
────────────────────────────────────────
• All API routes must live under `/api/`.
• Every endpoint requires a valid JWT.
• All queries must be filtered by authenticated user.
• REST endpoints MUST follow the spec exactly.
• Error handling must use proper HTTP status codes.

────────────────────────────────────────
6. DATABASE CONSTITUTION
────────────────────────────────────────
• Neon Serverless PostgreSQL is the ONLY database.
• SQLModel is the ONLY ORM.
• Each task MUST be associated with a user_id.
• Database schema must match the written schema spec exactly.
• No hidden tables, fields, or shortcuts.

────────────────────────────────────────
7. FRONTEND CONSTITUTION
────────────────────────────────────────
• Next.js App Router must be used.
• Server Components by default.
• Client Components ONLY when interactivity is required.
• All API calls must include JWT automatically.
• UI must be responsive and usable on mobile and desktop.

────────────────────────────────────────
8. SPEC-KIT COMPLIANCE
────────────────────────────────────────
• Specs are the single source of truth.
• Implementation must reference specs using:
  @specs/...
• If behavior is not defined in a spec, it must NOT be implemented.
• Specs may be updated ONLY if requirements change.

────────────────────────────────────────
9. EVALUATION ALIGNMENT
────────────────────────────────────────
This constitution exists to ensure:
• Clear audit trail of decisions
• Reproducible AI-driven development
• Fair hackathon evaluation
• No ambiguity between Phase I and Phase II

────────────────────────────────────────
10. FINAL DIRECTIVE
────────────────────────────────────────
Gemini must always:
• Read the constitution first
• Then read relevant specs
• Then generate plans and tasks
• Then implement ONLY what is specified

Any deviation from this constitution is considered a failure of Phase II compliance.

## Response snapshot

Updated the project constitution to version 3.0.0 for Hackathon Phase II.

## Outcome

- ✅ Impact: Medium - Updated the core principles of the project.
- 🧪 Tests: N/A
- 📁 Files: 1 file updated
- 🔁 Next prompts: N/A
- 🧠 Reflection: The constitution was updated successfully.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (if applicable): N/A
