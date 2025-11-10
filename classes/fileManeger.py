import json

class FileManeger:

    def add_to_json(self, list_book: list[object], list_user: list[object]):

        lib = {"books": [book.__dict__ for book in list_book], "users": [user.__dict__ for user in list_user]}

        with open("library.json", "w") as f:
            json.dump(lib, f, ensure_ascii = False, indent = 4)

    def lode_from_json(self):
        with open("library.json") as f:
            lib = json.load(f)
        return lib