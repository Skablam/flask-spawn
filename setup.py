from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

# class Tox(TestCommand):
#     user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
#     def initialize_options(self):
#         TestCommand.initialize_options(self)
#         self.tox_args = None
#     def finalize_options(self):
#         TestCommand.finalize_options(self)
#         self.test_args = []
#         self.test_suite = True
#     def run_tests(self):
#         import tox
#         import shlex
#         args = self.tox_args
#         if args:
#             args = shlex.split(self.tox_args)
#         errno = tox.cmdline(args=args)
#         sys.exit(errno)

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(name='flask-spawn',
      version='0.1.10',
      install_requires=[
            'Click==3.3',
            'Cookiecutter',
        ],
      description='Generate new flask projects quickly and easily, in a variety of customisable structures.',
      url='https://github.com/Skablam/flask-spawn',
      author='Matthew Pease',
      author_email='stainlesssteelmatt@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      entry_points='''
            [console_scripts]
            spawn=flaskspawn.spawn:spawn
      ''',
      tests_require=['pytest'],
      cmdclass = {'test': PyTest},
)
