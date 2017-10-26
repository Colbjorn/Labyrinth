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

    "inventory": [["leather armor", 1], ["sword", 2], ["health potion", 1]],  # Simply add in item objects imported from items.py.

    "spells": []
}
