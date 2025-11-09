import click
from .commands.task_commands import task as task_cmd
from .commands.blueprint_commands import blueprint

@click.group()
def task():
    """Task management CLI tool."""
    pass

# Add command groups
task.add_command(task_cmd, name='task')
task.add_command(blueprint)

# Quick access commands
@task.command()
def list():
    """List active tasks (shortcut)."""
    from .core.task_manager import TaskManager
    manager = TaskManager()
    tasks = manager.list_active_tasks()
    
    if not tasks:
        click.echo("No active tasks.")
        return
    
    for t in tasks:
        click.echo(f"{t['id']}: {t['title']} [{t['priority']}]")

if __name__ == "__main__":
    task()