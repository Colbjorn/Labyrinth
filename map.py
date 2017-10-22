# Stores the map. Room 1 is always the same. The other rooms are generated once the game begins.
from items import items
from monsters import monsters

room_1 = {
    "name": "Labyrinth Entrance",

    "description":
    """""",#tbd

    "exits": ["north"],

    "items": [], #tbd

    "co-ordinates": (0, 0),

    "monster": "",

    "entered": True,

    "interactables": "",

    "used": False,

    "number": 1
    
}

rooms = {
    (0, 0): room_1,
}
