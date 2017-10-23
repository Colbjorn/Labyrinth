# Main game code.
from map import rooms
from gameparser import *
from player import *
from items import *
from attacks import *
from generator import *
from monsters import *

# Turns inputted list into a string of items.
def list_of_items(items):
    hold = ""
    for i in items:
        hold += (str(i["name"]) + ", ")
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
    # Display room items
    print_room_items(room)
    # Display room interactibles
    '''
            CODE THAT WILL DISPLAY THE DESCRIPTION OF AN INTERACTIBLE
'''

