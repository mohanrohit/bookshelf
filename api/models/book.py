# book.py

from api import db

from model import ModelMixin

class Book(db.Model, ModelMixin):
  __tablename__ = "books"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
  title = db.Column(db.String(64), nullable=False, unique=True)
