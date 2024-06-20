def optellen(nummer1, nummer2):
    result = nummer1 + nummer2
    return (f"{nummer1} + {nummer2} = {result}") ,result

def aftrekken(nummer1, nummer2):
    result = nummer1 - nummer2
    return (f"{nummer1} - {nummer2} = {result}"), result

def keer(nummer1, nummer2):
    result = nummer1 * nummer2
    return (f"{nummer1} * {nummer2} = {result}"), result

def delen(nummer1, nummer2):
    result = nummer1 / nummer2
    return (f"{nummer1} / {nummer2} = {result}"), result

def ophogen(nummer1, nummer2):
    result = nummer1 + nummer2
    return (f"{nummer1} + {nummer2} = {result}"), result

def verlagen(nummer1, nummer2):
    result = nummer1 - nummer2
    return (f"{nummer1} - {nummer2} = {result}"), result

def verdubbelen(nummer1, nummer2):
    result = nummer1 * nummer2
    return (f"{nummer1} * {nummer2} = {result}"), result

def halveren(nummer1, nummer2):
    result = nummer1 / nummer2
    return (f"{nummer1} / {nummer2} = {result}"), result

def nummerV(nummer1):
    if nummer1 == None:
             while True:
                try:
                    nummer1 = float(input("welk getal? "))
                    break
                except:
                    print("geen geldig getal")
    return float(nummer1)

def nummerV2(nummer2):
    while True:
        try:
            nummer2 = float(input("welk getal? "))
            break
        except:
            print("geen geldig getal")
    return float(nummer2)