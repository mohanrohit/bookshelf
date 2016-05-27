from api_view import ApiView

from book import Book

class BookView(ApiView):
  def get(self, id):
    id = int(id)

    book = Book.query.get(id)
    if not book:
      return self.render_error("Book with id %d was not found." % id, 404)

    return self.render_object(book)
