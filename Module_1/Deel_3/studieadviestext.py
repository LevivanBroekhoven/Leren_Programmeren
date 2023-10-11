print("""
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies.
************************************************************ 
""")

OPTIES = (" Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit")

AANTAL_WEKEN_VRAAG = int(input('Hoeveel weken ben je al bezig met de opleiding? '))

print(OPTIES)
COMPETENTIE_STELLING_1 = int(input('Ik voel stress of blokkades bij het maken van programmeeropdrachten: '))

print(OPTIES)
COMPETENTIE_STELLING_2 = int(input('Ik stel programmeeropdrachten en -uitdagingen uit: '))

print(OPTIES)
COMPETENTIE_STELLING_3 = int(input('Ik denk dat ik geen talent heb voor de opleiding: '))

print(OPTIES)
COMPETENTIE_STELLING_4 = int(input('Ik vermijd assessments (CJV) en feedback van kritische docenten: '))

print(OPTIES)
COMPETENTIE_STELLING_5 = int(input('Ik vergelijk mezelf met anderen die beter lijken te zijn: '))

if AANTAL_WEKEN_VRAAG <= 10:
    print(OPTIES)
    COMPETENTIE_STELLING_6 = int(input('Ik voel geen interesse in nieuwe programmeertechnieken: '))
    
    print(OPTIES)
    COMPETENTIE_STELLING_7 = int(input('Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is: '))

uitslag = COMPETENTIE_STELLING_1 + COMPETENTIE_STELLING_2 + COMPETENTIE_STELLING_3 + COMPETENTIE_STELLING_4 + COMPETENTIE_STELLING_5

if AANTAL_WEKEN_VRAAG <= 10:
    uitslag += COMPETENTIE_STELLING_6 + COMPETENTIE_STELLING_7

print("*********************** STUDIEADVIES ***********************")

COMPETENTIE_ADVIES_ZORGELIJK = "Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen."

COMPETENTIE_ADVIES_TWIJFELACHTIG = "Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!"

COMPETENTIE_ADVIES_GERUSTSTELLEND = "Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!"

if uitslag >= 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif uitslag == 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
