class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Book: {self.title}, author: {self.author}"
