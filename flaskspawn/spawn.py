import click
import os
from cookiecutter.main import cookiecutter

@click.group()
def spawn():
    pass

@spawn.command()
@click.option('--name')
def simple(name):
    import pdb; pdb.set_trace()
    cookiecutter('{0}/cookiecutters/simple/'.format(os.path.dirname(os.path.abspath(__file__))),
                 no_input=True,
                 extra_context={'repo_name': '{0}'.format(name)})

@spawn.command()
def large():
    click.echo('Generate simple large project')
