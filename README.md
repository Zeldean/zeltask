# zeltask

Task management CLI tool with blueprint templates and recurring task automation.

## Features

- **Blueprint System**: Create reusable task templates (recurring + manual)
- **Categories & Tags**: Organize tasks with flexible labeling
- **Recurring Tasks**: Auto-generate tasks based on schedules
- **Sub-tasks**: Break down complex tasks into smaller items
- **Task Completion**: Mark tasks and sub-tasks as done
- **Active Management**: Focus on current tasks, archive completed ones

## Installation

```bash
pip install -e .
```

## Core Concepts

### Task Types
- **Manual**: One-time tasks created on demand
- **Recurring**: Auto-generated from blueprint schedules

### Data Structure
- `~/.local/state/zel/task/active.json` - Current tasks
- `~/.local/state/zel/task/completed.json` - Finished tasks archive
- `~/.local/state/zel/task/blueprint.json` - Task templates

### Task States
- **Active**: Needs to be done
- **Completed**: Marked as finished with timestamp
- **Sub-tasks**: Nested items within main tasks

## Usage Overview

### Setup & Management
```bash
# Setup categories and tags
zeltask category create "Work" "Personal" "Study"
zeltask tag create "urgent" "bug" "review" "planning"

# Create blueprint templates
zeltask blueprint create recurring "Daily Standup" --schedule daily --time "09:00"
zeltask blueprint create manual "Code Review Template" --priority medium

# List blueprints
zeltask blueprint list
```

### Task Operations
```bash
# Create tasks
zeltask create "Fix login bug" --priority high --tags "bug,urgent"
zeltask create from-blueprint "code_review_template" "Review PR #123"

# List and filter tasks
zeltask list
zeltask list --priority high
zeltask list --tags "urgent"
zeltask list --category "Work"

# Task completion
zeltask complete <task_id>
zeltask complete <task_id> --subtask <subtask_id>

# Add sub-tasks
zeltask subtask add <task_id> "Write unit tests"
```

### Recurring Task Management
```bash
# Trigger recurring task generation
zeltask recurring generate

# View recurring schedules
zeltask recurring list

# Disable/enable recurring tasks
zeltask recurring disable <blueprint_id>
zeltask recurring enable <blueprint_id>
```

### Display & Filtering
```bash
# Show active tasks
zeltask show
zeltask show --today
zeltask show --overdue

# Archive management
zeltask archive list
zeltask archive restore <task_id>
```

## Task Structure

### Active Task Example
```json
{
  "id": "task_001",
  "title": "Review project documentation", 
  "description": "Update README and installation steps",
  "type": "manual",
  "priority": "high",
  "created": "2024-01-15T10:30:00Z",
  "due": "2024-01-16T17:00:00Z",
  "category": "Work",
  "tags": ["documentation", "urgent"],
  "sub_tasks": [
    {
      "id": "sub_001",
      "title": "Check installation commands",
      "completed": "2024-01-15T11:00:00Z"
    }
  ]
}
```

### Blueprint Template Example
```json
{
  "id": "daily_standup",
  "title": "Daily standup prep",
  "description": "Prepare updates for team standup", 
  "type": "recurring",
  "priority": "low",
  "schedule": "daily",
  "time": "09:00",
  "started": "2024-01-08",
  "category": "Work",
  "tags": ["standup", "team"]
}
```

## Workflow

1. **Setup**: Create categories, tags, and blueprint templates
2. **Daily Use**: 
   - Run `zeltask recurring generate` to create scheduled tasks
   - Use `zeltask list` to see what needs doing
   - Complete tasks with `zeltask complete`
3. **Management**: Create ad-hoc tasks, manage blueprints, review archives

## Integration

Part of the Zel productivity suite:
- **zeltimer**: Time tracking with session management
- **zeltask**: Task management with recurring automation
- **zeljournal**: Daily notes and reflection
- **zelutil**: Shared configuration and utilities

All tools use standardized `~/.local/state/zel/` data structure for cross-tool integration and daily summary generation.