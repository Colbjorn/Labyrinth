# This module lists all attacks and spells monsters/the player can use.
import random


def scratch_attack(self, target):
    damage = random.randint(1, 3) + (self["attack"]*0.5)
    target["health"] -= damage
    # TODO: Decide on how armor will work (if applicable) and add an armor check to attacks.
