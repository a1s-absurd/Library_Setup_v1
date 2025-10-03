from dataclasses import dataclass


@dataclass
class LibraryItem:
    item_type: str
    
    def add_item(self):
        pass
    
    def remove_item(self):
        pass
        


# class Itemtype:
#     def __init__(self, book, dvd, cd, mag):
#         self.book  = book
#         self.dvd = dvd
#         self.cd = cd
#         self.mag = mag

class Book(LibraryItem):
    def __init__(self):
        pass
    
class DVD(LibraryItem):
    def __init__(self):
        pass

class CD(LibraryItem):
    def __init__(self):
        pass

class Mag(LibraryItem):
    def __init__(self):
        pass