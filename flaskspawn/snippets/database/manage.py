from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from application.models import *
from application.routes import app
from application import db
import os

app.config.from_object(os.environ.get('SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
