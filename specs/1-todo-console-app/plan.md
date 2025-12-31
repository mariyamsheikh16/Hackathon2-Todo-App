# Implementation Plan: Phase 1 In-Memory Todo Application

**Branch**: `1-todo-console-app` | **Date**: 2026-01-01 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/1-todo-console-app/spec.md`

## Summary

This plan outlines the design for a Phase 1 in-memory Todo Console Application in Python. It follows a clean architecture with a clear separation of concerns between models, services, and the command-line interface, adhering strictly to the project constitution and feature specification.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python Standard Library only)
**Storage**: In-memory Python list or dictionary
**Testing**: N/A for Phase 1 plan
**Target Platform**: Console / Command-Line Interface
**Project Type**: Single project
**Performance Goals**: N/A for Phase 1
**Constraints**: Must run entirely in memory; state is lost on exit.
**Scale/Scope**: Single user, single session.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Strict Spec-Driven Development**: The plan is derived directly from the `spec.md`.
- [x] **II. Clean, Maintainable Python**: The proposed structure promotes clean, minimal, and readable code.
- [x] **III. Clean Architecture**: The plan explicitly enforces separation of concerns (Models, Service, CLI).
- [x] **IV. In-Memory Data Store**: The plan specifies an in-memory list/dictionary for storage, with no persistence.
- [x] **V. Deterministic and Testable Logic**: The service layer is designed to contain all business logic, making it deterministic and testable.
- [x] **VI. Graceful Error Handling**: The plan designates the CLI and Service layers to handle errors gracefully.
- [x] **VII. No Unsolicited Features**: The plan's scope is strictly limited to the features defined in `spec.md`.
- [x] **VIII. Simplicity and Clarity**: The architecture is minimal and avoids unnecessary complexity.
- [x] **IX. Unstructured Code Prohibited**: The file structure provides a clear and organized foundation for the code.

**Result**: All constitutional gates pass.

## Project Structure

### Documentation (this feature)

```text
specs/1-todo-console-app/
├── plan.md              # This file
├── research.md          # Confirms no external research needed
├── data-model.md        # Defines the Task entity
├── quickstart.md        # Explains how to run the application
├── contracts/           # Empty; no API contracts for this CLI app
└── tasks.md             # To be created by /sp.tasks command
```

### Source Code (repository root)

The project will use a single `src` directory with a clean separation of concerns.

```text
src/
├── models.py        # Contains the Task data model (e.g., a dataclass).
├── todo_service.py  # Manages all business logic and the in-memory task list.
├── cli.py           # Handles all user interaction (menus, input, output).
└── main.py          # Application entry point; wires components and runs the main loop.
```

**Structure Decision**: The 'Single project' structure is adopted. It is simple, clean, and perfectly suited for this small-scale console application, directly reflecting the "Clean Architecture" principle from the constitution.

## Application Flow Plan

1.  **Startup**:
    - The user executes `python src/main.py`.
    - `main.py` initializes the `TodoService`.
    - `main.py` starts the main application loop located in `cli.py`.
2.  **Main Loop**:
    - `cli.py` clears the screen and displays the main menu of options (e.g., "1. Add Task", "2. View Tasks", etc.).
    - `cli.py` prompts the user for a numeric choice.
3.  **User Action**:
    - The user enters a number corresponding to an action.
    - `cli.py` captures the input and calls the appropriate function.
    - The function in `cli.py` gathers any additional required input from the user (e.g., task title).
    - The `cli.py` function then calls the relevant method on the `TodoService` instance, passing the user data.
    - `todo_service.py` performs the business logic (e.g., adds the task to its internal list).
    - Control returns to `cli.py`, which displays a success or error message.
    - The main loop repeats.
4.  **Exit**:
    - The user selects the "Exit" option from the menu.
    - The main loop terminates, and the program exits safely.

## Error Handling Plan

- **Invalid Menu Input**: If the user enters non-numeric or out-of-range text at the main menu, `cli.py` will catch this, display an error message (e.g., "Invalid option, please try again."), and re-display the menu.
- **Missing Task ID**: If the user provides an ID for an update, delete, or toggle operation that does not exist in the `TodoService`'s list, the service will signal this failure (e.g., return `False` or `None`). `cli.py` will then display an appropriate error message (e.g., "Error: Task with ID [id] not found.").
- **Invalid Task Data**: If the user tries to create a task with an empty title, `cli.py` will validate this before calling the service and prompt the user again.

## In-Memory Data Plan

- **Storage**: A simple Python `list` will be used to store `Task` objects. This list will be a private member of the `TodoService` class.
- **ID Generation**: A private integer counter, also a member of the `TodoService` class, will be used to generate unique task IDs. It will be initialized to `0` and incremented by `1` every time a new task is successfully created.