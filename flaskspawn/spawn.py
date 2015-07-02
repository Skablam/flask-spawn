import click
import os
from cookiecutter.main import cookiecutter

@click.group()
def spawn():
    pass

@spawn.command()
def simple():
    import pdb; pdb.set_trace()
    cookiecutter('{0}/cookiecutters/simple/'.format(os.path.dirname(os.path.abspath(__file__))))

@spawn.command()
def large():
    click.echo('Generate simple large project')
