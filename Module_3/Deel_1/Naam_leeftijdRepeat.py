list = []


def name():
    naam = input("Wat is je naam? ")
    return(naam)

def age():
    leeftijd = input("Wat is je leeftijd? ")
    return(leeftijd)

def vragen():
    naam = name()
    leeftijd = age()
    return{"naam":naam, "leeftijd":leeftijd}

while True: 
    list.append(vragen())
    doorgaan = input("nog iemand?")
    if doorgaan == "stop":
        break


for x in list:
    print(f"{x['naam']} is {x['leeftijd']} jaar oud")






