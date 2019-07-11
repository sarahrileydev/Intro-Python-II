# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.strength = 10
        self.items = []

    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! there's no room here.", "\n")

    def pickup_item(self, item):
        if item:
            self.items.append(item)
            print(f"You have added {item.name}")
        else:
            print("Item not found. Please choose valid item.")
        
    def drop_item(self, item):
        self.items.remove(item)
        

    def _get_item_string(self):
        if len(self.items) > 0:
            return "\n" + ", ".join([item for item in self.items]) + "\n"
        else:
            return ""

    def print_inventory(self):
        print(f"Your strength is: {self.strength}\n")
        if len(self.items) > 0:
            print("You are carrying:\n  " + ", ".join([item.name for item in self.items]) + "\n")

 
