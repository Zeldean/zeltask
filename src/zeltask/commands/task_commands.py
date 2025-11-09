"""Task-related CLI commands."""

import click
from ..core.task_manager import TaskManager

@click.group()
def task():
    """Task management commands."""
    pass

@task.command()
@click.argument('title')
@click.option('--description', '-d', default="")
@click.option('--priority', '-p', default="medium")
@click.option('--category', '-c')
@click.option('--tags', '-t')
def create(title, description, priority, category, tags):
    """Create a new task."""
    tag_list = tags.split(',') if tags else []
    manager = TaskManager()
    task_id = manager.create_task(title, description, priority, category, tag_list)
    click.echo(f"Created task: {task_id}")

@task.command()
def list():
    """List all active tasks."""
    manager = TaskManager()
    tasks = manager.list_active_tasks()
    
    if not tasks:
        click.echo("No active tasks.")
        return
    
    for task in tasks:
        click.echo(f"{task['id']}: {task['title']} [{task['priority']}]")

@task.command()
@click.argument('task_id')
def complete(task_id):
    """Mark task as completed."""
    manager = TaskManager()
    if manager.complete_task(task_id):
        click.echo(f"Completed task: {task_id}")
    else:
        click.echo(f"Task not found: {task_id}")