import datetime
from flask import url_for
from app import db

class Project(db.Document):
    last_edited_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    project_mentor = db.StringField(max_length=50, required=True)
    project_supervisor = db.StringField(max_length=50, required=True)
    description = db.StringField(required=True)
    tags = db.ListField(db.StringField(max_length=50))
