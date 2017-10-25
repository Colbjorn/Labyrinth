def call_health(health, maxhealth):
    print('HP: [' + '#'*int(health/2) + ' '*int((maxhealth-health)/2) + ']' + ' ' + str(health) + '/' + str(maxhealth))


def call_exp(exp, nxtlvl):
    print('EXP: [' + '|' * int(exp/5) + ' ' * int((nxtlvl - exp)/5) + ']' + ' ' + str(
        exp) + '/' + str(nxtlvl))


def call_stats(health, maxhealth, exp, nxtlvl):
    call_health(health, maxhealth)
    call_exp(exp, nxtlvl)
