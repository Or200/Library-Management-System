

class Library:

    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book : object) -> None:
        if book not in self.list_of_books:
            self.list_of_books.append(book)
            print("the book added successfully")
        else:
            print("the book is already in the system")

    def add_user(self, user : object) ->None:
        if user not in self.list_of_users:
            self.list_of_users.append(user)
            print("the user added successfully")
        else:
            print("the user is already in the system")

    def borrow_book(self, user_id : int, book_isbn : int) ->None:
            for book in self.list_of_books:
                if book.ISBN == book_isbn:
                    if book.is_available:
                        for user in self.list_of_users:
                            if user.id == user_id:
                                user.borrowed_books.append(book)
                                book.is_available = False
                                print("the borrow went successfully")
                                break
            else:
                print("the borrow is failed")

    def return_book(self, user_id : int, book_isbn : int) -> None:
        for user in self.list_of_users:
            if user.id == user_id:
                for book in self.list_of_books:
                    if book.ISBN == book_isbn:
                        book.is_available = True
                        user.borrowed_books.remove(book)
                        print("the return went successfully")
                        break
        else:
            print("the return is failed")

    def list_available_books(self) -> list:
        list_of_available_books = []
        for book in self.list_of_books:
            if book.is_available:
                list_of_available_books.append(book.__dict__)
        return list_of_available_books

    def search_book(self, title_or_author) -> object:
        list_of_books = []
        for book in self.list_of_books:
            if book.author == title_or_author or book.title == title_or_author:
                list_of_books.append(book.__dict__)
        return list_of_books