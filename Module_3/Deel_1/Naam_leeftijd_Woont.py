list = []


def name():
    naam = input("Wat is je naam? ")
    return(naam)

def age():
    leeftijd = input("Wat is je leeftijd? ")
    return(leeftijd)

def living_place():
    woonplaats = input("Waar woon je? ")
    return(woonplaats)

def vragen():
    naam = name()
    leeftijd = age()
    woonplaats = living_place()
    return{"naam":naam, "leeftijd":leeftijd, "Woon":woonplaats}

while True: 
    list.append(vragen())
    doorgaan = input("nog iemand?")
    if doorgaan == "stop":
        break


for x in list:
    print(f"{x['naam']} die in {x['Woon']} woont, is {x['leeftijd']}  jaar oud")



