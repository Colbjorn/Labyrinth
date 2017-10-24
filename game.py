# Main game code.
from map import rooms
from gameparser import *
from player import player
from items import *
from attacks import *
from generator import *
from monsters import *

# Turns inputted list into a string of items.
def list_of_items(items):
    hold = ""
    print(items)
    for item in items:
        print(hold)
        print(item["name"])
        hold += (str(item["name"]) + ", ")
        print(hold)
    return hold.rstrip(", ")

# Prints all of the items in an inputted room.
def print_room_items(room):
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")
        print()

def print_room(room):
    print()
    # Display room name
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display room items3
    print_room_items(room)


def print_inventory_items(items):
    print("you have " + list_of_items(items) + ".")
    print()


def print_exit(direction):
    print("GO " + direction.upper())


def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction)
#    for i in room_items:
#        print("TAKE " + str(i["id"]) + " to take " + str(i["name"]) + ".")
#    for i in inv_items:
#        print("DROP " + str(i["id"]) + " to drop your " + str(i["name"]) + ".")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    if is_valid_exit(rooms[tuple(player["location"])]["exits"], direction):
        print(direction)
        print(player["location"][0])
        print(player["location"][1])
        move(direction, player["location"])
        print(player["location"])
        rooms_create(player["location"])
    else:
        print("You cannot go there.")


def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(direction, coordinates):
    # changes player coords to next room
    print(coordinates)
    if direction == "north":
        coordinates[1] += 1
    elif direction == "east":
        coordinates[0] += 1
    elif direction == "south":
        coordinates[1] -= 1
    elif direction == "west":
        coordinates[0] -= 1


def main():
    playing = True
    # Main game loop
    while playing:
        # Display game status (room description, inventory etc.)
        print_room(rooms[tuple(player["location"])])
        #print_inventory_items(player["inventory"])

        # Show the menu with possible actions and ask the player
        current_room = rooms[tuple(player["location"])]
        command = menu(current_room["exits"], current_room["items"], player["inventory"])

        # Execute the player's command
        execute_command(command)

if __name__ == "__main__":
    main()
