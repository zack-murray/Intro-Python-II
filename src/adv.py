from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['treasure'].items.append(
    Item('magical_key',
    'An old gold key, doesnt look like anything special but might be useful.')
)

room['foyer'].items.append(
    Item('lit_candel',
    'A lit candel sitting on a table, provides a sufficient source of illumination.')
)

#
# Main
#

# Tries to move player in input direction
def try_direction(player, direction):
    attribute = direction + '_to'

    # Allows us to check if class has an attribute
    if hasattr(player.location, attribute):
        # For valid direction
        # getattr fetches value associated with attribute
        # effectively updating player's location to new room
        player.location = getattr(player.location, attribute)
    else:
        # For invalid direction
        print("You search and search, but can't seem to find an exit!")

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
while True:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print('\n')
    print(player.location)
    # * Waits for user input and decides what to do.
    command = input("\nCommand: ").lower().split()
        
    # If the user enters "q", quit the game.
    if command == 'q':
        break
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if len(command) > 1:
        item = command[1]

    command = command[0]
        
    if command == 'n':
        # move north
        # print('This works!')
        try_direction(player, command)
    elif command == 's':
        # move south
        try_direction(player, command)
    elif command == 'e':
        # move east
        try_direction(player, command)
    elif command == 'w':
        # move west
        try_direction(player, command)
    elif command == 'inspect':
        # inspect current room for items
        loot = player.select_room().search_room()
        #if loot is not None: 
            #print(f"After an exhausting search, you have found a {item_name}")
        #else:
            #print(f"Searching tiredlessly has proven un-fruitful, there are no items in this room")
    elif command == 'get':
        # user takes an item in the room
        #item = player.select_room().grab_item(item)
        if (player.location == room['foyer']) or (player.location == room['treasure']):
            player.select_room().grab_item(item)
            player.add_item(item)
            print(f'You pick up a {player.items}')
        else:
            print(f'You scan the area from top to bottom, but dont find any items')
        print('\n')
        #print(f'You pick up a {player.items}')
        #print(f"You've picked up an item")
    elif command == 'drop':
        # user drops an item in the room
        item_tbd = player.drop_item(item)
        if item_tbd is not None:
            player.location.items.append(item)
            #player.location.add_item(item_tbd)
            print("\n")
            print(f"You've have dropped an item")
            #print(f"You have dropped {item_tbd}")
        else:
            print(f"You do not have a item to drop")
            
    #
        
