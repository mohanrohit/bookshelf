# book.py

from api import db

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(64), nullable=False)
