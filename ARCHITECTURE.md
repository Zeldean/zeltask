# Zel App Architecture Standard

## Overview
Standardized architecture for all Zel productivity apps (zeltask, zeltimer, zeljournal, etc.) ensuring consistency, maintainability, and shared functionality.

## File Structure

```
src/zel{app}/
├── __init__.py              # Package initialization
├── cli.py                   # Main CLI entry point
├── core/                    # Business logic layer
│   ├── __init__.py
│   ├── models.py           # Data structures & types
│   ├── storage.py          # Data persistence layer
│   └── {app}_manager.py    # Main business logic
└── commands/               # CLI command modules
    ├── __init__.py
    ├── {feature}_commands.py
    └── ...
```

## Layer Responsibilities

### CLI Layer (`cli.py`)
- **Purpose**: Main entry point and command routing
- **Responsibilities**:
  - Click group setup and command registration
  - High-level command orchestration
  - Quick access shortcuts (e.g., `zeltask list`)
- **Dependencies**: Commands modules only

### Commands Layer (`commands/`)
- **Purpose**: CLI command definitions and user interaction
- **Responsibilities**:
  - Click command definitions with arguments/options
  - User input validation and formatting
  - Output formatting and display
  - Calling core business logic
- **Dependencies**: Core layer, Click
- **Files**:
  - `{feature}_commands.py` - Feature-specific commands
  - Group related commands (e.g., task operations, blueprint management)

### Core Layer (`core/`)
- **Purpose**: Business logic and data management
- **Responsibilities**:
  - Application-specific business rules
  - Data validation and processing
  - Orchestrating storage operations
  - Cross-cutting concerns (recurring tasks, etc.)
- **Dependencies**: Storage, Models, zelutil
- **Files**:
  - `models.py` - Data structures, dataclasses, types
  - `storage.py` - JSON file operations, data persistence
  - `{app}_manager.py` - Main business logic coordinator

## Shared Dependencies (zelutil)

### Path Management
```python
from zelutil.utils.state import resolve_state_dir
# Always use: resolve_state_dir() / "app_name"
```

### Common Utilities
- State directory resolution
- Configuration management
- Cross-app integration helpers
- Shared data structures

## Data Storage Standard

### File Structure
```
~/.local/state/zel/
├── {app}/
│   ├── active.json      # Current/working items
│   ├── completed.json   # Archived/finished items
│   └── blueprint.json   # Templates/configurations
└── shared/              # Cross-app data
```

### JSON Structure
- **active.json**: Current working items (tasks, timers, etc.)
- **completed.json**: Historical/archived items
- **blueprint.json**: Templates and configurations

## Implementation Benefits

### For Individual Apps
- **Consistent**: Same patterns across all Zel apps
- **Maintainable**: Clear separation of concerns
- **Testable**: Business logic isolated from CLI
- **Extensible**: Easy to add new commands/features

### For Zel Ecosystem
- **Shared utilities**: Common functionality in zelutil
- **Cross-integration**: Apps can easily interact
- **Unified data**: Standardized storage enables daily summaries
- **Scalable**: New apps follow established patterns

## Implementation Guidelines

### New Zel App Checklist
1. Create standard folder structure
2. Use zelutil for paths and state management
3. Implement 3-layer architecture (CLI → Commands → Core)
4. Follow JSON storage standard (active/completed/blueprint)
5. Add to zelutil registry for cross-app integration

### Command Design
- Group related functionality (e.g., `zeltask task create`)
- Provide shortcuts for common operations (e.g., `zeltask list`)
- Use consistent option naming across apps
- Validate inputs at command level, process in core

### Storage Design
- Use zelutil.utils.state for path resolution
- Implement app-specific storage class in core/storage.py
- Follow active/completed/blueprint pattern
- Handle file creation and error cases gracefully

This architecture ensures all Zel apps are consistent, maintainable, and can integrate seamlessly for comprehensive productivity tracking.