from cookiecutter.main import cookiecutter
import click
import os

@click.group()
def spawn():
    pass

@spawn.command()
@click.option('-n', '--name', prompt='Project name')
@click.option('-t', '--type', type=click.Choice(['simple-frontend', 'simple-api']), default='simple-frontend')
def new(name, type):

    if type == 'simple-frontend':
        cookiecutter_path = '{0}/cookiecutters/simple-frontend/'.format(os.path.dirname(os.path.abspath(__file__)))

    cookiecutter(cookiecutter_path,
                 no_input=True,
                 extra_context={'repo_name': '{0}'.format(name)})

@spawn.command()
def large():
    click.echo('Generate simple large project')
