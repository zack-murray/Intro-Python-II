# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

# Basic player class to-be-updated
# Prepping for items
class Player: 
    def __init__(self, location):
        self.location = location
        self.items = []

    # Preps item to be taken play user
    def select_room(self):
        return self.location
    
    # Allows user to add item to inventory
    def add_item(self, item: Item):
        #if (self.location == Room['foyer']) or (self.location == Room['treasure']):
        self.items.append(item)
            #print(f'You pick up a {player.items}')
        #else:
           #print(f'Shit outta luck')

    # Allows user to drop item(s) in their current room
    def drop_item(self, item_name: str):
        for item in self.items:
            print(item)
            if item == item_name:
                self.items.remove(item)
                return item
        return None
        