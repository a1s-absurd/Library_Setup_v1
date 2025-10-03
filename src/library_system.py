from . import libraryitems
from . import read_write_db


class Library:
    library_items: list
    
    def __init__(self):
        try:
            ff = read_write_db.DBReadWrite().dic_of_library_items["library"]
            self.library_items = [libraryitems.LibraryItem(i["item_type"]) for i in ff]
            
            # print(self.library_items)
        except KeyError as e:
            print(e)
            
    def __repr__(self):
        return f"{[i for i in self.library_items]}"
    
    def search(self):
        pass