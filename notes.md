player = Player("Brady", room['outside'])
current_room = player.current_room

print(current_room)

valid_directions = ["n", "s", "e", "w"]

while True:
    # Wait for user input
    cmd = input("-> ")
    # Parse user inputs (n, s, e, w, q)
    if cmd in valid_directions:
        # If input is valid, move the player and loop
        player.travel(cmd)
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else:
        print("I did not recognize that command")


# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! there's no room here.", "\n")

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        str = f"""
              \n----------------------------------
              \n{self.title}
              \n   {self.description}\n"""
        return str