# This module lists all the items and their relevant details.
import itemeffects

knife = {  # Sample item subject to change
    "id": "knife",

    "name": "Knife",

    "type": "Weapon",

    "description": "A sharp metal object perfect for shanking things with.",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(knife),
    # End reference.

    "damage": [1, 5],  # [Min, max]

    "cost": 10,

    "requirement": 0,  # Level requirement. MAY BE UNNECESSARY!

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.5
}

# It is of utmost importance that all dictionaries are saved within a list so that it is possible to call them
# using an index or a loop!
items = {
    "knife": knife
}
