# Authentication

## Signup & Login Behavior
- A new user can sign up with a username and password.
- An existing user can log in with their username and password.
- Upon successful login, the user is issued a JWT token.

## JWT Lifecycle
- **Issuance:** A JWT token is issued by Better Auth on the Next.js frontend after a user successfully logs in.
- **Transmission:** The JWT token is sent from the frontend to the backend in the `Authorization` header of every API request to a protected endpoint.
- **Validation:** The backend validates the JWT token's signature using a shared secret.
- **Expiration:** JWT tokens should have a reasonable expiration time. The frontend should handle token expiration and prompt the user to log in again.

## Token Validation Rules
- The backend must verify the JWT's signature.
- The backend must check if the token has expired.
- The backend must extract the user's identity (e.g., user ID) from the token's payload.

## Security Constraints
- Passwords must be hashed before being stored in the database.
- The JWT secret key must be kept confidential and not exposed to the frontend.
- The application should be protected against common security vulnerabilities, such as Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF).

## Failure & Error Scenarios
- If a user tries to log in with invalid credentials, the API should return a 401 Unauthorized error.
- If a user tries to access a protected endpoint with a missing or invalid JWT token, the API should return a 401 Unauthorized error.
- If a user's JWT token is expired, the API should return a 401 Unauthorized error.
