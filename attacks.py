# This module lists all attacks and spells monsters/the player can use.
import random
from items import * #allows fetching damage of player's items from different file
from player import * #allows fetching player's current weapon
from qte import random_qte

# self = enemy dictionary
# target = player dictionary
# Physical attacks are reduced by (defense)%. Anything that seems like it wouldn't be affected by armor isn't.

##### ENEMY ATTACKS #####
def scratch_attack(self, target):
    damage = random.randint(1, 3) + (self["attack"]*0.5)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is scratching", target["name"], "! They've taken", damage, "damage.")
    # TODO: Decide on how armor will work (if applicable) and add an armor check to attacks.


def sword_attack(self, target):
    damage = random.randint(5,8) + (self["attack"]*0.8)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is slashing", target["name"], "with a sword! They've taken", damage, "damage.")


def stun_attack(self, target):
    damage = random.randint(1,5) + (self["attack"]*0.3)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "has knocked", target["name"], "with a stun attack! They've taken", damage, "damage.")


def punch_attack(self, target):
    damage = random.randint(1,3) + (self["attack"]*0.5)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name", "is punching", target["name"], "! They've taken", damage, "damage."])


def throw_attack(self, target):
    damage = random.randint(1,5) + (self["attack"]*0.3)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is throwing knives at", target["name"], "! They've taken", damage, "damage.")


def tail_attack(self, target):
    damage = random.randint(1,5) + (self["attack"]*0.5)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is tail-whipping", target["name"], "! They've taken", damage, "damage.")


def doubleslap_attack(self, target): # either implement 2 times or modify health
    for x in range (2):
        damage = random.randint(2,4) + (self["attack"]*0.6)
        target["health"] -= (damage * (1 - player["defense"]/100))
        print(self["name"], "is giving", target["name"], "a slap! They've taken", damage, "damage.")
    print(self["name"], "gave", target["name"], "a double slap!")


def fiveslap_attack(self, target): # either implement 5 times or modify health
    for x in range (5):
        damage = random.randint(1,3) + (self["attack"]*0.3)
        target["health"] -= (damage * (1 - player["defense"]/100))
        print(self["name"], "is giving", target["name"], "a slap! They've taken", damage, "damage.")
    print(self["name"], "gave", target["name"], "a quintuple slap!")


def spit_acid_attack(self, target):
    damage = random.randint(2,4) + (self["attack"]*0.5)
    target["health"] -= damage
    print(self["name"], "is spitting acid at", target["name"], "! They've taken", damage, "damage.")


def spit_fire_attack(self, target):
    damage = random.randint(4,9) + (self["attack"]*0.8)
    target["health"] -= damage
    print(self["name"], "is spitting fire at", target["name"], "! They've taken", damage, "damage.")


def stomp_attack(self, target):
    damage = random.randint(1,6) + (self["attack"]*0.8)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "has stomped", target["name"], "into the ground! They've taken", damage, "damage.")


def summon_attack(self, target):
    damage = random.randint(2,8) + (self["attack"]*0.5)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is summoning mini versions of themselves to attack", target["name"], "! They've taken", damage, "damage.")


def banter_attack(self, target):
    print(self["name"], "is annoying", target["name"], "with terrible banter. It does no damage, but they feel a loss in their will to live.")


def bite_attack(self, target):
    damage = random.randint(2,6) + (self["attack"]*0.7)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is biting into part of", target["name"], "! They manage to shove them off. They've taken", damage, "damage.")


def rainbow_attack(self, target):
    damage = random.randint(3,7) + (self["attack"]*0.5)
    target["health"] -= (damage * (1 - player["defense"]/100))
    print(self["name"], "is firing the power of rainbows to", target["name"], "! They've taken", damage, "damage. Don't do drugs kids!")


def scream_attack(self, target):
    damage = random.randint(2,4) + (self["attack"]*0.3)
    target["health"] -= damage
    print(self["name"], "is rupturing", target["name"] + "'s ears & insides by screaming! They've taken"), damage, "damage."


def qte_kamehameha(self, target):
    print(self["name"], "is preparing a laser attack!", target["name"], "has to dodge!")
    input()
    dodge = random_qte(3)
    if dodge:
        print(target["name"], "dodged it!")
    else:
        damage = random.randint(20, 25) + self["attack"]
        target["health"] -= damage


def qte_cosmic_slap(self, target):
    print(self["name"], "prepares to slap", target["name"], "with the fury of a thousand suns!")
    input()
    dodge = random_qte(1)
    if dodge:
        print(target["name"], "dodged it!")
    else:
        damage = random.randint(15, 20) + (self["attack"]*0.5)
        target["health"] -= (damage * (1 - player["defense"]/100))


##### PLAYER ATTACKS #####
def p_attack(self, target, weapon):
    # lookup weapon name passed to function on items.py and retrieve it's name and damage
    damage = items_dict[weapon]["damage"] + (self["attack"]*items_dict[weapon]["bonus"])
    target["health"] -= damage
    print(self["name"], "is", items_dict[weapon]["action"], target["name"], "with", items_dict[weapon]["name"] + ", dealing",
          str(damage), "damage!")
