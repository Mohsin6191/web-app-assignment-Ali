# src/storage.py
import json
import os
from typing import List, Dict, Any


def ensure_data_file(file_path: str) -> None:
    """Create the JSON file (and parent folder) if it doesn't exist."""
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_tasks(file_path: str) -> List[Dict[str, Any]]:
    """Load tasks from JSON. Returns an empty list if file is missing/invalid."""
    ensure_data_file(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []
        return data

    except json.JSONDecodeError:
        # If JSON is broken, don't crash — return empty list
        return []
    except OSError:
        return []


def save_tasks(file_path: str, tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to JSON (pretty printed)."""
    ensure_data_file(file_path)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
