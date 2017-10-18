# This module lists all monsters and their relevant details.

goblin = {  # Sample monster subject to change.
    "name": "Goblin",

    "level": 1,

    # Monsters currently only store max health because of the TODO below.
    "health": 15,  # TODO: Might be a good idea to have monster current health stored in the combat function.
    # The above is in order to make it so new monsters always start at max health, and for easier tracking.

    "mana": 0,

    "defense": 0,

    "attacks": {  # TODO: Possibly have an entire file dedicated to attacks as they will all be functions.
        "scratch": scratch_attack()
    },

    "loot": []
}
monsters = [goblin]
