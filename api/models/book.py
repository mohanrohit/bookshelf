# book.py

class Book(object):
  def __init__(self, title, id):
      self.title = title
      self.id = id

  def __str__(self):
    return "Book(id=%d, title='%s')" % (self.id, self.title)
