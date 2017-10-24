# Tracks player's stats.
player = {
    "name": "Captain Placeholder",  # Inputted by player at start of game.

    # TODO: Make sure the following are printed every turn.
    "location": [0, 0],

    "max health": 20,  # TODO: Balance this with weapons and monsters!

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

    "armor": "no armor",

    "inventory": [],  # Simply add in item objects imported from items.py.

    "spells": []
}
