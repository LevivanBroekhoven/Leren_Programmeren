import random
nummers = (1,2,3,4,5,6)

def numbergen():
    randomnummer = random.choice(nummers)
    return randomnummer

def fivenumbergen():
    numberslist = []
    for x in range(5):
        randomnummer = random.choice(nummers)
        numberslist.append(randomnummer)
    return numberslist
