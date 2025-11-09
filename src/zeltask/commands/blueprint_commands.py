"""Blueprint-related CLI commands."""

import click
from ..core.task_manager import TaskManager

@click.group()
def blueprint():
    """Blueprint template commands."""
    pass

@blueprint.command()
@click.argument('blueprint_type', type=click.Choice(['recurring', 'manual']))
@click.argument('blueprint_id')
@click.argument('title')
@click.option('--description', '-d', default="")
@click.option('--priority', '-p', default="medium")
@click.option('--schedule', help="For recurring: daily, weekly")
@click.option('--time', help="Time for recurring tasks (HH:MM)")
def create(blueprint_type, blueprint_id, title, description, priority, schedule, time):
    """Create a new blueprint template."""
    manager = TaskManager()
    
    kwargs = {
        'description': description,
        'priority': priority
    }
    
    if blueprint_type == 'recurring':
        kwargs['schedule'] = schedule
        kwargs['time'] = time
    
    manager.create_blueprint(blueprint_id, title, blueprint_type, **kwargs)
    click.echo(f"Created {blueprint_type} blueprint: {blueprint_id}")

@blueprint.command()
def list():
    """List all blueprint templates."""
    manager = TaskManager()
    blueprints = manager.storage.load_blueprints()
    
    if not blueprints:
        click.echo("No blueprints found.")
        return
    
    for bp in blueprints:
        click.echo(f"{bp['id']}: {bp['title']} [{bp['type']}]")