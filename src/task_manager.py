# src/task_manager.py
from typing import List, Dict, Any, Optional
from datetime import datetime


def _next_id(tasks: List[Dict[str, Any]]) -> int:
    """Generate next task id."""
    if not tasks:
        return 1
    return max(t["id"] for t in tasks if "id" in t) + 1


def add_task(tasks: List[Dict[str, Any]], title: str, description: str = "") -> Dict[str, Any]:
    """Add a new task."""
    title = title.strip()
    description = description.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    task = {
        "id": _next_id(tasks),
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    return task


def list_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return tasks (as-is)."""
    return tasks


def find_task(tasks: List[Dict[str, Any]], task_id: int) -> Optional[Dict[str, Any]]:
    """Find a task by id."""
    for t in tasks:
        if t.get("id") == task_id:
            return t
    return None


def mark_completed(tasks: List[Dict[str, Any]], task_id: int) -> bool:
    """Mark task as completed. Returns True if success."""
    task = find_task(tasks, task_id)
    if not task:
        return False
    task["completed"] = True
    return True


def delete_task(tasks: List[Dict[str, Any]], task_id: int) -> bool:
    """Delete a task. Returns True if deleted."""
    task = find_task(tasks, task_id)
    if not task:
        return False
    tasks.remove(task)
    return True
