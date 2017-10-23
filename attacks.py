# This module lists all attacks and spells monsters/the player can use.
import random

# self = enemy dictionary
# target = player dictionary


def scratch_attack(self, target):
    damage = random.randint(1, 3) + (self["attack"]*0.5)
    target["health"] -= damage
    # TODO: Decide on how armor will work (if applicable) and add an armor check to attacks.


def sword_attack(self, target):
    damage = random.randint(5, 8) + (self["attack"]*0.8)
    target["health"] -= damage
    print(self["name"], " is slashing you with a sword!")


def stun_attack(self, target):
    damage = random.randint(1, 5) + (self["attack"]*0.3)
    target["health"] -= damage
    print(self["name"], " has knocked you with a stun attack!")


def punch_attack(self, target):
    damage = random.randint(1, 3) + (self["attack"]*0.5)
    target["health"] -= damage
    print(self["name", " is punching you!"])


def throw_attack(self, target):
    damage = random.randint(1, 5) + (self["attack"]*0.3)
    target["health"] -= damage
    print(self["name"], " is throwing knives at you!")


def tail_attack(self, target):
    damage = random.rantint(1, 5) + (self["attack"]*0.5)
    target["health"] -= damage
    print(self["name"], " is tail-whipping you!")


def doubleslap_attack(self, target):  # either implement 2 times or modify health
    damage = random.randint(1, 5) + (self["attack"]*0.5)
    target["health"] -= damage
    print(self["name"], " is giving you a double slap!")


def fiveslap_no_jutsu_attack(self, target):
    damage = random.randint(1, 5) + (self["attack"]*0.5)  # either implement 5 times or modify health
    target["health"] -= damage
    print(self["name"], " is giving you a quintuple slap!")


def spit_attack(self, target):
    damage = random.randint(2, 4) + (self["attack"]*0.5)
    target["health"] -= damage
    print(self["name"], " is spitting acid at you!")


def stomp_attack(self, target):
    damage = random.randint(1, 6) + (self["attack"]*0.8)  # will change dramatically based on level/monster size
    target["health"] -= damage
    print(self["name"], " has stomped you into the ground!")


def summon_attack(self, target):
    damage = random.randint(2, 8) + (self["attack"]*0.5)
    target["health"] -= damage
    print(self["name"], " is summoning mini versions of themselves to attack you!")


def banter_attack(self, target):
    print(self["name"], " is annoying you with terrible banter. It does no damage, but you feel a loss in your will to live")
    # TODO: Make bants.


def bite_attack(self, target):
    damage = random.randint(2, 6) + (self["attack"]*0.7)
    target["health"] -= damage
    print(self["name"], " is biting into part of you. You manage to shove them off")