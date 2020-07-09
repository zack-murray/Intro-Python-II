# Implement a class to hold room information. This should have name and
# description attributes.\
from item import Item
# A basic room class to hit mvp
# Prepping for items
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def __str__(self):
        return f"{self.name}: {self.description}"

    # Prints the room's inventory
    def search_room(self):
        if len(self.items) == 0:
            print("Despite a valiant search, you find no useful items.\n")
        else:
            print(f"Items in this room: ")
            for item in self.items:
                print(item.name)

    # Preps item to be taken by user
    def grab_item(self, item_name: str):
        itemToReturn: ''
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                #return item