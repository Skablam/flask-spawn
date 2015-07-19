from flaskspawn.spawn import new, spawn
import click
from click.testing import CliRunner
import unittest, pytest
import os, os.path, sys, subprocess, filecmp

class TestSpawn(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_spawn(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(spawn, ['new', 'testapp'])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

    def test_small_new_default(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(new, ['testapp'])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

    def test_small_new_view(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(new, ['testapp', "-v", "hello"])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            if not os.path.exists("testapp/application/templates/hello.html"):
                pytest.fail("template hello.html not created")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

    def test_small_new_dataview(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(new, ['testapp', "-dv", "goodbye"])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

    def test_small_new_template(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(new, ['testapp', "-t", "hello"])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            raise_error_if_file_doesnt_exist("testapp/application/templates/hello.html", "hello.html")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

    def test_small_with_database(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(new, ['testapp', "-d"])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            raise_error_if_file_doesnt_exist("testapp/manage.py", "manage.py")
            raise_error_if_file_doesnt_exist("testapp/application/models.py", "manage.py")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

    def test_small_with_blueprint(self):
        path_to_small = os.getcwd() + "/flaskspawn/cookiecutters/small/{{cookiecutter.repo_name}}"
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(new, ['testapp', "-b", "farewell"])
            assert result.exit_code == 0
            if not second_dir_has_all_files_of_first(path_to_small, "testapp"):
                pytest.fail("application created not equal to small template")
            raise_error_if_file_doesnt_exist("testapp/application/farewell.py", "farewell.py")
            testappoutput = subprocess.check_output(["py.test"], cwd="testapp")
            self.assertNotRegexpMatches(testappoutput, "failed")

def second_dir_has_all_files_of_first(dir1, dir2):
    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not second_dir_has_all_files_of_first(new_dir1, new_dir2):
            return False
    return True

def raise_error_if_file_doesnt_exist(file_path, file_name):
    if not os.path.exists(file_path):
        pytest.fail("file {0} not created".format(file_name))
