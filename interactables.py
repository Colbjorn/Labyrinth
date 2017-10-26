# This module lists all the interactables the player can interact with.
import interactable_effects


story_npc_1 = {
    "description": "You see a villager looking carefully at you. He seems thankful.",

    "context action": "talk",

    "context result": interactable_effects.story_npc_1,

    "used": False
}

story_npc_2 = {
    "description": "The papers on the desk tempt you to read them.",

    "context action": "inspect",

    "context result": interactable_effects.story_npc_2,

    "used": False
}

red_cross = {
    "description": "The red cross look extremely digable",

    "context action": "dig",

    "context result": interactable_effects.red_cross,

    "used": False
}

door = {
    "description": "The door is open. You know this door will lead you home.",

    "context action": "leave",

    "context result": interactable_effects.door,

    "used": False
}
