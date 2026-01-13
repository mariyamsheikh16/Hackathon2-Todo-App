# Tasks for Phase II Web App

This document outlines the detailed tasks for implementing the Phase II Web Application, derived from the approved specifications and plan.

## Dependencies

The completion order for user stories is:
- US1 (User Authentication) must be completed before US2 (Todo CRUD).

## Phase 1: Project Setup Tasks

- [ ] T001 Project Setup - Initialize Next.js frontend application in `/app` directory.
- [ ] T002 Project Setup - Initialize FastAPI backend application in `/api` directory.
- [ ] T003 Project Setup - Create `.env` files for frontend (`/app/.env.local`) and backend (`/api/.env`) to manage environment variables (e.g., database connection string, JWT secret).
- [ ] T004 Project Setup - Configure frontend (`/app/next.config.js`) and backend (`/api/main.py` or similar) to recognize each other's service locations.

## Phase 2: Foundational Tasks

- [ ] T005 Database & Models - Define `User` model using SQLModel in `/api/models/user.py`. This model should include `id`, `username`, `hashed_password`.
- [ ] T006 Database & Models - Define `Todo` model using SQLModel in `/api/models/todo.py`. This model should include `id`, `title`, `description`, `completed`, and a `user_id` foreign key.
- [ ] T007 Backend - Implement initial database connection and session management (FastAPI dependencies) in `/api/database.py`.
- [ ] T008 Backend - Implement password hashing utility in `/api/utils/auth.py`.

## Phase 3: User Authentication [US1]

- [ ] T009 [US1] Backend - Implement User Signup API endpoint `/api/auth/signup` in `/api/routers/auth.py`. This endpoint should handle user creation and password hashing.
- [ ] T010 [US1] Backend - Implement User Login API endpoint `/api/auth/login` in `/api/routers/auth.py`. This endpoint should verify credentials and return a JWT token.
- [ ] T011 [US1] Backend - Implement JWT authentication middleware for FastAPI in `/api/dependencies.py` to verify tokens on protected routes.
- [ ] T012 [US1] Frontend - Setup basic Next.js App Router structure with `(auth)` group for authentication pages (`/app/app/(auth)/login/page.tsx`, `/app/app/(auth)/signup/page.tsx`).
- [ ] T013 [US1] Frontend - Create Signup UI components and integrate with `/api/auth/signup` endpoint in `/app/components/SignupForm.tsx`.
- [ ] T014 [US1] Frontend - Create Login UI components and integrate with `/api/auth/login` endpoint in `/app/components/LoginForm.tsx`.
- [ ] T015 [US1] Frontend - Implement Auth Context/State Management to store and provide JWT token across the application in `/app/context/AuthContext.tsx`.
- [ ] T016 [US1] Frontend - Handle JWT storage securely (e.g., in HttpOnly cookie or local storage) and automatic inclusion in API requests.

## Phase 4: Todo CRUD [US2]

- [ ] T017 [US2] Backend - Implement Get All Todos API endpoint `/api/todos/` (GET) in `/api/routers/todos.py`. This endpoint must filter by authenticated user.
- [ ] T018 [US2] Backend - Implement Create Todo API endpoint `/api/todos/` (POST) in `/api/routers/todos.py`. This endpoint must associate the new todo with the authenticated user.
- [ ] T019 [US2] Backend - Implement Get Todo by ID API endpoint `/api/todos/{todo_id}` (GET) in `/api/routers/todos.py`. This endpoint must ensure user ownership.
- [ ] T020 [US2] Backend - Implement Update Todo API endpoint `/api/todos/{todo_id}` (PUT) in `/api/routers/todos.py`. This endpoint must ensure user ownership.
- [ ] T021 [US2] Backend - Implement Delete Todo API endpoint `/api/todos/{todo_id}` (DELETE) in `/api/routers/todos.py`. This endpoint must ensure user ownership.
- [ ] T022 [US2] Frontend - Create Todo List UI components to display todos in `/app/components/TodoList.tsx`.
- [ ] T023 [US2] Frontend - Implement Add Todo functionality with UI and API integration in `/app/components/AddTodoForm.tsx`.
- [ ] T024 [US2] Frontend - Implement Edit Todo functionality with UI and API integration in `/app/components/EditTodoForm.tsx`.
- [ ] T025 [US2] Frontend - Implement Delete Todo functionality with UI and API integration in `/app/components/TodoItem.tsx`.

## Phase 5: Integration Tasks

- [ ] T026 Integrate Frontend API Calls with Backend (Authentication) - Ensure all protected API calls from frontend correctly send JWT.
- [ ] T027 Implement Global Error and Loading State Handling in Frontend - Display loading indicators and user-friendly error messages for all API interactions.

## Phase 6: Security & Access Control Tasks

- [ ] T028 Backend - Refine User Isolation: Ensure all database queries related to todos explicitly filter by the authenticated `user_id` to prevent data leakage.
- [ ] T029 Frontend - Implement Protected Routes and Redirects: Secure frontend routes, redirecting unauthenticated users to the login page.
- [ ] T030 Frontend - Handle JWT Token Expiration: Automatically redirect users to login upon token expiration.

## Phase 7: Testing & Verification Tasks

- [ ] T031 Backend - Write Unit and Integration Tests for Authentication APIs (signup, login, JWT validation) in `/api/tests/test_auth.py`.
- [ ] T032 Backend - Write Unit and Integration Tests for Todo CRUD APIs (all operations) in `/api/tests/test_todos.py`.
- [ ] T033 Frontend - Implement Basic UI Tests for Auth Flows (signup, login, logout) using a testing framework like Playwright or Cypress in `/app/tests/e2e/auth.spec.ts`.
- [ ] T034 Frontend - Implement Basic UI Tests for Todo CRUD (add, view, edit, delete) using a testing framework like Playwright or Cypress in `/app/tests/e2e/todos.spec.ts`.
