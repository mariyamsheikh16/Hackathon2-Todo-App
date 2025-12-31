# Data Model: Phase 1 In-Memory Todo Application

This document defines the data entities for the project, as derived from the feature specification.

## Entity: Task

Represents a single to-do item in the application.

### Attributes

| Attribute     | Type    | Constraints                               | Description                                     |
|---------------|---------|-------------------------------------------|-------------------------------------------------|
| `id`          | Integer | Required, Unique, Auto-incremented        | The unique identifier for the task.             |
| `title`       | String  | Required, Non-empty                       | The main title or name of the task.             |
| `description` | String  | Optional                                  | A more detailed description of the task.        |
| `completed`   | Boolean | Required, Default: `False`                | The completion status of the task.              |

### State Transitions

- A `Task` is created with `completed` as `False`.
- The `completed` status can be toggled between `True` and `False`.
- The `title` and `description` can be updated after creation.
- A `Task` object is destroyed when deleted by the user or when the application session ends.

### Example Representation (Python `dataclass`)

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
```
