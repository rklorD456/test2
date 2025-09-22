import click
from .repo import InMemoryRepo


@click.group()
@click.pass_context
def cli(ctx):
    """Tiny hospital CLI"""
    ctx.obj = {}
    ctx.obj['repo'] = InMemoryRepo()


@cli.command()
@click.argument('name')
@click.argument('age', type=int)
@click.option('--diagnosis', '-d', default=None)
@click.pass_context
def add(ctx, name, age, diagnosis):
    """Add a patient"""
    repo = ctx.obj['repo']
    p = repo.add_patient(name, age, diagnosis)
    click.echo(f"Added patient {p.id}: {p.name} ({p.age})")


@cli.command('list')
@click.pass_context
def _list(ctx):
    repo = ctx.obj['repo']
    for p in repo.list_patients():
        click.echo(f"{p.id}: {p.name}, age={p.age}, diagnosis={p.diagnosis}")
