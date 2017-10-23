# This module lists all attacks and spells monsters/the player can use.
import random


def scratch_attack(self, target):
    damage = random.randint(1, 3) + (self["attack"]*0.5)
    target["health"] -= damage
    # TODO: Decide on how armor will work (if applicable) and add an armor check to attacks.

def sword_attack(self, target):
    damage = random.randint(5,8) + (self["attack"]*0.8)
    target["health"] -= damage

def stun_attack(self, target):
    damage = random.randint(1,5) + (self["attack"]*0.3)
    target["health"] -= damage

def punch_attack(self, target):
    damage = random.randint(3,7) + (self["attack"]*0.5)
    target["health"] -= damage

def throw_attack(self, target):
    damage = random.randint(1,5) + (self["attack"]*0.3)
    target["health"] -= damage