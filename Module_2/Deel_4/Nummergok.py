import random 
ronde = 0
aantalgok = 0
punten = 0

while ronde < 3:
    getal = random.randint(1, 3)

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
            aantalgok += 1

    if ronde != 3 and aantalgok != 10:
        doorgaan = input("Wil je doorgaan?1 ")
        if doorgaan.lower() != "ja":
            print(f"Aantal punten {punten}")
            exit()

print()
print(f"Aantal punten {punten}")