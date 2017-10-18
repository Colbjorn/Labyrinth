# Might as well have a separate module for item effects!
from player import player


def equip(item):
    if item["id"] in player["inventory"]:
        if item["type"] == "Weapon":
            player["weapon"] = item["id"]
            player["inventory"].remove(item["id"])
        elif item["type"] == "Armor":
            player["armor"] = item["id"]
            player["inventory"].remove(item["id"])
        else:
            print("Cannot equip that!")
    else:
        print("You don't have that item!")

