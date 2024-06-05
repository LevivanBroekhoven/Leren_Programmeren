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
    




