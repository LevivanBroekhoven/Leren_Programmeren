import random

namen_lijst = []
lootjes_trekken = False 

while not lootjes_trekken:
    naam = input("Voer een naam in: ")
    while True:
        if naam in namen_lijst:
            naam =input("Voer een nieuwe naam in ")
        else:
            namen_lijst.append(naam)
            break

    if len(namen_lijst) >= 3:
        lootjes_trekken = input("wilt u de lootjes trekken (j/n)") == 'j'

for naam in namen_lijst:
    print(naam)