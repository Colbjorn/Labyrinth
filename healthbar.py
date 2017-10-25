def call_health(health, maxhealth):
    print('HP: [' + '#'*int(health/2) + ' '*int((maxhealth-health)/2) + ']' + ' ' + str(health) + '/' + str(maxhealth))


def call_mana(mana, maxmana):
    print('MP: [' + 'O' * int(mana/5) + ' ' * int((maxmana - mana)/5) + ']' + ' ' + str(
        mana) + '/' + str(maxmana))


def call_stats(health, maxhealth, mana, maxmana):
    call_health(health, maxhealth)
    call_mana(mana, maxmana)

