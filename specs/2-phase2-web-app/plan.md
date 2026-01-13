# Implementation Plan: Phase II Web App

This document outlines the execution plan for transforming the Phase I Todo Console Application into a Full-Stack Web Application.

## 1️⃣ Project Setup Plan
- **Repository Structure:**
    - `/app`: Next.js frontend application.
    - `/api`: FastAPI backend application.
    - `/specs`: Feature specifications.
- **Environment Configuration:**
    - Create `.env` files for both frontend and backend to manage environment variables (e.g., database connection string, JWT secret).
- **Frontend / Backend Separation:**
    - The frontend and backend will be developed and deployed as separate services.
    - The Next.js app will be responsible for all UI rendering.
    - The FastAPI app will expose a RESTful API.

## 2️⃣ Backend Implementation Plan
- **Database Schema Setup:**
    - Define `User` and `Todo` models using SQLModel.
    - The `User` model will include `id`, `username`, and `hashed_password`.
    - The `Todo` model will include `id`, `title`, `description`, `completed`, and a `user_id` foreign key.
- **Authentication Middleware:**
    - Implement a middleware in FastAPI to verify JWT tokens on protected endpoints.
    - The middleware will extract the `user_id` from the token payload and make it available in the request.
- **API Route Design:**
    - `/api/auth/signup`: Create a new user.
    - `/api/auth/login`: Authenticate a user and return a JWT token.
    - `/api/todos/`:
        - `GET`: Get all todos for the authenticated user.
        - `POST`: Create a new todo for the authenticated user.
    - `/api/todos/{todo_id}`:
        - `GET`: Get a specific todo by ID.
        - `PUT`: Update a specific todo by ID.
        - `DELETE`: Delete a specific todo by ID.
- **Validation & Error Handling:**
    - Use Pydantic models for request and response validation.
    - Implement custom exception handlers to return appropriate HTTP status codes and error messages.

## 3️⃣ Frontend Implementation Plan
- **App Router Structure:**
    - `(auth)` group for authentication pages (`/login`, `/signup`).
    - `(main)` group for the main application pages (`/`).
- **Auth Flows:**
    - Create signup and login forms.
    - Upon successful login, store the JWT token securely (e.g., in an HttpOnly cookie or local storage).
    - Implement a mechanism to automatically include the JWT token in all API requests.
- **Protected Routes & Session Handling:**
    - Create a higher-order component (HOC) or middleware to protect routes that require authentication.
    - If a user is not authenticated, they should be redirected to the login page.
    - Handle JWT token expiration and prompt the user to log in again.
- **Todo CRUD UI Flow:**
    - Create a main page to display the user's todo list.
    - Implement UI components for creating, updating, and deleting todos.
    - The UI should reflect the real-time state of the user's todos.

## 4️⃣ Integration Plan
- **Frontend ↔ Backend Communication:**
    - The frontend will use `fetch` or a library like `axios` to make API calls to the backend.
    - All API calls will be directed to the `/api/` endpoints of the FastAPI application.
- **Authorization Headers:**
    - The frontend will automatically attach the `Authorization: Bearer <token>` header to all protected API requests.
- **Error & Loading State Handling:**
    - The frontend will display loading indicators while waiting for API responses.
    - The frontend will display user-friendly error messages when API calls fail.

## 5️⃣ Security & Access Control Plan
- **User Isolation Strategy:**
    - All API endpoints for accessing user-specific data will be protected.
    - The backend will use the `user_id` from the JWT token to filter database queries and ensure that users can only access their own data.
- **Token Expiration Handling:**
    - The frontend will handle token expiration by redirecting the user to the login page.
    - The backend will reject requests with expired tokens.
- **Unauthorized Access Behavior:**
    - If a user tries to access a protected resource without a valid JWT token, the API will return a 401 Unauthorized error.
    - If a user tries to access another user's data, the API will return a 403 Forbidden error.

## 6️⃣ Testing & Verification Plan
- **API Testing Approach:**
    - Use `pytest` to write unit and integration tests for the FastAPI backend.
    - Test all API endpoints, including success cases, error cases, and authentication/authorization.
- **Auth Flow Verification:**
    - Write tests to verify the signup, login, and token validation flows.
- **CRUD Validation Checks:**
    - Write tests to verify the validation rules for creating and updating todos.
