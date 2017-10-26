# Stores the map. Room 1 is always the same. The other rooms are generated once the game begins.
from monsters import monsters_dict
from interactables import *

room_1 = {
    "name": "The Beginning",

    "description":
    """Welcome to the Labyrinth! For some mysterious reason, various dimensions have begun to mix into each other. It 
is up to you to try to escape this mayhem before something very, very bad occurs.
If you ever need help knowing what commands you can use, type HELP.""",#tbd

    "exits": ["north"],

    "items": [], #tbd

    "co-ordinates": (0, 0),

    "monster": "",

    "entered": False,

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

    "monster": monsters_dict["ogre"],

    "entered": False,

    "interactables": story_npc_1,

    "number": 10
}

story_room_2 = {
    "name": "Laboratorium",

    "description":
    '''You now find yourself within what appears to be a laboratory. The walls, however, seem clear as if made of glass.
There is nothing else within the room besides a table at its center atop which, most prominently, is a glass dome. The 
rest of the table seems to be covered in papers which seem to be the notes and scribbles of a man of questionable 
sanity. While a lot of the scribbles on the papers seem like gibberish, some seem strangely relevant to your situation...''',

    "exits": [],

    "items": [],

    "co-ordinates": None,

    "monster": "",

    "entered": False,

    "interactables": story_npc_2,

    "number": 20
}
rooms = {
    (0, 0): room_1,
}

story_room_3 = {
    "name": "Island",

    "description":
    '''you find yourself on a small island. Stranded, you see only the ocean touching the horizon.
a single palm tree can be seen om this small mound of sand. It seems the coconuts that once grew on
the tree has been split open and eaten. Perhaps somebody has been through here before?
you notice a large red cross by your feet''',

    "exits": [],  # Assigned when room is generated.

    "items": [],

    "co-ordinates": None,  # Assigned when room is generated.

    "monster": "",

    "entered": False,

    "interactables": story_npc_1,

    "number": 30
}

story_room_4 = {
    "name": "Empty Room",

    "description":
    '''You enter a near empty, white room. In the middle of the room is a door.
Through the door, you see your old home. Your family and friends and living their lives,
you recognise your hometown and get a great sence of relief.''',

    "exits": [],  # Assigned when room is generated.

    "items": [],

    "co-ordinates": None,  # Assigned when room is generated.

    "monster": "",

    "entered": False,

    "interactables": door,

    "number": 40
}

story_rooms = [story_room_1, story_room_2, story_room_3, story_room_4]
