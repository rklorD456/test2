import click
import os
from pathlib import Path
from .repo import InMemoryRepo


DEFAULT_SAVE_FILE = os.path.expanduser("~/.hospital_data.json")


@click.group()
@click.option('--data-file', default=DEFAULT_SAVE_FILE,
              help='JSON file to store patient data')
@click.pass_context
def cli(ctx, data_file):
    """Tiny hospital CLI"""
    ctx.obj = {}
    ctx.obj['repo'] = InMemoryRepo()
    ctx.obj['data_file'] = data_file
    
    # Create directory if needed
    Path(data_file).parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing data if any
    if os.path.exists(data_file):
        ctx.obj['repo'].load(data_file)


@cli.command()
@click.argument('name')
@click.argument('age', type=int)
@click.option('--diagnosis', '-d', default=None)
@click.pass_context
def add(ctx, name, age, diagnosis):
    """Add a patient"""
    repo = ctx.obj['repo']
    p = repo.add_patient(name, age, diagnosis)
    repo.save(ctx.obj['data_file'])
    click.echo(f"Added patient {p.id}: {p.name} ({p.age})")
    click.echo(f"Data saved to {ctx.obj['data_file']}")


@cli.command('list')
@click.pass_context
def _list(ctx):
    """List all patients"""
    repo = ctx.obj['repo']
    patients = repo.list_patients()
    if not patients:
        click.echo("No patients found.")
        return
    
    for p in patients:
        click.echo(f"{p.id}: {p.name}, age={p.age}, diagnosis={p.diagnosis}")
