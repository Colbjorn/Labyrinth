# This module has all functions that are called when an interactable's contextual action is called.
from gameparser import normalise_input
from player import player


def story_npc_1():
    def skip():
        inpt = input("If you wish to skip the dialogue, SKIP now.")
        if len(inpt) == 0:
            pass
        elif normalise_input(inpt)[0] == "skip":
            print('''"Not much for exposition, are you?" The villager says, dejected. "Fine, here\'s your loot.
Go on now. Go beat the game since you're in such a rush."''')
            # TODO: GIVE REWARD.
            return True
    print('"Thank you for killing that monstrosity, strange traveller. Were it not for you, I may have died.')
    if not skip():
        print('''I have no idea what has been happening around here. I was just living life as usual until one day,
the sky went dark.''')
        input()
        print('''It was only for a second; my wife and children didn\'t even notice it. But ever since then, these creatures
have been appearing out of nowhere! Some didn\'t mind us. Some were like you, simply passersby. But others...''')
        input()
        print('''Others tried to kill us on sight, just like that one you saved us from. Not only that, but every step I
take further away from my farm might lead me to someplace completely different. I\'ve seen hells, tiny worlds,
been underwater and walked on clouds, all within just a few steps away from my house!''')
        input()
        print('''I don\'t know what to do... I fear for my family\'s safety. None of this makes sense! What did we do
to deserve this?!"''')
        input()
        print('''The man begins to sob, and as he does you notice a tear in the sky as if it had been slashed through
with a knife. It seems to be getting bigger. You try to look closer, through the tear. Suddenly, within a 
flash before your eyes, you are someplace else. Bright cosmic colors surround you. The ground below your feet, you 
notice, is gone. A million worlds are surrounding you; planets, galaxies, universes! Such a magnificent place, you 
wish you could observe it forever...''')
        input()
        print('''As soon as you realize your own thoughts, the colors begin to dim. A massive shadow dwarfing the limits of 
your very imagination begins to approach, and as it does all of the surrounding worlds, planets, galaxies begin to 
vanish, one by one, leaving no trace behind. The shadow notices you, and accelerates towards you at an unholy speed.
You hear a deafening ringing as the shadow completely envelops you, leaving you in absolute darkness...''')
        input()
        print('''You find yourself back at the farm. The villager is still sobbing before you, as if nothing had happened.
As his sobs slow down, he looks back up at you.''')
        input()
        print('''"Please. Please, try to find out what is happening. The world can\'t continue to exist like this, it just
can\'t! Here, I know it\'s not much, but I hope this helps"''')
    #TODO: Make a reward.

