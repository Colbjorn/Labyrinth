# This module lists all monsters and their relevant details.
import attacks


goblin = {  # Sample monster subject to change.
    "name": "Goblin",

    "description": "An ugly green creature.",

    "level": 1,

    # Monsters currently only store max health because of the TODO below.
    "max health": 15,  # TODO: Might be a good idea to have monster current health stored in the combat function.
    # The above is in order to make it so new monsters always start at max health, and for easier tracking.

    "attack": 0.3,

    "status effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack,
        "doubleslap": attacks.doubleslap_attack,
        "5slap": attacks.fiveslap_attack,
    },

    "loot": [],

    "experience": 20,

    "gold": 5,
}

skeleton = {
    "name": "Skeleton",

    "description": "Could do with gaining a few pounds.",

    "level": 1,

    "max health": 8,

    "attack": 0.3,

    "status effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack,
        "stun": attacks.stun_attack,
        "sword": attacks.sword_attack,
        "banter": attacks.banter_attack,
        "summon": attacks.summon_attack,
    },

    "loot": [],

    "experience": 15,

    "gold": 5,
}

slime = {
    
    "name": "Slime",

    "description": "A foul-smelling blob of protoplasm.",

    "level": 1,

    "max health": 5,

    "attack": 0.2,

    "status_effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack,
        "summon": attacks.summon_attack,
        "stomp": attacks.stomp_attack,
        "spit_a": attacks.spit_acid_attack,
    },

    "loot": [],

    "experience": 10,

    "gold": 4,
}

zombie = {
    
    "name": "Zombie",

    "description": "A shambling pile of rotten flesh.",

    "level": 2,

    "max health": 20,

    "attack": 0.4,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "bite": attacks.bite_attack,
        "scratch": attacks.scratch_attack,
    },

    "loot": [],

    "experience": 25,

    "gold": 8,
}

orc = {
    
    "name": "Orc",

    "description": "A goblin with too much testosterone.",

    "level": 2,

    "max health": 12,

    "attack": 0.4,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "sword": attacks.sword_attack,
        "scratch": attacks.scratch_attack,
        "2slap": attacks.doubleslap_attack,
        "5slap": attacks.fiveslap_attack,
        "scream": attacks.scream_attack,

    },

    "loot": [],

    "experience": 30,

    "gold": 8,
}

ogre = {
    
    "name": "Ogre",

    "description": "A large dim looking humanoid.",

    "level": 2,

    "max health": 20,

    "attack": 0.5,

    "status_effects": [],

    "attacks": {
        "scratch": attacks.scratch_attack,
        "stun": attacks.stun_attack,
        "punch": attacks.punch_attack,
        "scream": attacks.scream_attack,
    },

    "loot": [],

    "experience": 35,

    "gold": 10,
}

evil_unicorn = {
    
    "name": "Evil Unicorn",

    "description": "A unicorn with a blackened heart.",

    "level": 3,

    "max health": 25,

    "attack": 0.5,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "rainbow": attacks.rainbow_attack,
        "bite": attacks.bite_attack,
        "spit_a": attacks.spit_acid_attack,
    },

    "loot": [],

    "experience": 30,

    "gold": 10,
}

gang_of_bandits = {
    
    "name": "Gang of Bandits",

    "description": "A gang of tough-looking criminals.",

    "level": 3,

    "max health": 45,

    "attack": 0.6,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "sword": attacks.sword_attack,
        "bite": attacks.bite_attack,
        "scratch": attacks.scratch_attack,
        "2slap": attacks.doubleslap_attack,
        "5slap": attacks.fiveslap_attack,
    },

    "loot": [],

    "experience": 60,

    "gold": 15,
}

dragon = {

    "name": "Dragon",

    "description": "It's a dragon! I'd recommend running, but that command doesn't exist.",

    "level": 5,

    "max health": 100,

    "attack": 0.9,

    "status_effects": [],

    "attacks": {
        "punch": attacks.punch_attack,
        "bite": attacks.bite_attack,
        "scratch": attacks.scratch_attack,
        "stomp": attacks.stomp_attack,
        "spit_a": attacks.spit_acid_attack,
        "spit_f": attacks.spit_fire_attack,
        "tail": attacks.tail_attack,
        "summon": attacks.summon_attack,
        "scream": attacks.scream_attack,
    },

    "loot": [],

    "experience": 100,

    "gold": 20,
}


# Important! In order for optimization to be implemented later on, keep the below list ordered by level.
monsters = [goblin, skeleton, slime, zombie, orc, ogre, evil_unicorn, gang_of_bandits, dragon]
