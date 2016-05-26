from flask.ext.classy import FlaskView
#from flask.ext.restful import Resource
from book import Book

class BookView(FlaskView):
  def __init__(self):
    self.books = {
      4: Book("Head First Design Patterns", 4),
      6: Book("Advanced Qt programming", 6),
      13: Book("Computer graphics", 13)
    }

  def get(self, id):
    id = int(id)
    if not id in self.books.keys():
      return "Book with id %d not found." % id, 404

    book = self.books[id]
    print "book is %s" % book
    return book.title, 200
