# Task CRUD

## User Stories
- As a logged-in user, I want to create a new task so that I can keep track of what I need to do.
- As a logged-in user, I want to see a list of all my tasks so that I can see what I need to do.
- As a logged-in user, I want to update an existing task so that I can change its details or mark it as complete.
- As a logged-in user, I want to delete a task so that I can remove it from my list.

## CRUD Operations
- **Create:** A logged-in user can create a new task with a title and a description.
- **Read:** A logged-in user can retrieve a list of all their tasks.
- **Update:** A logged-in user can update the title, description, and completion status of their own tasks.
- **Delete:** A logged-in user can delete their own tasks.

## Acceptance Criteria
- A user must be logged in to perform any CRUD operation on tasks.
- A user can only view, update, or delete their own tasks.
- The API must return a 401 Unauthorized error if a user is not logged in.
- The API must return a 403 Forbidden error if a user tries to access another user's tasks.
- When a new task is created, it should be marked as not completed by default.

## Validation Rules
- The `title` of a task is required and cannot be empty.
- The `description` of a task is optional.
- The `completed` status of a task must be a boolean value.

## User Ownership Enforcement
- Each task in the database must be associated with a `user_id`.
- All API endpoints for task CRUD operations must be protected and require authentication.
- When fetching, updating, or deleting a task, the backend must ensure that the `user_id` of the task matches the `user_id` of the authenticated user.
