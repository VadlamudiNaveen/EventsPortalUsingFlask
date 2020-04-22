import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

# config file has all the connections
app = Flask(__name__)
app.config.from_object(Configuration)
MIGRATION_DIR = os.path.join('models', 'migrations')


# DB connections
mongo = PyMongo(app)                        # mongo db
db = SQLAlchemy(app)                        # sql alchemy
redis_client = FlaskRedis(app)              # redis cache







#login_manager = LoginManager()
#login_manager.init_app(app)
#app.config['FLASK_ADMIN_SWATCH'] = 'darkly'




