from cookiecutter.main import cookiecutter
from snippets.snippets import add_database_files
import click
import os

@click.group()
def spawn():
    pass

@spawn.command()
@click.option('-t', '--type', type=click.Choice(['simple-frontend', 'simple-api']), default='simple-frontend')
@click.option('-d', '--database', is_flag=True, help="use if you want to add code for database migrations")
@click.option('-b', '--blueprint', multiple=True)
@click.argument('appname', required=True)
def new(appname, type, database, blueprint):
    base_directory = os.path.dirname(os.path.abspath(__file__))

    if type == 'simple-frontend':
        cookiecutter_path = '{0}/cookiecutters/simple-frontend/'.format(base_directory)

    cookiecutter(cookiecutter_path,
                 no_input=True,
                 extra_context={'repo_name': '{0}'.format(appname)})

    if database:
        add_database_files(appname, base_directory)

    if blueprint:
        click.echo('\n'.join(blueprint))
