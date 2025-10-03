import os
import json

class DBReadWrite:
    def __init__(self):
        try:
            with open ("data/library_data.json", 'r') as library_data:
                # print(f"found {library_data}")
                self.dic_of_library_items = json.load(library_data)
                
        except FileNotFoundError as e:
            print(e)
            
    def map_to_library(self, data):
        json.load()
        