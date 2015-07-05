from shutil import copyfile

def add_database_files(appname, base_directory):
    database_directory = '{0}/snippets/database/'.format(base_directory)
    copyfile(database_directory + 'application/models.py', appname + '/application/models.py')
    copyfile(database_directory + 'manage.py', appname + '/manage.py')
    copy_contents_of_file(database_directory + 'requirements.txt', appname + '/requirements.txt')
    append_to_file(appname + '/application/__init__.py', database_directory + 'application/__init__.py')

def add_blueprints():
    pass #TODO

def copy_contents_of_file(source_file, destination_file):
    with file(source_file) as f:
        source_contents = f.read()

    f = open(destination_file, "w")
    f.write(source_contents)

def append_to_file(file_path, source_file):
    with file(source_file) as f:
        source_contents = f.read()

    with open(file_path, "a") as f:
        f.write(source_contents)
