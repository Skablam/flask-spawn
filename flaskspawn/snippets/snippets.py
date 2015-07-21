from shutil import copyfile
import jinja2
from .file_routines import append_to_file, append_text_to_file, add_text_to_file_after_pattern, copy_contents_of_file, add_text_to_top_of_file

template_list = []

def add_database_files(appname, base_directory):
    database_directory = '{0}/snippets/database/'.format(base_directory)

    copyfile(database_directory + 'application/models.py', appname + '/application/models.py')
    copyfile(database_directory + 'manage.py', appname + '/manage.py')
    add_to_requirements(database_directory + 'requirements.txt', appname + '/requirements.txt')
    add_config({"SQLALCHEMY_DATABASE_URI":'""'}, appname)
    #Update application/__init__.py
    import_directory = appname + '/application/__init__.py'
    add_import({import_directory:"from flask.ext.sqlalchemy import SQLAlchemy\n"})
    append_to_file(appname + '/application/__init__.py', database_directory + 'application/__init__.py')

def add_route(appname, routename, base_directory, template_folder):
    templateLoader = jinja2.FileSystemLoader(searchpath=base_directory + '/' + template_folder)
    templateEnv = jinja2.Environment(loader=templateLoader)

    jinja_template = templateEnv.get_template('application/views.py.j2')
    with open(appname + '/application/views.py', 'a') as f:
        f.write("\n" + jinja_template.render(routename=routename) + "\n")

def add_dataview(appname, dataviewname, base_directory, template_folder):
    add_import({appname + '/application/views.py':"from flask import Response\n"})
    add_route(appname, dataviewname, base_directory, template_folder)
    add_test(appname, base_directory, dataviewname, dataviewname, '200 OK')

def add_template(appname, templatename, base_directory):
    templateLoader = jinja2.FileSystemLoader(searchpath=base_directory + '/snippets/template')
    templateEnv = jinja2.Environment(loader=templateLoader)

    jinja_template = templateEnv.get_template('application/templates/sample_template.html')
    with open(appname + '/application/templates/' + templatename + '.html', 'w') as f:
        f.write("\n" + jinja_template.render(templatename=templatename) + "\n")

def add_view(appname, viewname, base_directory):
    add_route(appname, viewname, base_directory, 'snippets/view')
    add_template(appname, viewname, base_directory)
    add_import({appname + "/application/views.py":"from flask import render_template\n"})
    add_test(appname, base_directory, viewname, viewname, '200 OK')

def add_blueprint(appname, blueprintname, base_directory, size):
    if size == "small":
        add_blueprint_small(appname, blueprintname, base_directory)

def add_blueprint_small(appname, blueprintname, base_directory):
    add_blueprint_file(appname, blueprintname, base_directory)
    add_template(appname, blueprintname + 'main', base_directory)
    add_test(appname, base_directory, blueprintname, blueprintname, '301 MOVED PERMANENTLY')

def add_blueprint_file(appname, blueprintname, base_directory):
    templateLoader = jinja2.FileSystemLoader(searchpath=base_directory + '/snippets/blueprint - small')
    templateEnv = jinja2.Environment(loader=templateLoader)

    jinja_template = templateEnv.get_template('application/blueprint.py.j2')
    with open(appname + '/application/' + blueprintname + '.py', 'w') as f:
        f.write("\n" + jinja_template.render(blueprintname=blueprintname) + "\n")

    import_directory = appname + '/application/__init__.py'
    add_import({import_directory:"from " + blueprintname + " import " + blueprintname + "\n"})

    jinja_template = templateEnv.get_template('application/__init__.py')
    rendered_text = jinja_template.render(blueprintname=blueprintname) + '\n'
    append_text_to_file(appname + '/application/__init__.py', rendered_text)

def add_config(config, appname):
    for key in config:
        add_text_to_file_after_pattern("    " + key + " = " + config[key] + "\n", 'class Config\\(object\\)', appname + '/config.py')

def add_import(imports):
    for key in imports:
        if not imports[key] in open(key).read():
            add_text_to_top_of_file(key, imports[key])
            print "fff"

def add_to_requirements(source_requirements, destination_requirements):
    copy_contents_of_file(source_requirements, destination_requirements)

def add_test(appname, base_directory, testname, routename, expected_result):
    templateLoader = jinja2.FileSystemLoader(searchpath=base_directory + '/snippets/test')
    templateEnv = jinja2.Environment(loader=templateLoader)

    jinja_template = templateEnv.get_template('tests/test_app.py.j2')

    rendered_text = '\n' + jinja_template.render(testname=testname, routename=routename, expected_result=expected_result) + '\n'
    append_text_to_file(appname + '/tests/test_app.py', rendered_text)
