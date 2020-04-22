import os


class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    TESTING = True
    DEBUG = True
    FLASK_ADMIN_SWATCH = 'slate'
    SECRET_KEY = "this-is-the-secret-key-for-sample-app"
    MONGO_DBNAME = "myDatabase"
    MONGO_URI = "mongodb://localhost:27017/myDatabase"
    REDIS_URL = "redis://localhost:6379/0"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/mydata.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'codingbabas@gmail.com'
    MAIL_DEFAULT_SENDER = "codingbabas@gmail.com"
    MAIL_PASSWORD = 'coding143'
    # administrator list
    ADMINS = ['codingbabas@gmail.com']
