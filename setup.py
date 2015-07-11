from setuptools import setup, find_packages

setup(name='flask-spawn',
      version='0.1.9',
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
)
