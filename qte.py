import time
import string
import random


def qte(butn, tim):
    start = time.time()
    hit = input('Hit ' + butn + '! ').lower()
    end = time.time()
    success = False
    if hit == butn and (end-start)<tim:
        success = True
    if success == True:
        print('Success!')
    else:
        print('Fail!')
    return success


def random_qte(tim):
    chars = string.ascii_lowercase
    choice = random.choice(chars)
    qte(choice, tim)
