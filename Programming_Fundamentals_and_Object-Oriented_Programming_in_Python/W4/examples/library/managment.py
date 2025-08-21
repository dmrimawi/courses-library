from book import Book
from books_library import Library


book1 = Book("Fundamantal Programming", "GSG")
book2 = Book("Data Structures", "Ali")
book3 = Book("Algorithms", "Alkhawarzmi")

lib = Library()

lib.add_book(book1)
lib.add_book(book3)
lib.add_book(book2)

print(lib.list_all())


