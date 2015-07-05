from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

#IntelliJ considers the import below as 'not required'
#However, without it, the model is not migrated.
from application.models import *

from application.routes import app, db
app.config.from_object(os.environ.get('SETTINGS'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
