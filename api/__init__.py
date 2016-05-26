from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from router import Router

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "bib.db"

db = SQLAlchemy(app)

router = Router(app)
