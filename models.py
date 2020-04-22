from flask_admin.contrib.pymongo import ModelView
from wtforms import form, fields


class story_form(form.Form):
    import datetime
    email = fields.StringField('email')
    tag = fields.StringField('tags')
    title = fields.TextAreaField('title')
    story = fields.TextAreaField('story')
    published_at = fields.DateTimeField('published_at', default=datetime.datetime.utcnow)


class story_view(ModelView):
     column_list = ('email', 'tag', 'title', 'story', 'published_at')
     column_searchable_list = ['email', 'title', 'tag']
     form = story_form


# nosql schema
class UserForm(form.Form):
    name = fields.StringField('name')
    password = fields.PasswordField('password')
    created_at = fields.DateTimeField('created_at')
    updated_at = fields.DateTimeField('updated_at')
    sys_info = fields.StringField('sys_info')


class UserView(ModelView):
    column_list = ('name', 'password', 'created_at', 'sys_info', 'updated_at')
    column_sortable_list = ('name', 'password', 'created_at', 'sys_info', 'updated_at')
    column_searchable_list = ['name']
    form = UserForm


class freshers_form(form.Form):
    role = fields.StringField('role')
    skills = fields.StringField('skills')
    location = fields.StringField('location')
    company = fields.StringField('company')
    dead_line = fields.DateTimeField('dead_line')
    experience = fields.StringField('experience')
    salary = fields.IntegerField('salary')


class freshers_view(ModelView):
    column_list = ('role', 'skills', 'location', 'company', 'dead_line', 'experience')
    column_sortable_list = ('experience', 'company')
    column_searchable_list = ['company', 'role']
    form = freshers_form


class experience_form(form.Form):
    role = fields.StringField('role')
    skills = fields.StringField('skills')
    location = fields.StringField('location')
    company = fields.StringField('company')
    dead_line = fields.DateTimeField('dead_line')
    experience = fields.IntegerField('experience')
    salary = fields.StringField('salary')


class experience_view(ModelView):
    column_list = ('role', 'skills', 'location', 'company', 'dead_line', 'experience', 'salary')
    column_sortable_list = ('experience', 'company', 'salary')
    column_searchable_list = ['company', 'skills'
                              ]
    form = experience_form
