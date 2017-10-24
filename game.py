# Main game code.
from map import rooms
from gameparser import *
from player import *
from items import *
from attacks import *
from generator import *
from monsters import *
playing = True

# Turns inputted list into a string of items.
def list_of_items(items):
    hold = ""
    for i in items:
        hold += (str(i["name"]) + ", ")
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
    # Display room monster

    # Display room items
    print_room_items(room)
    # Display room interactables
    '''
            CODE THAT WILL DISPLAY THE DESCRIPTION OF AN INTERACTABLE
'''


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for i in room_items:
        print("TAKE " + str(i["id"]) + " to take " + str(i["name"]) + ".")
    for i in inv_items:
        print("DROP " + str(i["id"]) + " to drop your " + str(i["name"]) + ".")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        current_room = rooms[current_room["exits"][direction]]
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


def update_location(direction):
    pass


def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]


def combat_menu(monster):
    inpt = input("What will you do? ATTACK with your weapon, USE an item or RUN away?")
    norminpt = normalise_input(inpt)

    if len(norminpt) == 0:
        print("You pass your turn.")
    elif norminpt[0] == "attack":
        p_attack(player, monster, player["weapon"])
    elif norminpt[0] == "use":
        if len(norminpt)> 1:


def initiate_combat(monster):
    monster["health"] = monster["max health"]

    def fighting():
        if monster["health"] <= 0:
            print(monster["name"], "has been slain!")
            for i in monster["loot"]:
                player["inventory"].append(i)
                print("Obtained", i + "!")
            player["experience"] += monster["experience"]
            print("Gained", monster["experience"], "experience!")
            player["gold"] += monster["gold"]
            print("Gained", monster["gold"], "gold!")
            return False
        elif player["health"] <= 0:
            print("You have been slain!")
            print(""" __     ______  _    _   _____ _____ ______ _____  
 \ \   / / __ \| |  | | |  __ \_   _|  ____|  __ \ 
  \ \_/ / |  | | |  | | | |  | || | | |__  | |  | |
   \   /| |  | | |  | | | |  | || | |  __| | |  | |
    | | | |__| | |__| | | |__| || |_| |____| |__| |
    |_|  \____/ \____/  |_____/_____|______|_____/ """)
            global playing
            playing = False
            return False
        else:
            return True
    while fighting():
        random.choice(monster["attacks"])(monster, player)



def main():
    # Main game loop
    while playing:
        # Display game status (room description, inventory etc.)
        print_room(current_room)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)
