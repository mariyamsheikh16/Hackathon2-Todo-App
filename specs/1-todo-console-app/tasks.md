# Tasks: Phase 1 In-Memory Todo Application

**Input**: Design documents from `specs/1-todo-console-app/`
**Prerequisites**: plan.md, spec.md, data-model.md

## Phase 1: Setup (Shared Infrastructure)
**Purpose**: Create the empty Python files for the project structure.

- [x] T001 [P] Create empty file `src/models.py`
- [x] T002 [P] Create empty file `src/todo_service.py`
- [x] T003 [P] Create empty file `src/cli.py`
- [x] T004 [P] Create empty file `src/main.py`

---
## Phase 2: Foundational (Blocking Prerequisites)
**Purpose**: Implement the core data model.
**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T005 Implement the `Task` data class in `src/models.py` per the data-model.md specification.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---
## Phase 3: User Story 1 & 2 - Add and View Tasks (Priority: P1) 🎯 MVP
**Goal**: Allow users to create tasks and see their list.
**Independent Test**: A user can start the app, add multiple tasks, and see them listed correctly.

### Implementation for User Stories 1 & 2
- [ ] T006 [US1] In `src/todo_service.py`, implement the `TodoService` class with an in-memory list for storing tasks and a counter for task IDs.
- [ ] T007 [US1] In `src/todo_service.py`, implement the `add_task(title: str, description: str)` method. It should create a new `Task` object and add it to the list.
- [ ] T008 [US2] In `src/todo_service.py`, implement the `get_all_tasks()` method. It should return the full list of tasks.
- [ ] T009 [US1] In `src/cli.py`, implement the `add_task_ui()` function that prompts the user for a title and description and calls the service.
- [ ] T010 [US2] In `src/cli.py`, implement the `view_tasks_ui()` function that gets all tasks from the service and prints them in a user-friendly format, including the `[ ]` status indicator.
- [ ] T011 [US1, US2] In `src/cli.py`, create a main menu loop that displays options for "Add Task", "View Tasks", and "Exit".

**Checkpoint**: At this point, a user can add and view tasks for a single session. This is the MVP.

---
## Phase 4: User Story 5 - Toggle Task Completion (Priority: P1)
**Goal**: Allow users to mark a task as complete or incomplete.
**Independent Test**: A user can add a task, view it as incomplete `[ ]`, toggle its status, and then view it as complete `[✓]`.

### Implementation for User Story 5
- [ ] T012 [US5] In `src/todo_service.py`, implement the `toggle_task_completion(task_id: int)` method. It should find the task by ID and flip its `completed` status. Handle cases where the ID is not found.
- [ ] T013 [US5] In `src/cli.py`, implement the `toggle_task_ui()` function that prompts the user for a task ID and calls the service.
- [ ] T014 [US5] In `src/cli.py`, add the "Toggle Task Status" option to the main menu loop.

**Checkpoint**: Users can now change the completion status of tasks.

---
## Phase 5: User Story 3 - Update a Task (Priority: P2)
**Goal**: Allow users to edit the title and description of a task.
**Independent Test**: A user can add a task, update its title, and verify the change by viewing the task list.

### Implementation for User Story 3
- [ ] T015 [US3] In `src/todo_service.py`, implement the `update_task(task_id: int, title: str, description: str)` method. It should find the task by ID and update its details. Handle cases where the ID is not found.
- [ ] T016 [US3] In `src/cli.py`, implement the `update_task_ui()` function that prompts for an ID and the new details, then calls the service.
- [ ] T017 [US3] In `src/cli.py`, add the "Update Task" option to the main menu loop.

**Checkpoint**: Users can now edit existing tasks.

---
## Phase 6: User Story 4 - Delete a Task (Priority: P2)
**Goal**: Allow users to remove a task from their list.
**Independent Test**: A user can add a task, delete it, and verify it no longer appears in the list.

### Implementation for User Story 4
- [ ] T018 [US4] In `src/todo_service.py`, implement the `delete_task(task_id: int)` method. It should remove the task with the given ID. Handle cases where the ID is not found.
- [ ] T019 [US4] In `src/cli.py`, implement the `delete_task_ui()` function that prompts for an ID and calls the service.
- [ ] T020 [US4] In `src/cli.py`, add the "Delete Task" option to the main menu loop.

**Checkpoint**: Users can now delete tasks.

---
## Phase 7: Polish & Cross-Cutting Concerns
**Purpose**: Finalize the application entry point and ensure a smooth user experience.

- [ ] T021 In `src/main.py`, write the main application entry point logic that initializes the `TodoService`, passes it to the CLI functions, and starts the main menu loop from `cli.py`.
- [ ] T022 In `src/cli.py`, implement robust error handling for invalid (non-numeric) user input in the main menu.
- [ ] T023 Review all UI functions in `src/cli.py` to ensure user-friendly success and error messages are displayed for all operations.

---
## Dependencies & Execution Order
- **Phase 1 (Setup)** must be completed first.
- **Phase 2 (Foundational)** depends on Phase 1.
- **Phase 3 (Add/View)** depends on Phase 2.
- **Phases 4, 5, and 6** all depend on Phase 3, but can be implemented in any order relative to each other.
- **Phase 7 (Polish)** depends on all previous phases and should be done last.

## Implementation Strategy
### MVP First (P1 User Stories)
1. Complete Phase 1 (Setup)
2. Complete Phase 2 (Foundational)
3. Complete Phase 3 (Add/View Tasks)
4. **STOP and VALIDATE**: At this point, the core MVP is functional.
5. Complete Phase 4 (Toggle Completion)
6. **STOP and VALIDATE**: All P1 stories are now complete.

### Incremental Delivery
After the MVP is validated, proceed to implement Phase 5 (Update) and Phase 6 (Delete). Finalize the application with Phase 7 (Polish).
