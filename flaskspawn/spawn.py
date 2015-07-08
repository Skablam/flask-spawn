from cookiecutter.main import cookiecutter
from .snippets.snippets import add_database_files, add_route, add_template, add_view, add_blueprint
from distutils.dir_util import remove_tree
import click
import os

@click.group()
def spawn():
    pass

@spawn.command()
@click.option('-ty', '--type', type=click.Choice(['simple-frontend', 'simple-api']), default='simple-frontend')
@click.option('-d', '--database', is_flag=True, help="use to add code/files for database migrations")
@click.option('-b', '--blueprint', multiple=True)
@click.option('-r', '--route', multiple=True)
@click.option('-t', '--template', multiple=True)
@click.option('-v', '--view', multiple=True)
@click.argument('appname', required=True)
def new(appname, type, database, blueprint, route, template, view):
    base_directory = os.path.dirname(os.path.abspath(__file__))

    if type == 'simple-frontend':
        cookiecutter_path = '{0}/cookiecutters/simple-frontend/'.format(base_directory)
    elif type == 'simple-api':
        cookiecutter_path = '{0}/cookiecutters/simple-frontend/'.format(base_directory)

    cookiecutter(cookiecutter_path,
                 no_input=True,
                 extra_context={'repo_name': '{0}'.format(appname)})

    #Need to remove templates folder as not needed in api app
    if type == 'simple-api':
        remove_tree(appname + '/application/templates')

    if database:
        add_database_files(appname, base_directory)

    if blueprint:
        for blueprintname in blueprint:
            add_blueprint(appname, blueprintname, base_directory)

    if route:
        for routename in route:
            add_route(appname, routename, base_directory, 'snippets/route')

    if template:
        for templatename in template:
            add_template(appname, templatename, base_directory)

    if view:
        for viewname in view:
            add_view(appname, viewname, base_directory)
