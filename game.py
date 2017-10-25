# Main game code.
from map import rooms
from gameparser import *
from player import player
from items import *
from attacks import *
from generator import *
from monsters import *
from healthbar import call_health
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
    if not room["entered"]:
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
        rooms[tuple(player["location"])]["entered"] = True
        move(direction, player["location"])
        print(player["location"])
        if not rooms[tuple(player["location"])]["entered"]:
            rooms_create_around(player["location"])
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
    if direction == "north":
        co_ordinates[1] += 1
    elif direction == "east":
        co_ordinates[0] += 1
    elif direction == "south":
        co_ordinates[1] -= 1
    elif direction == "west":
        co_ordinates[0] -= 1


def combat_menu(monster):
    choice = False
    while not choice:
        call_health(player["health"], player["max health"])
        inpt = input("What will you do? ATTACK with your weapon, USE an item or RUN away?")
        norminpt = normalise_input(inpt)
        if len(norminpt) == 0:
            print("You do nothing.")
            choice = True
        elif norminpt[0] == "attack":
            p_attack(player, monster, player["weapon"])
            choice = True
        elif norminpt[0] == "use":
            if len(norminpt) > 1:
                pass  # Throw in the use function
            else:
                print("Use what?")
                print_inventory_items(player["inventory"])
        elif norminpt[0] == "run":
            result = random.randint(1, 5)
            print(result)
            if result < 3:
                print("Successfully escaped!")
                return "run"
            else:
                print("Failed to run away!")
                choice = True
        else:
            print("Can't do that!")
        print()



def initiate_combat(monster):
    # Entire combat loop.
    monster["health"] = monster["max health"]

    def theyded():
        # Checks health. If anyone dies, stops the fighting appropriately.
        if monster["health"] <= 0:
            print(monster["name"], "has been slain!")
            for i in monster["loot"]:
                player["inventory"].append(i)
                print("Obtained", i + "!")
            player["experience"] += monster["experience"]
            print("Gained", monster["experience"], "experience!")
            player["gold"] += monster["gold"]
            print("Gained", monster["gold"], "gold!")
            rooms[tuple(player["location"])]["monster"] = ""
            return True
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
            return True

    print(monster["name"], "attacks!")
    while 1:
        if theyded():
            break
        choice = combat_menu(monster)
        if choice == "run":
            # Runs in random direction.
            north = copy(player["location"])
            north[1] += 1
            east = copy(player["location"])
            east[0] += 1
            south = copy(player["location"])
            south[1] -= 1
            west = copy(player["location"])
            west[0] -= 1
            options = [north, east, west, south]
            new_options = []
            for i in options:
                if room_check(i):
                    new_options.append(i)
            run_choice = random.choice(new_options)
            if run_choice == north:
                move("north", player["location"])
            elif run_choice == east:
                move("east", player["location"])
            elif run_choice == south:
                move("south", player["location"])
            elif run_choice == west:
                move("west", player["location"])
            else:
                print("Error while running away.")
            break
        if theyded():
            break
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
        # Checks whether player has entered a monster's territory and initiates combat if so.
        if current_room["monster"] != "":
            initiate_combat(current_room["monster"])


if __name__ == "__main__":
    main()
