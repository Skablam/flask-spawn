export SETTINGS="config.DevelopmentConfig"

py.test --junitxml=TEST-{{cookiecutter.repo_name}}.xml --cov-report term-missing --cov application tests
