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

bad_sword = {  # Sample item subject to change
    "id": "bad_sword",

    "name": "Knackered Sword",

    "type": "Weapon",

    "action": "slashing",

    "description": "A knackered old sword. Trusted by many for hundreds of years.",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(bad_sword),
    # End reference.

    "damage": 15,  # [Min, max]

    "cost": 15,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.6
}

sword = {  # Sample item subject to change
    "id": "sword",

    "name": "Sword",

    "type": "Weapon",

    "action": "slashing",

    "description": "A generic sword. Still coated with fear from those lost to it's blade",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(sword),
    # End reference.

    "damage": 20,  # [Min, max]

    "cost": 20,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.7
}

new_sword = {  # Sample item subject to change
    "id": "new_sword",

    "name": "New Sword",

    "type": "Weapon",

    "action": "slashing",

    "description": "A sword fresh off the production line! It has high hopes in slaying your foes!",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(new_sword),
    # End reference.

    "damage": 25,  # [Min, max]

    "cost": 25,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.7
}

glowing_sword = {  # Sample item subject to change
    "id": "glowing_sword",

    "name": "Glowing Sword",

    "type": "Weapon",

    "action": "slashing",

    "description": "Ooooh! A glowing sword!",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(glowing_sword),
    # End reference.

    "damage": 30,  # [Min, max]

    "cost": 30,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.7
}

old_hammer = {  # Sample item subject to change
    "id": "old_hammer",

    "name": "Old Hammer",

    "type": "Weapon",

    "action": "whacking",

    "description": "An old hammer! Probably better for hanging up pictures",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(old_hammer),
    # End reference.

    "damage": 15,  # [Min, max]

    "cost": 10,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.6
}

hammer = {  # Sample item subject to change
    "id": "hammer",

    "name": "Hammer",

    "type": "Weapon",

    "action": "whacking",

    "description": "A hammer! Watch where you swing it!",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(hammer),
    # End reference.

    "damage": 20,  # [Min, max]

    "cost": 15,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.6
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

    "leather armor": leather_armor,

    "bad_sword": bad_sword,

    "sword": sword,

    "new_sword": new_sword,

    "glowing_sword": glowing_sword,

    "old_hammer": old_hammer,

    "hammer": hammer,


}
