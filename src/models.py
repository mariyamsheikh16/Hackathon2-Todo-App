from dataclasses import dataclass

@dataclass
class Task:
    """Represents a single to-do item."""
    id: int
    title: str
    description: str = ""
    completed: bool = False
