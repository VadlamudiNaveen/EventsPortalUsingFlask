from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import *

migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()