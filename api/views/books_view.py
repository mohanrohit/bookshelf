from api_view import ApiView

from book import Book

class BooksView(ApiView):
  def get(self):
    books = Books.query.all()

    return self.render_object(books)

  def post(self):
    for k, v in self.params.items():
      print k, v
    title = self.params["title"]
    if title is None:
      return self.render_error("Title is required.", 400)

    new_book = Book(title=title)
    new_book.save()

    return self.render_object(new_book)
