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


# Make a new player object that is currently in the 'outside' room.


# print(player.room.title)

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

player = Player("Sarah", room['outside'])

rock = Item("Rock")
pencil = Item("Pencil")


room['outside'].items.append(rock)
player.items.append(pencil)



current_room = player.current_room

print(current_room)

valid_directions = ["n", "s", "e", "w"]


while True:
    # Wait for user input
    cmd = input("-> ")
    wordList = cmd.split(' ')
    # Parse user inputs (n, s, e, w, q)
    if cmd in valid_directions:
        # If input is valid, move the player and loop
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    elif cmd == "q":
        print("Goodbye!")
        exit()
    elif wordList[0] == "get":
        if len(current_room.items):
            for item in current_room.items:
                if item.name.lower() == wordList[1].lower():
                    player.pickup_item(item)
                    current_room.items.remove(item)
                else:
                    print(f"We don't have any {wordList[1]}") 
    elif wordList[0] == "drop":
        if len(player.items):
            for item in player.items:
                if item.name.lower() == wordList[1].lower():
                    player.drop_item(item)
                    current_room.items.append(item)
                    print(f"You have dropped {item.name}")
                else:
                    print(f"We don't have any {wordList[1]}")   
    else:
        print("I did not recognize that command")


# print("Please choose a room. Enter n, s, e, w, or q to quit.")

# while True:
#     print(f'You are in the {player.room.title}. {player.room.description}')

#     if player.room.title == "Treasure Chamber":
#         print("You found the treasure!")
#         break
#     player_choice = input("What room do you want to visit? ")


#     if player_choice == "n":
#         if player.room.n_to:
#             player.room = player.room.n_to
#         else:
#             print("Nothing that way. Choose another direction.")
#     elif player_choice == "s":
#         if player.room.s_to:
#             player.room = player.room.s_to
#         else:
#             print("Nothing that way. Choose another direction.")
#     elif player_choice == "e":
#         if player.room.e_to:
#             player.room = player.room.e_to
#         else:
#             print("Nothing that way. Choose another direction.")
#     elif player_choice == "w":
#         if player.room.w_to:
#             player.room = player.room.w_to
#         else:
#             print("Nothing that way. Choose another direction.")
#     elif player_choice == "q":
#         print("Game over!")
#         break
