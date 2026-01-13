---
id: 1
title: Specify Phase II Web App
stage: spec
date: 2026-01-14
surface: agent
model: gemini
feature: 2-phase2-web-app
branch: 2-phase2-web-app
user: {{USER}}
command: /sp.specify
labels: [spec, hackathon-phase-2]
links:
  spec: specs/2-phase2-web-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-phase2-web-app/overview.md
- specs/2-phase2-web-app/architecture.md
- specs/2-phase2-web-app/features/task-crud.md
- specs/2-phase2-web-app/features/authentication.md
- specs/2-phase2-web-app/spec.md
- specs/2-phase2-web-app/checklists/requirements.md
tests:
  - 
---

## Prompt

You are an expert AI Product Architect and Spec-Driven Engineer. You are working on Hackathon II – Phase II. Phase I (Console-based Todo App) is already completed. Your task is to ENTER THE “SPECIFY” STAGE of the Agentic Dev Stack. ──────────────────────────────────────── PROJECT CONTEXT ──────────────────────────────────────── The goal is to transform an existing console-based Todo application into a modern, multi-user, full-stack web application. Technology stack is STRICT and NON-NEGOTIABLE: • Frontend: Next.js 16+ (App Router) • Backend: Python FastAPI • ORM: SQLModel • Database: Neon Serverless PostgreSQL • Authentication: Better Auth (JWT-based) • Spec System: Spec-Kit Plus • Implementation AI: Gemini • No manual coding allowed ──────────────────────────────────────── WHAT YOU MUST DO (SPECIFY PHASE) ──────────────────────────────────────── Create clear, professional, Spec-Kit compatible SPECIFICATIONS for Phase II. You MUST generate the following specification files ONLY (no implementation, no code): 1. overview.md 2. architecture.md 3. features/task-crud.md 4. features/authentication.md Each spec must be: • Written in clean, professional markdown • Explicit, unambiguous, and implementation-ready • Suitable for direct use by an AI coding agent • Aligned strictly with hackathon Phase II requirements ──────────────────────────────────────── SCOPE RULES ──────────────────────────────────────── INCLUDE: ✓ Multi-user Todo CRUD ✓ REST API behavior ✓ JWT-based authentication flow ✓ User-level data isolation ✓ Persistent storage with Neon DB ✓ Frontend–Backend interaction EXCLUDE: ✗ Chatbot ✗ AI assistants ✗ Advanced automation ✗ Any Phase III functionality ✗ Any feature not explicitly required ──────────────────────────────────────── AUTHENTICATION RULES (MANDATORY) ──────────────────────────────────────── • Better Auth runs ONLY on the Next.js frontend • JWT tokens must be issued after login • JWT must be sent in: Authorization: Bearer <token> • FastAPI backend must: - Verify JWT using shared secret - Extract authenticated user - Enforce user-based access control • Every API endpoint requires authentication • No unauthenticated access is allowed ──────────────────────────────────────── SPEC CONTENT REQUIREMENTS ──────────────────────────────────────── 1️⃣ overview.md must include: • Project purpose • Phase II goals • Tech stack summary • Feature list (Phase II only) 2️⃣ architecture.md must include: • High-level system architecture • Frontend ↔ Backend ↔ Database flow • Authentication flow using JWT • Clear separation of concerns 3️⃣ features/task-crud.md must include: • User stories • CRUD operations • Acceptance criteria • Validation rules • User ownership enforcement 4️⃣ features/authentication.md must include: • Signup & login behavior • JWT lifecycle • Token validation rules • Security constraints • Failure & error scenarios ──────────────────────────────────────── OUTPUT FORMAT ──────────────────────────────────────── • Output each spec as a SEPARATE markdown document • Clearly label each file with its filename as a header • Do NOT generate code • Do NOT generate plans or tasks yet ──────────────────────────────────────── FINAL INSTRUCTION ──────────────────────────────────────── This is the SPECIFY phase ONLY. Do not plan. Do not implement. Do not assume. Only define WHAT must be built — clearly, precisely, and professionally.

## Response snapshot

Created the feature specification for the Phase II Web App.

## Outcome

- ✅ Impact: High - Created the initial specification for the project.
- 🧪 Tests: N/A
- 📁 Files: 6 files created
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: The manual creation of files and directories was successful.

## Evaluation notes (flywheel)

- Failure modes observed: The PowerShell script for creating features is disabled on this system.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (if applicable): N/A
