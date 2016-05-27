# book.py

from api import db

class Book(db.Model):
  __tablename__ = "books"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
  title = db.Column(db.String(64), nullable=False, unique=True)
