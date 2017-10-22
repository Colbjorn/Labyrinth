# This module lists all monsters and their relevant details.
import attacks
from player import player

goblin = {  # Sample monster subject to change.
    "name": "Goblin",

    "level": 1,

    # Monsters currently only store max health because of the TODO below.
    "max health": 15,  # TODO: Might be a good idea to have monster current health stored in the combat function.
    # The above is in order to make it so new monsters always start at max health, and for easier tracking.

    "max mana": 0,

    "status effects": [],

    "strength": 0,

    "dexterity": 0,

    "constitution": 0,

    "will": 0,

    "attacks": {
        "scratch": attacks.scratch_attack
    },

    "loot": [],

    "experience": 10
}

# Important! In order for optimization to be implemented later on, keep the below list ordered by level.
monsters = [goblin]
