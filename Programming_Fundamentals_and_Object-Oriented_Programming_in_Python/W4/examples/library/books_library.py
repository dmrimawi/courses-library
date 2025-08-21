class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_all(self):
        list_of_books = ""
        for book in self.books:
            list_of_books = f"{list_of_books}{book.info()}\n"
        return list_of_books
