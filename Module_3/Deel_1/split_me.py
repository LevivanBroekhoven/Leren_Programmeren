from collections import Counter
import math, random

getallen = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3

def aantal (getallen):
    aantal = len(getallen)
    return aantal

def som_alle_getalen(getallen):
    som = sum(getallen)
    return som

def gemiddelde(som, aantal):
    gemiddelde = som / aantal
    return(gemiddelde)

def grootste_getal(getallen):
    grootste_getal = max(getallen)
    return(grootste_getal)

def kleinste_getal(getallen):
    kleinste_getal = min(getallen)
    return(kleinste_getal)

def eerste_getal(getallen):
    eerste_getal = getallen[0]
    return(eerste_getal)

def delen_controlgetal1(kleinste_getal, controlgetal1):
    delen1 = kleinste_getal / controlgetal1
    return delen1

def delen_controlgetal2(kleinste_getal, controlgetal2):
    delen1 = kleinste_getal / controlgetal2
    return delen1

def aantal_elementen (getallen):
    aantal_elementen = len(getallen)
    return aantal_elementen

def unieke_getallen_selecteren(getallen):
    unieke_getallen = list(set(getallen))
    return unieke_getallen

def verschil_tussen_elementen(aantal_unieke_elementen , controlegetal1):
    verschil1 = abs(aantal_unieke_elementen - controlegetal1)
    return verschil1

def gesorteerde_lijst(getallen):
    gesorteerde_lijst = sorted(getallen)
    return gesorteerde_lijst

def shuffle_lijst(getallen):
    random.shuffle(getallen)
    return (getallen)

def random_getal(getallen):
    random_getal = getallen[random.randint(0,len(getallen)-1)]
    return random_getal

def verschil_tussen_getallen(random_getal):
   verschil2 = abs(random_getal - controlegetal2)
   return verschil2

def tel_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return(telling_elementen)

def komtvoor(getallen):
   komtvoor = controlegetal1 in getallen and controlegetal2 in getallen
   return komtvoor

def standaardafwijking(gemiddelde , getallen , aantal):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def posities(getallen):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def deelbaardoor1(getallen):
    deelbaar1 = []
    for getal in getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return(deelbaar1)

def deelbaardoor2(getallen):
    deelbaar2 = []
    for getal in getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return(deelbaar2)


getal = random_getal(getallen)
def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}
    
    resultaten = {
        "Aantal getallen": len(getallen),
        "Gemiddelde": gemiddelde(som_alle_getalen(getallen), len(getallen)),
        "Som": som_alle_getalen(getallen),
        "Grootste getal": grootste_getal(getallen),
        "Kleinste getal": kleinste_getal(getallen),
        "Eerste getal": eerste_getal(getallen),
        f"{kleinste_getal(getallen)} / {controlegetal1}":delen_controlgetal1(kleinste_getal(getallen),controlegetal1),
        f"{grootste_getal(getallen)} / {controlegetal2}":delen_controlgetal2(grootste_getal(getallen),controlegetal2),
        "Aantal unieke elementen": aantal_elementen(unieke_getallen_selecteren(getallen)),
        f"Het verschil tussen {aantal_elementen(unieke_getallen_selecteren(getallen))} & {controlegetal1}": verschil_tussen_elementen(aantal_elementen(unieke_getallen_selecteren(getallen)),controlegetal1),
        "Gesorteerde lijst getallen": gesorteerde_lijst(getallen),
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst(unieke_getallen_selecteren(getallen)),
        "Telling van elementen": tel_elementen(getallen),
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaardoor1(unieke_getallen_selecteren(getallen)),
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaardoor2(unieke_getallen_selecteren(getallen)),
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor(getallen),
        f"{controlegetal1} komt voor op positie(s)": posities(getallen),
        "Standaardafwijking": standaardafwijking(gemiddelde(som_alle_getalen(getallen), aantal(getallen)), getallen, aantal(getallen)),
        "Geshufflede lijst": shuffle_lijst(getallen),
        "Willekeurige getal uit de lijst": random_getal(getallen),
        f"Het verschil tussen {getal} & {controlegetal2}": verschil_tussen_getallen(getal),
    }

    return resultaten



getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")