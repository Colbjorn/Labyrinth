# Tracks player's stats.

player = {
    "name": "",  # Inputted by player at start of game.

    # TODO: Make sure the following are printed every turn.
    "location": [0, 0],

    "max health": 20,  # TODO: Balance this with weapons and monsters!

    "health": 20,

    "max mana": 10,  # Can be any other secondary resource, or none at all!

    "mana": 10,

    "level": 1,

    "experience": 0,

    "status effects": [],  # e.g. poisoned, paralyzed, etc.

    # Revise stats, see if they make sense.
    "strength": 5,  # Maybe could modify during a character creator?

    "dexterity": 5,

    "constitution": 5,

    "will": 5,

    "weapon": None,

    "armor": None,

    "inventory": ["knife"],  # Simply add in item objects imported from items.py.

    "spells": []  # Same as items.
}
