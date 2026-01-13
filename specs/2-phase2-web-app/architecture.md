# Architecture

## High-Level System Architecture
The system is composed of three main components:
1.  **Frontend:** A Next.js single-page application (SPA) that provides the user interface.
2.  **Backend:** A Python FastAPI application that serves as the API layer.
3.  **Database:** A Neon Serverless PostgreSQL database for data persistence.

## Frontend ↔ Backend ↔ Database Flow
1.  The user interacts with the Next.js frontend in their browser.
2.  The frontend makes API calls to the FastAPI backend.
3.  The backend processes the requests, interacts with the PostgreSQL database using SQLModel as the ORM, and returns the response to the frontend.
4.  All communication between the frontend and backend is done via a RESTful API, and data is exchanged in JSON format.

## Authentication Flow using JWT
1.  The user signs up or logs in through the Next.js frontend.
2.  The frontend sends the user's credentials to the backend.
3.  The backend verifies the credentials and, if successful, generates a JWT token. The token is issued by Better Auth running on the Next.js frontend.
4.  The JWT token is sent back to the frontend and stored securely.
5.  For subsequent requests to protected API endpoints, the frontend includes the JWT token in the `Authorization` header as a Bearer token.
6.  The FastAPI backend verifies the JWT token's signature using a shared secret.
7.  If the token is valid, the backend extracts the authenticated user's identity from the token and processes the request.
8.  If the token is invalid or missing, the backend rejects the request with a 401 Unauthorized status code.

## Separation of Concerns
-   **Frontend (Next.js):** Responsible for UI, client-side routing, and state management. It communicates with the backend via API calls.
-   **Backend (FastAPI):** Responsible for business logic, API endpoints, authentication, and database interactions. It is completely decoupled from the frontend.
-   **Database (PostgreSQL):** Responsible for data storage and retrieval.
-   **Authentication (Better Auth):** The Better Auth service runs on the Next.js frontend and is responsible for issuing JWT tokens. The backend is responsible for validating the tokens.
