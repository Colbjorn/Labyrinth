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

    "rarity": 1,

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

    "cost": 0,

    "rarity": 1
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
    
    "rarity": 5,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.5
}

bad_sword = {  # Sample item subject to change
    "id": "knackered sword",

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

    "rarity": 5,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.6
}

sword = {  # Sample item subject to change
    "id": "sword",

    "name": "Sword",

    "type": "Weapon",

    "action": "slashing",

    "description": "A generic sword. Still coated with the fear of those slain by it. Or blood, that's also possible.",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(sword),
    # End reference.

    "damage": 20,  # [Min, max]

    "cost": 20,

    "rarity": 15,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.7
}

new_sword = {  # Sample item subject to change
    "id": "new sword",

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

    "rarity": 30,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.7
}

glowing_sword = {  # Sample item subject to change
    "id": "glowing sword",

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

    "rarity": 70,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.7
}

old_hammer = {  # Sample item subject to change
    "id": "old hammer",

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

    "rarity": 5,

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

    "rarity": 15,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.6
}

fire_hammer = {  # Sample item subject to change
    "id": "sulphuras",

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

    "rarity": 30,

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

    "rarity": 65,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 0.9
}

kirill = {  # Sample item subject to change
    "id": "kirill",

    "name": "Jeweled Sword of Kirill",

    "type": "Weapon",

    "action": "l33t h4xxing",

    "description": "l33t m4s3r h4x0r Kirill, hacks everything to death with them mad skillzZz.",

    "usage": "equip",

    # The below function was adapted from user Tony Veijalainen in a StackOverflow forum. Reference:
    # https://stackoverflow.com/questions/3738381/what-do-i-do-when-i-need-a-self-referential-dictionary
    # Accessed on 20/10/2017 at 11:15.
    "on use": lambda: itemeffects.equip(kirill),
    # End reference.

    "damage": 99999,  # [Min, max]

    "cost": 80,

    "rarity": 99,

    # Bonuses could be either additive or multiplicative (e.g. 1.5 bonus strength adds 1.5 x strength to damage)
    "bonus": 1.0
}

clothes = {
    "id": "clothes",

    "name": "Clothes",

    "type": "Armor",

    "description": "Ordinary set of clothing.",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(clothes),

    "defense": 1,

    "rarity": 1,

    "cost": 10
}

leather_armor = {
    "id": "leather armor",

    "name": "Leather Armor",

    "type": "Armor",

    "description": "It's leather. Ooooh, leather!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(leather_armor),

    "defense": 15,

    "cost": 50,
    
    "rarity": 15
}

wooden_armor = {
    "id": "wooden armor",

    "name": "Wooden Armor",

    "type": "Armor",

    "description": "Wield the power of trees! All natural. Rather flammable.",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(wooden_armor),

    "defense": 20,

    "cost": 60,

    "rarity": 25
}

golden_armor = {
    "id": "golden armor",

    "name": "Golden Armor",

    "type": "Armor",

    "description": "Well protected, but good luck running away with that weight!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(golden_armor),

    "defense": 35,

    "cost": 100,

    "rarity": 40
}

platinum_armor = {
    "id": "platinum armor",

    "name": "Platinum Armor",

    "type": "Armor",

    "description": "Well that thing uses half the world's platinum resources. Better be worth it!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(platinum_armor),

    "defense": 50,
    
    "rarity": 60,

    "cost": 250
}

diamond_armor = {
    "id": "diamond armor",

    "name": "Diamond Armor",

    "type": "Armor",

    "description": "You're basically a walking company bank account now. Good job!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(diamond_armor),

    "defense": 75,

    "rarity": 80,

    "cost": 500
}

ultimate_armor = {
    "id": "ultimatanium armor",

    "name": "Ultimatanium Armor",

    "type": "Armor",

    "description": "I didn't know that stuff existed! Better than diamonds? That's a scientific breakthrough!",

    "usage": "equip",

    "on use": lambda: itemeffects.equip(ultimate_armor),

    "defense": 80,

    "rarity": 99,

    "cost": 1000
}

health_potion = {
    "id": "health_potion",

    "name": "Health Potion",

    "type": "Consumable",

    "description": "Drink it and it'll somehow heal you",

    "usage": "heal",

    "on use": lambda: game.heal(health_potion, target),

    "heal": 25,

    "rarity": 50,

    "cost": 1000
}

# It is of utmost importance that all dictionaries are saved within a list so that it is possible to call them
# using an index or a loop!
items_dict = {
    "fists": no_weapon,

    "no armor": no_armor,

    "knife": knife,

    "knackered sword": bad_sword,

    "sword": sword,

    "new sword": new_sword,

    "glowing sword": glowing_sword,

    "old hammer": old_hammer,

    "hammer": hammer,

    "kirill": kirill,

    "sulphuras": fire_hammer,

    "lightsaber": lightsaber,

    "clothes": clothes,

    "leather armor": leather_armor,

    "wooden armor": wooden_armor,

    "golden armor": golden_armor,

    "platinum armor": platinum_armor,

    "diamond armor": diamond_armor,

    "ultimatanium armor": ultimate_armor,

    "health potion": health_potion

}

items_list = [
    knife,

    health_potion,

    leather_armor,
    
    bad_sword,
    
    sword,

    new_sword,
    
    glowing_sword,
    
    old_hammer,
    
    hammer,
    
    kirill,
    
    fire_hammer,
    
    lightsaber,
    
    clothes,
    
    leather_armor,
    
    wooden_armor,
    
    golden_armor,
    
    platinum_armor,
    
    diamond_armor,
    
    ultimate_armor,
    
    health_potion
]
