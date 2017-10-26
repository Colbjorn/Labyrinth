# Stores the map. Room 1 is always the same. The other rooms are generated once the game begins.
from monsters import monsters
from interactables import *

room_1 = {
    "name": "Labyrinth Entrance",

    "description":
    """DESCRIPTION HERE""",#tbd

    "exits": ["north"],

    "items": [], #tbd

    "co-ordinates": (0, 0),

    "monster": "",

    "entered": True,

    "interactables": "",

    "number": 1
    
}

story_room_1 = {
    "name": "Farm",

    "description":
    '''Before you is a small ranch. Open fields surround the area, cattle peacefully graze upon the local vegetation,
and you can see some kind of vegetables being grown, but you don\'t know exactly what kind. The place seems inhabited,
but there are signs of disorganization that show this place is not as peaceful as it seems; broken bales of hay spread 
across some of the countryside, broken fences, and even a strangely-shaped glowing object that looks like a sword, which 
unfortunately vanishes into the ether as you move forward. It looks like it may have once been peaceful here, but
definitely not anymore.''',

    "exits": [],  # Assigned when room is generated.

    "items": [],

    "co-ordinates": None,  # Assigned when room is generated.

    "monster": "",

    "entered": False,

    "interactables": story_npc_1,

    "number": 10
}

rooms = {
    (0, 0): room_1,
}
