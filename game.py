# Main game loop.
import monsters
from player import player

# The below is a crappy combat proof-of-concept in order to test/show that attacks work regardless of attacker/target.
current_enemy = monsters.goblin
current_enemy["health"] = current_enemy["max health"]
print(player["health"])

current_enemy["attacks"]["scratch"](current_enemy, player)

print(player["health"])
print(current_enemy["health"])
current_enemy["attacks"]["scratch"](player, current_enemy)
print(str(current_enemy["health"]) + "/" + str(current_enemy["max health"]))
