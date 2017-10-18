# This module lists all attacks monsters can use.
import random


def scratch_attack(self, target):
    damage = random.randint(1, 3) + (self["strength"]*0.5)
    target["health"] -= damage
