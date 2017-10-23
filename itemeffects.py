# Might as well have a separate module for item effects!
from player import player


def equip(item):
    if item["id"] in player["inventory"]:
        if item["type"] == "Weapon":
            if player["weapon"] != None:# If a weapon is being held, it'll move to the inventory.
                player["inventory"].add(player["weapon"])
            player["weapon"] = item["id"]
            player["inventory"].remove(item["id"])
        elif item["type"] == "Armor":
            if player["armor"] != None:# If an armor is being warn, it'll move to the inventory.
                player["inventory"].add(player["armor"])
            player["armor"] = item["id"]
            player["inventory"].remove(item["id"])
        else:
            print("Cannot equip that!")
    else:
        print("You don't have that item!")

