

class User:
    
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.borrowed_books = []
