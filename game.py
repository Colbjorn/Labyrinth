# Main game code.
from map import rooms
from gameparser import *
from player import player
from items import *
from attacks import *
from generator import *
from monsters import *
playing = True


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
        move(direction, player["location"])
        print(player["location"])
        if not rooms[tuple(player["location"])]["entered"]:
            rooms_create_around(player["location"])
            rooms[tuple(player["location"])]["entered"] =  True
        print(rooms[tuple(player["location"])]["entered"])
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


def move(direction, co_ordinates):
    # changes player coords to next room
    print(co_ordinates)
    if direction == "north":
        co_ordinates[1] += 1
    elif direction == "east":
        co_ordinates[0] += 1
    elif direction == "south":
        co_ordinates[1] -= 1
    elif direction == "west":
        co_ordinates[0] -= 1


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
    make_room([0, 1])
    rooms[(0, 1)]["exits"].append("south")


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
