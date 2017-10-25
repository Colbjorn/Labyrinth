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
    if success:
        print('Success!')
    else:
        print('Fail!')
    return success


def random_qte(tim):
    # This function makes the QTE function use a random character for success.
    # Reference:
    # https://stackoverflow.com/questions/16060899/alphabet-range-python
    chars = string.ascii_lowercase
    # End reference.
    choice = random.choice(chars)
    qte(choice, tim)
