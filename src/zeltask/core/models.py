"""Task data models and structures."""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class SubTask:
    id: str
    title: str
    completed: Optional[str] = None

@dataclass
class Task:
    id: str
    title: str
    description: str
    type: str  # "manual" or "recurring"
    priority: str
    created: str
    category: Optional[str] = None
    due: Optional[str] = None
    tags: List[str] = None
    sub_tasks: List[SubTask] = None
    recur_id: Optional[str] = None
    recur_date: Optional[str] = None
    completed: Optional[str] = None

@dataclass
class Blueprint:
    id: str
    title: str
    description: str
    type: str  # "recurring" or "manual"
    priority: str
    category: Optional[str] = None
    tags: List[str] = None
    schedule: Optional[str] = None  # "daily", "weekly"
    time: Optional[str] = None
    day: Optional[str] = None
    started: Optional[str] = None