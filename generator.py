import random
from copy import copy
from map import rooms


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
    rooms[tuple(co_ordinates)] = new_room


def room_check(new_room_coordinates):
    # This function takes in a set of coordinates and checks whether a room with those coordinates already exists.
    if tuple(new_room_coordinates) in rooms:
        return True
    else:
        return False


def rooms_create(co_ordinates):
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
