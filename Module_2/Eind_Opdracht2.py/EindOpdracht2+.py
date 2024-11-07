from random import *
import random
namen_lijst = []
namen_lijst_copy = []
lootjes_trekken = False 
zien = True

while not lootjes_trekken:
    naam = input("Voer een naam in: ")
    while True:
        if naam in namen_lijst:
            naam = input("Voer een nieuwe naam in: ")
        else:
            namen_lijst.append(naam)  
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
            print(f"{naam} heeft {assigned_naam}")
            
            zien = input("wil je nog een zien? (j/n) ") == "j"
                 