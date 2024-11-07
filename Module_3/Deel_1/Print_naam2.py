from Functions_naam import *
list = []

while True: 
    list.append(vragen())
    doorgaan = input("nog iemand? ")
    if doorgaan == "stop":
        break


for x in list:
    print(f"in {x['Woonplaats']} woont,de {x['leeftijd']} jarige {x['naam']}  ")

