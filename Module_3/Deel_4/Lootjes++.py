from random import *
import random
namen_lijst = []
namen_lijst_copy = []
lootjes_trekken = False 
zien = True
itemslijst = []

while not lootjes_trekken:
    naam = input("Voer een naam in: ")
    while True:
        if naam in namen_lijst:
            naam = input("Voer een nieuwe naam in: ")
        else:
            namen_lijst.append(naam)
            items = []
            items.append(naam)
            for x in range(3):
                item = input("welke 3 items wil je? ")
                items.append(item)

            itemslijst.append(items)


            break

    if len(namen_lijst) >= 3:
        lootjes_trekken = input("Wilt u de lootjes trekken (j/n): ") == 'j'

while True:
    namen_lijst_copy = namen_lijst[:]
    random.shuffle(namen_lijst_copy)    
    
    lootjes = {}
    werkt = True
    
    for naam in range(len(namen_lijst)):
        if namen_lijst[naam] == namen_lijst_copy[naam]:
            werkt = False
            break
        lootjes[namen_lijst[naam]] = namen_lijst_copy[naam]

    if werkt:
        break



while zien:
    welkezien = input("welke wil je zien? ")

    for naam, assigned_naam in lootjes.items():
        if naam == welkezien:
            print(f"{naam} heeft {assigned_naam} en die wilt graag")

            for items in itemslijst:
                if items[0] == assigned_naam:
                    for item in items[1:]:
                        print(item)
                    break

            zien = input("wil je nog een zien? (j/n) ") == "j"
                 