from app import app
from flask.ext.restful import Api, Resource
from app.models.models import Project
from flask import jsonify
import logging
from logging.handlers import RotatingFileHandler
import json, datetime
from bson import objectid
api = Api(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

class ProjectCatalog(Resource):
    def get(self):
        projects = Project.objects()
        return jsonify({"projects":projects.to_json()})

api.add_resource(ProjectCatalog, '/projects/')

