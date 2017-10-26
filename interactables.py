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