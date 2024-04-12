boodschappen = []
Aantal = []


while True:
    artikel = input("Welk artikel wilt u toevoegen? ")
    aantal = input(f"Hoeveel {artikel} wilt u toevoegen? ")
    if artikel not in boodschappen:
        Opslag1 = artikel
        Opslag2 = aantal
        boodschappen.append(Opslag1)
        Aantal.append(Opslag2)


    else:
        index = boodschappen.index(artikel)
        Aantal[index] = str(int(aantal[index]) + int(aantal))


    keuze = input("Wilt u nog iets toevoegen? (ja/nee) ")
    if keuze.lower() != "ja":
        break

print("___[BOODSCHAPPENLIJST]___")

for i in range(len(boodschappen)):
            print(f"{Aantal[i]}x {boodschappen[i]} ")
print("_________________________")
    