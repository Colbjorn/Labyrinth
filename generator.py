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

        "number": len(rooms) + 1
    }
    rooms.append(new_room)


def room_check(new_room_coordinates):
    # This function takes in a set of coordinates and checks whether a room with those coordinates already exists.
    for room in rooms:
        if room["co-ordinates"] == new_room_coordinates:
            return True
        else:
            return False


