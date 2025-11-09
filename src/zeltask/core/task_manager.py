"""Core task management logic."""

from datetime import datetime
from typing import List, Optional
from .storage import TaskStorage
from .models import Task, Blueprint

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()
    
    def create_task(self, title: str, description: str = "", 
                   priority: str = "medium", category: str = None,
                   tags: List[str] = None) -> str:
        """Create a new manual task."""
        tasks = self.storage.load_active_tasks()
        task_id = f"task_{len(tasks) + 1:03d}"
        
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "type": "manual",
            "priority": priority,
            "created": datetime.now().isoformat(),
            "category": category,
            "tags": tags or [],
            "sub_tasks": []
        }
        
        tasks.append(new_task)
        self.storage.save_active_tasks(tasks)
        return task_id
    
    def complete_task(self, task_id: str) -> bool:
        """Mark task as completed and archive it."""
        tasks = self.storage.load_active_tasks()
        
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                task["completed"] = datetime.now().isoformat()
                self.storage.archive_task(task)
                tasks.pop(i)
                self.storage.save_active_tasks(tasks)
                return True
        return False
    
    def list_active_tasks(self) -> List[dict]:
        """Get all active tasks."""
        return self.storage.load_active_tasks()
    
    def create_blueprint(self, blueprint_id: str, title: str, 
                        blueprint_type: str, **kwargs) -> None:
        """Create a new blueprint template."""
        blueprints = self.storage.load_blueprints()
        
        new_blueprint = {
            "id": blueprint_id,
            "title": title,
            "type": blueprint_type,
            **kwargs
        }
        
        blueprints.append(new_blueprint)
        self.storage.save_blueprints(blueprints)