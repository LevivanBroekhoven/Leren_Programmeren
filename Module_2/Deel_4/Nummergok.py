import random 
ronde = 0
aantalgok = 0
punten = 0

while ronde < 20:
    getal = random.randint(1, 1000)

    if aantalgok == 10:
        print()
        print("Te vaak fout gegokt, ronde geëindigd")
        doorgaan = input("Wil je doorgaan?2 ")
        if doorgaan.lower() == "ja":
            ()
        else:
            print(f"Aantal punten {punten}")
            exit()

    aantalgok = 0
    ronde += 1
 
    while aantalgok < 10:
        print()
        print(f"ronde {ronde}")
        gok = int(input("getal "))

        if gok == getal:
            punten += 1
            print("Geraden")
            print(f"punten {punten}")
            break

        else:
            print("fout")
            verschil = getal - gok
            print(verschil)
            if verschil < 20:
                print("heel warm")
            elif verschil < 50:
                print("warm")
            aantalgok += 1

    if ronde != 20 and aantalgok != 10:
        doorgaan = input("Wil je doorgaan?1 ")
        if doorgaan.lower() != "ja":
            print(f"Aantal punten {punten}")
            exit()

print()
print(f"Aantal punten {punten}")