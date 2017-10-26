# Tracks player's stats.

player = {
    "name": "Captain Placeholder",  # Inputted by player at start of game.

    "location": [0, 0],

    "last important location": [0, 0],

    "max health": 20,

    "health": 20,

    "max mana": 10,  # Can be any other secondary resource, or none at all!

    "mana": 10,

    "level": 1,

    "experience": 0,

    "gold": 0,

    "status effects": [],  # e.g. poisoned, paralyzed, etc.

    # Revise stats, see if they make sense.
    "attack": 5,

    "defense": 0,

    "weapon": "knife",

    "armor": "clothes",

    "inventory": [],  # Simply add in item objects imported from items.py.

    "spells": []
}

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