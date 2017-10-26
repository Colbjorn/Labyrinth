# This module has all functions that are called when an interactable's contextual action is called.
from gameparser import normalise_input
from player import *


def story_npc_1():
    def skip():
        inpt = input("If you wish to skip the dialogue, SKIP now.")
        if len(inpt) == 0:
            pass
        elif normalise_input(inpt)[0] == "skip":
            print('''"Not much for exposition, are you?" The villager says, dejected. "Fine, here\'s your loot.
Go on now. Go beat the game since you're in such a rush."''')
            print("Obtained a new sword!")
            modified_amount(player["inventory"], "new sword", "append")
            input()
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
        print("Obtained a new sword!")
        modified_amount(player["inventory"], "new sword", "append")
        input()


def story_npc_2():
    def skip():
        inpt = input("If you wish to skip the event, SKIP now.")
        if len(inpt) == 0:
            pass
        elif normalise_input(inpt)[0] == "skip":
            print('''Things happen and you find a thing.''')
            print("You Were Rewarded A Lightsaber")
            modified_amount(player["inventory"], "lightsaber", "append")
            input()
            return True
    print("You decide to approach the desk in order to read the notes spread on the table.")
    if not skip():
        print('''As you near the table, you glance at the glass dome at the table's center. You see within it, at its
center, a small table with an even smaller glass dome on it. There also seems to be a miniature person looking 
into the glass dome...''')
        input()
        print('''You suddenly feel like you are being watched, and you could swear that the room has just gotten
somewhat darker than it was before. You look above you and realize that the room is not a regular square
room; it is in fact a glass dome.''')
        input()
        print('''Towering above the dome is what seems to be a humanoid figure, currently looking up into the sky.
From its mannerisms, eerily similar to yours, you assume it is just as perplexed by its own situation as you are by
yours.''')
        input()
        print('''You decide to not give it much further thought, and turn back to the table to read some of the notes.
You spot from the corner of your eye that the figure outside has turned around towards your direction, and the
figure within the small dome has turned towards its own table. Rather than feeling like this situation doesn't make
sense, you feel like the very meaning of sense itself has just been lost to the ether. You proceed to read the notes.''')
        input()
        print('''Unfortunately due to how disorganized the author was, the notes are mostly written in a bullet
point format. The parts that stand out to you are as follows:''')
        input()
        print('''"EFFECT?
- Anomaly confirmed extradimensional
- Transdimensional effects directly observed
- Test successful
CONSEQUENCES?
- Merging
ENTITY POSSIBLY RESPONSIBLE??
- effects?
- entity
-entity
no no no no no"''')
        input()
        print('''The rest of the pages are either gibberish, illegible, or repetitions of the words "no", "death" and, for some reason,
"digestion". Buried underneath all the pages you notice a faint glimmer...''')
        print("You Were Rewarded A Lightsaber")
        modified_amount(player["inventory"], "lightsaber", "append")
        input()

def red_cross():
    def skip():
        inpt = input("If you wish to skip the dialogue, SKIP now.")
        if len(inpt) == 0:
            pass
        elif normalise_input(inpt)[0] == "skip":
            print('''since you're too lazy to dig for treasure, here's the loot.''')
            print("You Were Rewarded Golden Armor")
            modified_amount(player["inventory"], "golden armor", "append")
            return True
    if not skip():
        print('''"You begin to dig into the red cross. The sand was course and got everywhere, makeing it very difficult
to dig effectively. After some time, and a few breaks, you strike a large wooden chest. in the chest is a set of golden, glimmering armor.
This armor will deffinetly be effective in your travels.''')
        print("You Were Rewarded Golden Armor")
        modified_amount(player["inventory"], "golden armor", "append")
        input()


def door():
    def skip():
        inpt = input("If you wish to skip the dialogue, SKIP now.")
        if len(inpt) == 0:
            pass
        elif normalise_input(inpt)[0] == "skip":
            print('''you beat the game. It looks like you don't care so why should I?''')
            print("Congrats you ingrate")
            input()
            import sys
            sys.exit()
            return True
    if not skip():
        print('''You didn't want to leave. You have a duty to save these lands but you just aren't strong enough
your time in this place has been the worst time of your life. The monsters and terrifying and strong,
you've nearly died countless times. It's not your duty to save reality, it's someone better's duty.''')
        input()
        print("Congratulation!!! You've Survived! You can now return home and live the rest of you life in peace.")
        print("Hopefully Azgoth, Destroyer of worlds doesn't find your reality")
        input()
        import sys
        sys.exit()
