# Tracks player's stats.

name = ""  # Inputted by player at start of game.

# TODO: Make sure the following are printed every turn.
location = [0, 0]
max_health = 20  # TODO: Balance this with weapons and monsters!
current_health = 20
max_mana = 10  # Can be any other secondary resource, or none at all!
current_mana = 10

# Revise stats, see if they make sense.
strength = 5  # Maybe could modify during a character creator?
dexterity = 5
constitution = 5
will = 5

weapon = None
armor = None
inventory = []  # Simply add in item objects imported from items.py.
spells = []  # Same as items.
