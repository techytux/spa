from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

app.config["MONGODB_SETTINGS"] = {'DB': 'spa'}
app.config["SECRET_KEY"] = ""

db = MongoEngine(app)
from app.routes import index

if __name__ == '__main__':
    app.run()

