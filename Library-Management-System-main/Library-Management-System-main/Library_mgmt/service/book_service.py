from dao.book_dao import BookDAO
from models.book import Book

class BookService:

    @staticmethod
    def add_new_book(title, author, isbn, category, total):
        if total < 0:
            raise ValueError("Total copies cannot be negative")

        book = Book(title, author, isbn, category, total, total)
        BookDAO.add_book(book)

    @staticmethod
    def view_books():
        return BookDAO.get_all_books()

    @staticmethod
    def search_books(keyword):
        return BookDAO.search_book(keyword)

    @staticmethod
    def remove_book(book_id):
        BookDAO.delete_book(book_id)
