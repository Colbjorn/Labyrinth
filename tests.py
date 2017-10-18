# For testing purposes.
import monsters
from player import player
from items import items

# The below is a crappy combat proof-of-concept in order to test/show that attacks work regardless of attacker/target.
current_enemy = monsters.goblin
current_enemy["health"] = current_enemy["max health"]
print(player["health"])

current_enemy["attacks"]["scratch"](current_enemy, player)

print(player["health"])
print(current_enemy["health"])
current_enemy["attacks"]["scratch"](player, current_enemy)
print(str(current_enemy["health"]) + "/" + str(current_enemy["max health"]))

print("Your inventory is " + str(player["inventory"]))
inpt = input("Use what?")
if inpt not in player["inventory"]:
    print("Don't have that!")
else:
    items[inpt]["on use"](items[inpt])
print(player["weapon"])
