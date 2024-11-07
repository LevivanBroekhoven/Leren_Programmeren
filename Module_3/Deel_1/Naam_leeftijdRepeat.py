list = []


def vragen():
    dict = {}
    dict['naam']= input("Wat is je naam? ")
    dict["leeftijd"] = input("Wat is je leeftijd? ")
    return dict

while True: 
    list.append(vragen())
    doorgaan = input("nog iemand?")
    if doorgaan == "stop":
        break


for x in list:
    print(x)






