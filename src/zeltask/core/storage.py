"""JSON file storage management."""

import json
from pathlib import Path
from typing import List, Dict, Any
from zelutil.utils.state import resolve_state_dir

class TaskStorage:
    def __init__(self):
        self.base_path = resolve_state_dir() / "task"
        self.base_path.mkdir(parents=True, exist_ok=True)
        
    def load_active_tasks(self) -> List[Dict[str, Any]]:
        """Load active tasks from JSON."""
        file_path = self.base_path / "active.json"
        if not file_path.exists():
            return []
        with open(file_path) as f:
            data = json.load(f)
            return data.get("tasks", [])
    
    def save_active_tasks(self, tasks: List[Dict[str, Any]]) -> None:
        """Save active tasks to JSON."""
        file_path = self.base_path / "active.json"
        with open(file_path, 'w') as f:
            json.dump({"tasks": tasks}, f, indent=2)
    
    def load_blueprints(self) -> List[Dict[str, Any]]:
        """Load blueprint templates."""
        file_path = self.base_path / "blueprint.json"
        if not file_path.exists():
            return []
        with open(file_path) as f:
            data = json.load(f)
            return data.get("templates", [])
    
    def save_blueprints(self, blueprints: List[Dict[str, Any]]) -> None:
        """Save blueprint templates."""
        file_path = self.base_path / "blueprint.json"
        with open(file_path, 'w') as f:
            json.dump({"templates": blueprints}, f, indent=2)
    
    def archive_task(self, task: Dict[str, Any]) -> None:
        """Move task to completed archive."""
        file_path = self.base_path / "completed.json"
        completed = []
        if file_path.exists():
            with open(file_path) as f:
                data = json.load(f)
                completed = data.get("completed_tasks", [])
        
        completed.append(task)
        with open(file_path, 'w') as f:
            json.dump({"completed_tasks": completed}, f, indent=2)