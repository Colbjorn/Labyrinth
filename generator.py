import random
from copy import copy
from map import rooms
from monsters import monsters
from player import player
from descriptions import room_descriptions


def choose_monster(room):
    # This function chooses a monster equal to ya boy's in level and adds it to the room taken as an argument.
    # Also has a chance of spawning nothing at all.
    spawn = False
    if random.randint(1, 2) == 1:
        spawn = True
    if spawn:
        chosen = False
        monsters_copy = copy(monsters)
        while not chosen:
            choice = random.choice(monsters_copy)
            if choice["level"] != player["level"]:
                monsters_copy.remove(choice)
            else:
                chosen = True
                room["monster"] = choice
    else:
        room["monster"] = ""


def make_room(co_ordinates):
    # This function creates a room dictionary with an appropriate name and number.
    # It will use random number generation to select from lists of items, descriptions, etc.
    new_room = {
        "name": "",

        "description": """""",

        "exits": [],

        "items": [],

        "co-ordinates": co_ordinates,

        "monster": "",

        "entered": False,

        "interactables": "",

        "used": False,

        "number": len(rooms)+1
    }
    choose_monster(new_room)
    location = copy(random.choice(room_descriptions))
    new_room["name"] = location["name"]
    new_room["description"] = location["description"]
    rooms[tuple(co_ordinates)] = new_room


def room_check(new_room_coordinates):
    # This function takes in a set of coordinates and checks whether a room with those coordinates already exists.
    if tuple(new_room_coordinates) in rooms:
        return True
    else:
        return False


def rooms_create_around(co_ordinates):
    # Coordinates list rewritten due to if functions utilizing variable names.
    north = copy(co_ordinates)
    north[1] += 1
    east = copy(co_ordinates)
    east[0] += 1
    south = copy(co_ordinates)
    south[1] -= 1
    west = copy(co_ordinates)
    west[0] -= 1
    rms = [north, east, south, west]
    for i in rms:
        if room_check(i):
            rms.remove(i)
    rm_num = random.randint(1, len(rms))
    while rm_num > 0:
        # Praise StackOverflow. Reference:
        # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
        rm = random.choice(rms)
        # End reference.
        rms.remove(rm)
        rm_num -= 1
        make_room(rm)
        if rm == north:
            if not ("south") in rooms[tuple(rm)]["exits"]:
                rooms[tuple(rm)]["exits"].append("south")
            rooms[tuple(co_ordinates)]["exits"].append("north")
        elif rm == east:
            if not ("west") in rooms[tuple(rm)]["exits"]:
                rooms[tuple(rm)]["exits"].append("west")
            rooms[tuple(co_ordinates)]["exits"].append("east")
        elif rm == south:
            if not ("north") in rooms[tuple(rm)]["exits"]:
                rooms[tuple(rm)]["exits"].append("north")
            rooms[tuple(co_ordinates)]["exits"].append("south")
        elif rm == west:
            if not ("east") in rooms[tuple(rm)]["exits"]:
                rooms[tuple(rm)]["exits"].append("east")
            rooms[tuple(co_ordinates)]["exits"].append("west")
        else:
            print("Invalid exit created.")
