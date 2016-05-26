from flask.ext.classy import FlaskView
#from flask.ext.restful import Resource
from book import Book

class BooksView(FlaskView):
  def __init__(self):
    self.books = {
      4: Book(id=4, title="Head First Design Patterns"),
      6: Book(id=6, title="Advanced Qt programming"),
      13: Book(id=13, title="Computer graphics")
    }

  def get(self):
    books = ["book %d: %s" % (k, v) for k, v in self.books.items()]

    return str(books), 200
