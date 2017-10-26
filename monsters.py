# This module lists all monsters and their relevant details.
import attacks
import items


goblin = {  # Sample monster subject to change.
    "name": "Goblin",

    "description": "An ugly green creature.",

    "level": 1,

    "max health": 15,
    # Monsters will always set their (current) health equal to the max at the beginning of combat.

    "attack": 0,

    "status effects": [],

    "attacks": [  # Nerf this shit it's 2stronk4me
        attacks.scratch_attack,
        attacks.doubleslap_attack,
        attacks.fiveslap_attack,
    ],

    "loot": [
	    items.bad_sword,
	    items.old_hammer,
    ],

    "experience": 5,

    "gold": 5,
}

skeleton = {
    "name": "Skeleton",

    "description": "Could do with gaining a few pounds.",

    "level": 1,

    "max health": 8,

    "attack": 2,

    "status effects": [],

    "attacks": [
        attacks.scratch_attack,
        attacks.stun_attack,
        attacks.sword_attack,
        attacks.banter_attack,
        attacks.summon_attack,
    ],

    "loot": [
	    items.bad_sword,
	    items.old_hammer,
	    items.leather_armor
    ],

    "experience": 15,

    "gold": 10
}

slime = {
    
    "name": "Slime",

    "description": "A foul-smelling blob of protoplasm.",

    "level": 1,

    "max health": 5,

    "attack": 2,

    "status_effects": [],

    "attacks": [
        attacks.scratch_attack,
        attacks.summon_attack,
        attacks.stomp_attack,
        attacks.spit_acid_attack,
    ],

    "loot": [
	    items.leather_armor,
	    items.bad_sword,
    ],

    "experience": 10,

    "gold": 4,
}

zombie = {
    
    "name": "Zombie",

    "description": "A shambling pile of rotten flesh.",

    "level": 2,

    "max health": 20,

    "attack": 4,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.bite_attack,
        attacks.scratch_attack,
    ],

    "loot": [
        items.sword,
        items.hammer,
        items.wooden_armor,
    ],

    "experience": 25,

    "gold": 8,
}

orc = {
    
    "name": "Orc",

    "description": "A goblin with too much testosterone.",

    "level": 2,

    "max health": 12,

    "attack": 4,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.sword_attack,
        attacks.scratch_attack,
        attacks.doubleslap_attack,
        attacks.fiveslap_attack,
        attacks.scream_attack,
    ],

    "loot": [
        items.sword,
        items.hammer,
        items.wooden_armor,
    ],

    "experience": 30,

    "gold": 8,
}

ogre = {
    
    "name": "Ogre",

    "description": "A large dim looking humanoid.",

    "level": 2,

    "max health": 20,

    "attack": 5,

    "status_effects": [],

    "attacks": [
        attacks.scratch_attack,
        attacks.stun_attack,
        attacks.punch_attack,
        attacks.scream_attack,
    ],

    "loot": [
        items.sword,
        items.hammer,
        items.wooden_armor,
    ],

    "experience": 35,

    "gold": 10,
}

evil_unicorn = {
    
    "name": "Evil Unicorn",

    "description": "A unicorn with a blackened heart.",

    "level": 3,

    "max health": 25,

    "attack": 5,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.rainbow_attack,
        attacks.bite_attack,
        attacks.spit_acid_attack,
    ],

    "loot": [
        items.golden_armor,
	    items.sword,
    ],

    "experience": 30,

    "gold": 10,
}

gang_of_bandits = {
    
    "name": "Gang of Bandits",

    "description": "A gang of tough-looking criminals.",

    "level": 3,

    "max health": 45,

    "attack": 6,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.sword_attack,
        attacks.bite_attack,
        attacks.scratch_attack,
        attacks.doubleslap_attack,
        attacks.fiveslap_attack,
        attacks.banter_attack,
    ],

    "loot": [
        items.golden_armor,
	    items.sword,
    ],

    "experience": 60,

    "gold": 15,
}

ninja = {

    "name": "Ninja",

    "description": "A real ninja! From one of the finest training grounds, apparently.",

    "level": 4,

    "max health": 50,

    "attack": 0.6,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.sword_attack,
        attacks.bite_attack,
        attacks.scratch_attack,
        attacks.doubleslap_attack,
        attacks.fiveslap_attack,
        attacks.scream_attack,
        attacks.summon_attack,
        attacks.stomp_attack,
    ],

    "loot": [
        items.golden_armor,
        items.new_sword,
    ],

    "experience": 60,

    "gold": 18,
}

devil_cat = {

    "name": "The Devil's Cat",

    "description": "All the things you wished your cat wouldn't do.",

    "level": 6,

    "max health": 40,

    "attack": 6,

    "status_effects": [],

    "attacks": [
        attacks.bite_attack,
        attacks.scratch_attack,
        attacks.summon_attack,
        attacks.scream_attack,
        attacks.spit_fire_attack,
        attacks.tail_attack,
        attacks.banter_attack,
    ],

    "loot": [
        items.fire_hammer,
        items.platinum_armor,
    ],

    "experience": 60,

    "gold": 15,
}

dragon = {

    "name": "Dragon",

    "description": "It's a dragon! I'd recommend running...",

    "level": 5,

    "max health": 100,

    "attack": 9,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.bite_attack,
        attacks.scratch_attack,
        attacks.stomp_attack,
        attacks.spit_acid_attack,
        attacks.spit_fire_attack,
        attacks.tail_attack,
        attacks.summon_attack,
        attacks.scream_attack,
    ],

    "loot": [
        items.diamond_armor,
        items.new_sword,
    ],

    "experience": 100,

    "gold": 20,
}

giant_dragon = {

    "name": "Giant Dragon",

    "description": "It's a giant dragon! Yeah, I'd certainly try running now...",

    "level": 10,

    "max health": 160,

    "attack": 20,

    "status_effects": [],

    "attacks": [
        attacks.punch_attack,
        attacks.bite_attack,
        attacks.scratch_attack,
        attacks.stomp_attack,
        attacks.spit_acid_attack,
        attacks.spit_fire_attack,
        attacks.tail_attack,
        attacks.summon_attack,
        attacks.scream_attack,
    ],

    "loot": [
        items.ultimate_armor,
        items.lightsaber,
    ],

    "experience": 200,

    "gold": 30,
}

azgoth = {
    "Name": "Azgoth, Devourer of Worlds",

    "description": """The 37-dimensional being that started it all is before you. It almost looks serene.
    You cannot understand its very existence. All you know is the motivation within you to end this once and for all.""",

    "level": 20,

    "max health": 500,

    "attack": 50,

    "status effects": [],

    "attacks": [
        attacks.stomp_attack,
        attacks.spit_fire_attack,
        attacks.summon_attack,
        attacks.qte_cosmic_slap,
        attacks.qte_kamehameha
    ],

    "loot": [items.kirill],

    "experience": 0,

    "gold": 0
}
# Important! In order for optimization to be implemented later on, keep the below list ordered by level.
monsters = [goblin, skeleton, slime, zombie, orc, ogre, evil_unicorn, gang_of_bandits, ninja, devil_cat, dragon, giant_dragon]
