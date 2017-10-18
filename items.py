# This module lists all the items and their relevant details.
import itemeffects

knife = {  # Sample item subject to change
    "id": "knife",

    "name": "Knife",

    "type": "Weapon",

    "description": "A sharp metal object perfect for shanking things with.",

    "usage": "equip",

    "on use": itemeffects.equip, 

    "damage": [1, 5],  # [Min, max]

    "cost": 10,

    "requirement": {
        "strength": 0,
        "dexterity": 0,
        "constitution": 0,
        "will": 0
    },

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonuses": {
        "strength": 0.2,
        "dexterity": 0.7,
        "constitution": 0,
        "will": 0
    }
}

# It is of utmost importance that all dictionaries are saved within a list so that it is possible to call them
# using an index or a loop!
items = {
    "knife": knife
}
