from Functions_naam import *
list = []

while True: 
    list.append(vragen())
    doorgaan = input("nog iemand? ")
    if doorgaan == "stop":
        break


for x in list:
    print(f"{x['naam']} die in {x['Woon']} woont, is {x['leeftijd']}  jaar oud")

