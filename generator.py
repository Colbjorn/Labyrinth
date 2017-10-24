import random
from copy import copy
from map import rooms
from monsters import monsters
from player import player


def choose_monster(room):
    # This function picks a monster from the list of monsters in monsters.py and adds it to the room taken as argument.
    # Copy functions obtained from python documentation. Reference:
    # https://docs.python.org/3/library/copy.html
    monster_list = copy(monsters)
    for i in monster_list:
        if i["level"] > (player["level"] + 5):
            monster_list.remove(i)
        elif i["level"] < (player["level"] - 5):
            monster_list.remove(i)
    room["monster"] = random.choice(monster_list)


def make_room(co_ordinates):
    # This function creates a room dictionary with an appropriate name and number.
    # It will use random number generation to select from lists of items, descriptions, etc.
    new_room = {
        "name": "", # TODO: Room name list.

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
    rooms[tuple(co_ordinates)] = new_room


def room_check(new_room_coordinates):
    # This function takes in a set of coordinates and checks whether a room with those coordinates already exists.
    if tuple(new_room_coordinates) in rooms:
        return True
    else:
        return False


def create_rooms_around(co_ordinates):
    # Creates rooms around the given coordinates, adding exits as appropriate and skipping rooms that already exist.
    north = copy(co_ordinates)
    north[1] += 1
    east = copy(co_ordinates)
    east[0] += 1
    south = copy(co_ordinates)
    south[1] -= 1
    west = copy(co_ordinates)
    west[0] -= 1
    rms = [north, east, west, south]
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
            rooms[tuple(rm)]["exits"].append("south")
            rooms[tuple(co_ordinates)]["exits"].append("north")
        elif rm == east:
            rooms[tuple(rm)]["exits"].append("west")
            rooms[tuple(co_ordinates)]["exits"].append("east")
        elif rm == south:
            rooms[tuple(rm)]["exits"].append("north")
            rooms[tuple(co_ordinates)]["exits"].append("south")
        elif rm == west:
            rooms[tuple(rm)]["exits"].append("east")
            rooms[tuple(co_ordinates)]["exits"].append("west")
        else:
            print("Invalid exit created.")


make_room([0, 1])
rooms[(0, 1)]["exits"].append("south")
create_rooms_around([0, 1])
print(rooms)
