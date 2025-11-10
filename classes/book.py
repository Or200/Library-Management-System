

class Book:

    def __init__(self, title, author, ISBN, is_available : bool):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = is_available

    def print_book_info(self):
        print(f"the title: {self.title}, the author: {self.author}, the ISBN: {self.ISBN}, is available: {self.is_available}")