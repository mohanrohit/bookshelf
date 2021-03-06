﻿import os

base_directory = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = False
  SECRET_KEY = "some-secret-key"

  # for SQLAlchemy
  SQLALCHEMY_DATABASE_URI = "sqlite:///" + base_directory + "/db/bib.db"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_MIGRATE_REPO = base_directory + "/db/migrations"

class ProductionConfig(Config):
  DEBUG = False

class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
