# This module lists all monsters and their relevant details.
import attacks
from player import player

goblin = {  # Sample monster subject to change.
    "name": "Goblin",

    "description": "",

    "level": 1,

    # Monsters currently only store max health because of the TODO below.
    "max health": 15,  # TODO: Might be a good idea to have monster current health stored in the combat function.
    # The above is in order to make it so new monsters always start at max health, and for easier tracking.

    "attack": 0,

    "status effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack
    },

    "loot": [],

    "experience": 20
}

skeleton = {
    "name": "Skeleton",

    "description": "",

    "level": 1,

    "max health": 8,

    "status effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack,
        "stun": attacks.stun_attack
    },

    "loot": [],

    "experience": 15
}

slime = {
    
    "name": "Slime",

    "description": "",

    "level": 1,

    "max health": 5,

    "status_effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack
    },

    "loot": [],

    "experience": 10
}

zombie = {
    
    "name": "Zombie",

    "description": "",

    "level": 2,

    "max health": 20,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack
    },

    "loot": [],

    "experience": 25
}

orc = {
    
    "name": "ORc",

    "description": "",

    "level": 2,

    "max health": 12,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "sword": attacks.sword_attack
    },

    "loot": [],

    "experience": 30
}

ogre = {
    
    "name": "Ogre",

    "description": "",

    "level": 2,

    "max health": 20,

    "status_effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack,
        "stun": attacks.stun_attack,
        "punch": attacks.punch_attack
    },

    "loot": [],

    "experience": 35
}

evil_unicorn = {
    
    "name": "Evil Unicorn"

    "description": "",

    "level": 3,

    "max health": 25,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack
    },

    "loot": [],

    "experience": 30
}

gang_of_bandits = {
    
    "name": "Gang of Bandits",

    "description": "",

    "level": 3,

    "max health": 45,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "sword": attacks.sword_attack

    },

    "loot": [],

    "experience": 60
}



# Important! In order for optimization to be implemented later on, keep the below list ordered by level.
monsters = [goblin, skeleton, slime, zombie, orc, ogre, evil_unicorn, gang_of_bandits]
