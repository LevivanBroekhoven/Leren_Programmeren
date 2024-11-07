list = []


def vragen():
    dict = {}
    dict['naam']= input("Wat is je naam? ")
    dict["leeftijd"] = input("Wat is je leeftijd? ")
    dict["Woonplaats"] = input("Waar woon je? ")

    return dict

while True: 
    list.append(vragen())
    doorgaan = input("nog iemand?")
    if doorgaan == "stop":
        break


for x in list:
    print(f"{x['naam']} die in {x['Woonplaats']} woont, is {x['leeftijd']}  jaar oud")



