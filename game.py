# Main game code.
from map import rooms
from gameparser import *
from player import player
from items import items_dict
from attacks import *
from generator import *
from monsters import *
from healthbar import call_health
from copy import deepcopy
playing = True


def check_story_rooms_around(co_ordinates):
    # Checks for unentered story room near coordinates, and prints a message and updates HUD accordingly if there is one.
    north = copy(co_ordinates)
    north[1] += 1
    east = copy(co_ordinates)
    east[0] += 1
    south = copy(co_ordinates)
    south[1] -= 1
    west = copy(co_ordinates)
    west[0] -= 1
    rms = [north, east, south, west]
    valid_rms = []
    for i in rms:
        if room_check(i):
            valid_rms.append(i)
    for i in valid_rms:
        if rooms[tuple(i)] in story_rooms and not rooms[tuple(i)]["entered"]:
            if rooms[tuple(i)] == story_rooms[0]:
                if i == north:
                    print("You hear a yell coming from the north. It might be worth checking out.")
                    player["last important location"] = north
                elif i == east:
                    print("You hear a yell coming from the east. It might be worth checking out.")
                    player["last important location"] = east
                elif i == south:
                    print("You hear a yell coming from the south. It might be worth checking out.")
                    player["last important location"] = south
                elif i == west:
                    print("You hear a yell coming from the west. It might be worth checking out.")
                    player["last important location"] = west
            elif rooms[tuple(i)] == story_rooms[1]:
                if i == north:
                    print("A strong gust of wind blows from the north.")
                    player["last important location"] = north
                elif i == east:
                    print("A strong gust of wind blows from the east.")
                    player["last important location"] = east
                elif i == south:
                    print("A strong gust of wind blows from the south.")
                    player["last important location"] = south
                elif i == west:
                    print("A strong gust of wind blows from the west.")
                    player["last important location"] = west

# Turns inputted list into a string of items.
def list_of_items(itms):
    hold = ""
    for item in itms:
        name = item[0]
        amount = item[1]
        hold += (items_dict[name]["name"] + " x " + str(amount) + ", ")
    return hold.rstrip(", ")


# Prints all of the items in an inputted room.
def print_room_items(room):
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")
        print()


def print_room(room):
    # Display room name
    print(room["name"].upper())
    print()
    # Display room coordinates and coordinates of last spotted story room.
    print("LOCATION:", room["co-ordinates"])
    print("POINT OF INTEREST:", player["last important location"])
    print()
    # Prints room description if first time entering.
    if not room["entered"]:
        print(room["description"])
        print()
    # Prints interactables' description if they are present.
    if room["interactables"]:
        print(room["interactables"]["description"])
    # Checks story rooms around player's location.
    check_story_rooms_around(list(room["co-ordinates"]))
    # Display room items3
    print_room_items(room)


def print_inventory_items(items):
    if len(items) > 0:
        print("You have " + list_of_items(items) + ".")
        print()
    else:
        print("You are not carrying anything.")
        print()


def print_exit(direction):
    print("GO " + direction.upper())


def print_menu(exits, room_items, inv_items, coords):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction)
    if room_items:
        print("TAKE an item.")
    if inv_items:
        print("DROP an item.")
    if rooms[tuple(coords)]["interactables"]:
        if not rooms[tuple(coords)]["interactables"]["used"]:
            print("Context action:", rooms[tuple(coords)]["interactables"]["context action"].upper())
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


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


def execute_go(direction):
    rooms[tuple(player["location"])]["entered"] = True
    if is_valid_exit(rooms[tuple(player["location"])]["exits"], direction):
        move(direction, player["location"])
        if not rooms[tuple(player["location"])]["entered"]:
            rooms_create_around(player["location"])
    else:
        print("You cannot go there.")


def modified_amount(array, itemname, action):
    # This function takes in an array, an item's name and an action as argument.
    # When removing, the function checks for the item's name in the array and, if the item's amount is over 1, removes
    # one unit from this amount. If there's only one left, it removes the list from the array entirely.
    # When appending, it checks whether there first exists an item with that name in the array. If there, it
    # increases its amount by 1. Otherwise it creates a new list within the array, containing one instance of the item.
    # The function also returns a False boolean if it finds no item while removing so an appropriate print can be made.
    if action == "remove":
        for item in array:
            if item[0] == itemname:
                if item[1] == 1:
                    array.remove(item)
                    return True
                else:
                    item[1] -= 1
                    return True
        else:
            return False
    elif action == "append":
        for item in array:
            if item[0] == itemname:
                item[1] += 1
                return True
        else:
            array.append([itemname, 1])
            return True
    elif action == "check":
        for item in array:
            if item[0] == itemname:
                return True
        else:
            return False


def execute_take(item):
    rooms[tuple(player["location"])]["entered"] = True
    taken = modified_amount(rooms[tuple(player["location"])]["items"], item, "remove")
    if not taken:
        print("Can't take that!")
    else:
        print("You took", items_dict[item]["name"] + ".")
        modified_amount(player["inventory"], item, "append")


def execute_drop(item):
    rooms[tuple(player["location"])]["entered"] = True
    dropped = modified_amount(player["inventory"], item, "remove")
    if not dropped:
        print("Can't drop that!")
    else:
        print("You dropped", items_dict[item]["name"] + ".")
        modified_amount(rooms[tuple(player["location"])]["items"], item, "append")


def execute_describe(item):
    rooms[tuple(player["location"])]["entered"] = True
    itm = items_dict[item]
    is_there = False
    for i in player["inventory"]:
        if i[0] == item:
            print(itm["name"].upper())
            print("Type:", itm["type"])
            print(itm["description"])
            if itm["type"] == "Weapon":
                print("Attack:", itm["damage"])
                print("Damage bonus: x", itm["bonus"])
            elif itm["type"] == "Armor":
                print("Defense:", itm["defense"])
            print("Cost:", itm["cost"], "gold.")
            is_there = True
            break
    if not is_there:
        print("Can't examine an item you can\'t look at!")


def execute_status():
    rooms[tuple(player["location"])]["entered"] = True
    print(player["name"].upper())
    call_health(player["health"], player["max health"])
    print("Level:", str(player["level"]))
    print("Experience:", str(player["experience"]) + "/" + str(10* (player["level"]**2)))
    print("Gold:", str(player["gold"]))
    print("Attack:", str(player["attack"]))
    print("Defense:", str(player["defense"]))
    print("Weapon:", items_dict[player["weapon"]]["name"])
    print("Armor:", items_dict[player["armor"]]["name"])


def execute_use(item, target):
    if check_if_user(target):
        use_target = player
    else:
        use_target = monster_dict[target]
    if use_target == player or use_target in monsters_dict:
        if item["usage"] == "heal":
            use_target["health"] += item["heal"]
            if use_target["health"] > use_target["max health"]:
                use_target["health"] = use_target["max health"]
        if item["usage"] == "damage":
            use_target["health"] -= item["damage"]
            if use_target["health"] < 0:
                use_target["health"] = 0


def execute_equip(item):
    rooms[tuple(player["location"])]["entered"] = True
    is_there = False
    if item in items_dict.keys():
        itm = items_dict[item]
        if itm["type"] == "Weapon":
            is_there = modified_amount(player["inventory"], item, "remove")
            if is_there:
                if player["weapon"] is not None:  # If a weapon is being held, it'll move to the inventory.
                    modified_amount(player["inventory"], player["weapon"], "append")
                player["weapon"] = item
        elif itm["type"] == "Armor":
            is_there = modified_amount(player["inventory"], item, "remove")
            if is_there:
                if player["armor"] is not None:  # If an armor is being worn, it'll move to the inventory.
                    modified_amount(player["inventory"], player["armor"], "append")
                player["armor"] = item
                player["defense"] = itm["defense"]
    if itm["type"] == "Weapon":
        is_there = modified_amount(player["inventory"], item, "remove")
        if is_there:
            if player["weapon"] is not None:  # If a weapon is being held, it'll move to the inventory.
                modified_amount(player["inventory"], player["weapon"], "append")
            player["weapon"] = item
    elif itm["type"] == "Armor":
        is_there = modified_amount(player["inventory"], item, "remove")
        if is_there:
            if player["armor"] is not None:  # If an armor is being worn, it'll move to the inventory.
                
                modified_amount(player["inventory"], player["armor"], "append")
            player["armor"] = itm
            player["defense"] = itm["defense"]
    else:
        print("Cannot equip that!")
    if not is_there:
        print("Can't equip that!")


def execute_help():
    rooms[tuple(player["location"])]["entered"] = True
    print("Due to a large variety of commands, not all will be shown to you all the time or it'd be a truly painful experience.")
    print("Luckily, this here menu's here to help!")
    print()
    print("The following actions can be done when outside combat:")
    print("TAKE + an item that is currently on the floor will add it to your inventory.")
    print("DROP will drop an item onto the floor, but why do that?")
    print("EQUIP will equip a weapon/armor. If you already have any equipped, they return to your inventory.")
    print("DESCRIBE + an item in your inventory will give you a summary of stats and a visual description.")
    print("STATUS will show you all of your stats.")
    print("INVENTORY will display your inventory.")
    print("GO + a valid direction (these always show) will move you in that direction.")
    print("HELP will print this menu whenever you wish.")
    print()
    print("Sometimes, you will be able to interact with something in a room. The following is an example situation:")
    print("Context action: TALK")
    print("Typing the action will perform it, but only when in context.")
    print("After all, you can't open a chest that isn't there, or talk to a nonexistent person!")
    print()
    print("The following actions can be done in combat:")
    print("ATTACK will attack the enemy with your equipped weapon.")
    print("USE item ON a target will use said item on that target. Don't forget the target!")
    print("It would be a shame if you used a healing potion on an enemy, or a vial of poison on yourself!")
    print("RUN will attempt to run. Enemies get a free hit on you if you fail. If you succeed you will run in a random direction,")
    print("so be wise when fleeing!")


def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        item = " ".join(command[1:])
        command[1] = item
        command[2:] = []
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        item = " ".join(command[1:])
        command[1] = item
        command[2:] = []
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            print_inventory_items(player["inventory"])

    elif command[0] == "describe":
        if len(command) > 1:
            execute_describe(command[1])
        else:
            print("Describe what?")
            print_inventory_items(player["inventory"])

    elif command[0] == "status":
        execute_status()

    elif command[0] == "help":
        execute_help()

    elif command[0] == "inventory":
        print_inventory_items(player["inventory"])

    elif command[0] == "equip":
        item = " ".join(command[1:])
        command[1] = item
        command[2:] = []
        if len(command) > 1:
            execute_equip(command[1])
        else:
            print("Equip what?")

    elif command[0] == "use":
        item = " ".join(command[1:(command.index("on"))])
        target = " ".join(command[(command.index("on")) + 1:])
        command[1] = item
        command[2] = target
        command[3:] = []
        if modified_amount(player["inventory"], command[1], "check") and (command[2] in monsters_dict or check_if_user(command[2])):
            execute_use(items_dict[command[1]], command[2])
        elif command[1] in player["inventory"]:
            print("Use " + command[1] + " on who?")
        elif command[2] in monsters_dict or check_if_user(command[2]):
            print("Use what on " + command[2] + "?")
            print(command[1])
        else:
            print("Use what on who?")
            
    # The following code deals with context actions.
    elif command[0] == rooms[tuple(player["location"])]["interactables"]["context action"]\
            and not rooms[tuple(player["location"])]["interactables"]["used"]:
        rooms[tuple(player["location"])]["interactables"]["context result"]()
        rooms[tuple(player["location"])]["interactables"]["used"] = True
        rooms[tuple(player["location"])]["entered"] = True

    else:
        print("This makes no sense.")

def check_if_user(target):
    if target == "self" or target == "myself" or target == "me" or target == player["name"]:
        return True

def menu(exits, room_items, inv_items, coords):
    # Display menu
    print_menu(exits, room_items, inv_items, coords)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


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
                item = " ".join(norminpt[1:(norminpt.index("on"))])
                target = " ".join(norminpt[(norminpt.index("on")) + 1:])
                norminpt[1] = item
                norminpt[2] = target
                norminpt[3:] = []
                if modified_amount(player["inventory"], norminpt[1], "check") and (
                        norminpt[2] in monsters_dict or check_if_user(norminpt[2])):
                    execute_use(items_dict[norminpt[1]], norminpt[2])
                elif norminpt[1] in player["inventory"]:
                    print("Use " + norminpt[1] + " on who?")
                elif norminpt[2] in monsters_dict or check_if_user(norminpt[2]):
                    print("Use what on " + norminpt[2] + "?")
                    print(norminpt[1])
                else:
                    print("Use what on who?")
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


def level_up_check(experience):
    # This function takes in the player's experience, checks if it's enough to advance to the next level,
    # and levels up if need be. The player levels up when experience = 10 * (level**2).
    # The player's attack increases by their new level each time they level up.
    if experience >= 10 * (player["level"]**2):
        player["level"] += 1
        print("Level up! Leveled up to level", str(player["level"]) + "!")
        player["attack"] += player["level"]
        player["max health"] += 5
        player["health"] = player["max health"]


def initiate_combat(manster):
    # Entire combat loop.
    monster = deepcopy(manster)
    monster["health"] = monster["max health"]
    monster["loot"] = []
    for loot in manster["loot"]:
        if random.randint(1, 10) == 1:
            monster["loot"].append(loot)


    def theyded():
        # Checks health. If anyone dies, stops the fighting appropriately.
        if monster["health"] <= 0:
            print(monster["name"], "has been slain!")
            while monster["loot"] != []:
                # Takes literally everything.
                if random.randint(1,100) > items_dict[monster["loot"][0][0]]["rarity"]:
                    modified_amount(player["inventory"], monster["loot"][0][0], "append")
                    print("Obtained", monster["loot"][0][0] + "!")
                modified_amount(monster["loot"], monster["loot"][0][0], "remove")
            player["experience"] += monster["experience"]
            print("Gained", monster["experience"], "experience!")
            level_up_check(player["experience"])
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
    print(monster["health"])
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
        command = menu(current_room["exits"], current_room["items"], player["inventory"], player["location"])

        # Execute the player's command
        execute_command(command)
        # Checks whether player has entered a monster's territory and initiates combat if so.
        if current_room["monster"] != "":
            initiate_combat(current_room["monster"])


if __name__ == "__main__":
    main()
