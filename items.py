# This module lists all the items and their relevant details.
import itemeffects

no_weapon = {
    "id": "fists",

    "name": "Fists",

    "type": "Weapon",

    "action": "punching",

    "description": "Your fists. You can punch people with them. It could work in a fight. Maybe.",

    "usage": "none",

    "damage": 1,  # [Min, max]

    "cost": 0,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.1
}

no_armor = {
    "id": "no armor",

    "name": "Naked",

    "type": "Armor",

    "description": "Clothes are recommended.",

    "usage": "none",

    "defense": 0,

    "cost": 0
}

knife = {  # Sample item subject to change
    "id": "knife",

    "name": "Knife",

    "type": "Weapon",

    "action": "stabbing",

    "description": "A sharp metal object perfect for shanking things with.",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(knife),
    # End reference.

    "damage": 10,  # [Min, max]

    "cost": 10,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.5
}

leather_armor = {
    "id": "leather armor",

    "name": "Leather Armor",

    "type": "Armor",

    "description": "It's leather. Ooooh, leather!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(leather_armor),

    "defense": 20,

    "cost": 50
}
# It is of utmost importance that all dictionaries are saved within a list so that it is possible to call them
# using an index or a loop!
items = {
    "fists": no_weapon,

    "no armor": no_armor,

    "knife": knife,

    "leather armor": leather_armor
}

items_list = [

    knife,

    leather_armor
]
