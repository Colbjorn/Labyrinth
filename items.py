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

fire_hammer = {  # Sample item subject to change
    "id": "fire_hammer",

    "name": "Sulphuras",

    "type": "Weapon",

    "action": "whacking",

    "description": "You know, I think that hammer might be on fire... straight from some fire lord dude.",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(fire_hammer),
    # End reference.

    "damage": 30,  # [Min, max]

    "cost": 20,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.6
}

lightsaber = {  # Sample item subject to change
    "id": "lightsaber",

    "name": "Lightsaber",

    "type": "Weapon",

    "action": "slaying",

    "description": "A lightsaber?! Where did you even get that?!",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(lightsaber),
    # End reference.

    "damage": 100,  # [Min, max]

    "cost": 80,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.9
}

kirill = {  # Sample item subject to change
    "id": "kirill",

    "name": "Duelled Sword of Kirill",

    "type": "Weapon",

    "action": "l33t h4xxing",

    "description": "l33t h4xx3r Kirill, hacks everything to death with those mad skillz",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(kirill),
    # End reference.

    "damage": 99999,  # [Min, max]

    "cost": 80,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 1.0
}

leather_armor = {
    "id": "leather_armor",

    "name": "Leather Armor",

    "type": "Armor",

    "description": "It's leather. Ooooh, leather!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(leather_armor),

    "defense": 15,

    "cost": 50
}

wooden_armor = {
    "id": "wooden_armor",

    "name": "Wooden Armor",

    "type": "Armor",

    "description": "Wield the power of trees! All natural. Rather flammable.",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(wooden_armor),

    "defense": 20,

    "cost": 60
}

golden_armor = {
    "id": "golden_armor",

    "name": "Golden Armor",

    "type": "Armor",

    "description": "Well protected, but good luck running away with that weight!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(golden_armor),

    "defense": 35,

    "cost": 100
}

platinum_armor = {
    "id": "platinum_armor",

    "name": "Platinum Armor",

    "type": "Armor",

    "description": "Well that thing uses half the world's platinum resources. Better be worth it!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(platinum_armor),

    "defense": 50,

    "cost": 250
}

diamond_armor = {
    "id": "diamond_armor",

    "name": "Diamond Armor",

    "type": "Armor",

    "description": "You're basically a walking company bank account now. Good job!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(diamond_armor),

    "defense": 75,

    "cost": 500
}

ultimate_armor = {
    "id": "ultimate_armor",

    "name": "Ultimatanium Armor",

    "type": "Armor",

    "description": "I didn't know that stuff existed! Better than diamonds? That's a scientific breakthrough!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(ultimate_armor),

    "defense": 90,

    "cost": 1000
}

# It is of utmost importance that all dictionaries are saved within a list so that it is possible to call them
# using an index or a loop!
items = {
    "fists": no_weapon,

    "no armor": no_armor,

    "knife": knife,

    "bad_sword": bad_sword,

    "sword": sword,

    "new_sword": new_sword,

    "glowing_sword": glowing_sword,

    "old_hammer": old_hammer,

    "hammer": hammer,

    "kirill": kirill,

    "fire_hammer": fire_hammer,

    "lightsaber": lightsaber,

    "leather_armor": leather_armor,

    "wooden_armor": wooden_armor,

    "golden_armor": golden_armor,

    "platinum armor": platinum_armor,

    "diamond_armor": diamond_armor,

    "ultimate_armor": ultimate_armor,

}
