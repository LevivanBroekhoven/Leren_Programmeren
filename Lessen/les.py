lijst = []


for _ in range (2):
    auto = {}
    auto["merk"] = input("Merk ")
    auto["model"] = input("Model ")
    auto["prijs"] = input("prijs ")
    lijst.append(auto)


for x in lijst:
  print(x["prijs"])


Leeftijd = int(input)