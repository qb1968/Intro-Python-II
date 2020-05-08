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

#
# Main
#
items = {
    "saber": Item("Saber", "This is your weapon."),
    "torch": Item("Torch", "This is your light."),
    "gold": Item("Gold", "Eureka!")
}

room['outside'].items.append(items["torch"])
room['overlook'].items.append(items["saber"])
room['narrow'].items.append(items["gold"])
# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name = "Jonathan", current_room = room["outside"])
print("\nWelcome! Please enter a direction to travel n, s, e, w, and q to quit the game.\n\nYou may get, take, pickup items, or drop them.\n\n")
# print(f"{new_player.player.name} is in {new_player.current_room} \n")
print(new_player.current_room.list_items())
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    selection = input("Enter a direction, command or Q to escape: ")
    user_selection = selection.lower().split(" ")
    if len(user_selection) == 1: 
        if selection == "q": 
            print("GOODBYE!!!")
            break
        elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
            new_player.move(selection)
            print(f"\n{new_player.player_name} is in {new_player.current_room.room_name} \n{new_player.current_room.description}\n\n {new_player.current_room.list_items()}")
        elif selection == "i":
            new_player.print_items()
        else:
            print("Try Again!")
    elif len(user_selection) == 2: 
        if user_selection[0] in ["take", "get", "pickup"]:
            if items[user_selection[1]]:
                new_player.pickup_item(items[user_selection[1]])
                
                print("\n\nYou have added a new item to inventory!\n")
                print(f"{new_player.player_name} is {new_player.current_room} \n")
                print(new_player.current_room.list_items())
            else:
                print("That isn't an item.")
        elif user_selection[0] == "drop": 
            if items[user_selection[1]]:
                new_player.drop_item(items[user_selection[1]])
                print("You dropped an item!")
                print(new_player.print_items())
                print(f"{new_player.player_name} is {new_player.current_room} \n")
                print(new_player.current_room.list_items())
            else: 
                print("That isn't an item.")
        else: 
            print("Try Again!")
    else: 
        print("Try Again!")

# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.