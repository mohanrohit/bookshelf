import os

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.dirname(__file__) + "db/bib.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.dirname(__file__) + "db/migrations"