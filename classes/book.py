

class Book:

    def __init__(self, title : str, author : str, ISBN : int):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = True

    def print_book_info(self) -> None:
        print(f"the title: {self.title}, the author: {self.author}, the ISBN: {self.ISBN}, is available: {self.is_available}")