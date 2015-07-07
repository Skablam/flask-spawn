from shutil import copyfile
import re
import jinja2

template_list = []

def add_database_files(appname, base_directory):
    #TODO Make this method idempotent
    database_directory = '{0}/snippets/database/'.format(base_directory)

    copyfile(database_directory + 'application/models.py', appname + '/application/models.py')
    copyfile(database_directory + 'manage.py', appname + '/manage.py')
    add_to_requirements(database_directory + 'requirements.txt', appname + '/requirements.txt')
    add_config({"SQLALCHEMY_DATABASE_URI":'""'}, appname)
    #Update application/__init__.py
    import_directory = appname + '/application/__init__.py'
    add_import({import_directory:"from flask.ext.sqlalchemy import SQLAlchemy\n"})
    append_to_file(appname + '/application/__init__.py', database_directory + 'application/__init__.py')

def add_blueprints():
    pass #TODO

def copy_contents_of_file(source_file, destination_file):
    with open(source_file) as f:
        source_contents = f.read()

    with open(destination_file, "w") as f:
        f.write(source_contents)

def append_to_file(file_path, source_file):
    with open(source_file) as f:
        source_contents = f.read()

    with open(file_path, "a") as f:
        f.write(source_contents)

def add_text_to_file_after_pattern(text, pattern, destination_file):
    with open(destination_file, 'r+') as f:
        contents = f.readlines()
        line_index = None
        for idx,line in enumerate(contents):
            result = re.search(pattern, line)
            if result:
                line_index = idx
                break
        if line_index:
            contents.insert(line_index + 1, text)
            contents = "".join(contents)
            f.seek(0)
            f.write(contents)
            f.truncate()

def add_text_to_top_of_file(destination_file, text):
    with open(destination_file, 'r+') as f:
        contents = f.readlines()
        contents.insert(0, text)
        contents = "".join(contents)
        f.seek(0)
        f.write(contents)
        f.truncate()

def render_snippets(appname):
    templateLoader = jinja2.FileSystemLoader(searchpath=appname)
    templateEnv = jinja2.Environment(loader=templateLoader)

    for template in template_list:
        jinja_template = templateEnv.get_template(template["name"])
        import pdb; pdb.set_trace()
        f = open(appname + "/" + template["name"],'w')
        f.write(jinja_template.render(template["values"]))
        f.close

def add_template_to_be_rendered(template_name, values):
    template = {"name":template_name, "values":values}
    template_list.append(template)

def add_config(config, appname):
    for key in config:
        add_text_to_file_after_pattern("    " + key + " = " + config[key] + "\n" , 'class Config\(object\)', appname + '/config.py')

def add_import(imports):
    for key in imports:
        add_text_to_top_of_file(key, imports[key])

def add_to_requirements(source_requirements, destination_requirements):
    #TODO Need to make sure that requirements are not duplicated
    copy_contents_of_file(source_requirements, destination_requirements)
