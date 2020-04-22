from flask_admin import Admin
from flask_admin.contrib import rediscli
from flask_admin.contrib.sqla import ModelView
from redis import Redis
from app import *
from models import *

# admin registration is instantiated
admin = Admin(app, template_mode='bootstrap3')
admin.add_view(rediscli.RedisCli(Redis()))                       # redis cli
admin.add_view(story_view(mongo.db.stories, 'stories'))          # stories
admin.add_view(UserView(mongo.db.users, 'users'))                # users
admin.add_view(freshers_view(mongo.db.freshers, 'fresh_jobs'))   # Freshers jobs
admin.add_view(experience_view(mongo.db.experience, 'ex_jobs'))  # Experienced jobs