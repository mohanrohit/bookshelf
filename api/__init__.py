import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from router import Router

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.dirname(__file__) + "/db/bib.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_MIGRATE_REPO"] = os.path.dirname(__file__) + "/db/migrations"

db = SQLAlchemy(app)

router = Router(app)
