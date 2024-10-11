from EindOpdracht3Data import *
from EindOpdrachtFunctions import *

Smakenlijst = [{"Aardbeismaak": 0},{"Chocoladesmsaak": 0},{"Muntsmaak": 0},{"Vanillesmaak":0}]
Toppingslijst = [{"Slagroom": 0},{"Sprinkels": 0},{"CaramelsausHoorntje":0},{"CaramelsausBakje": 0}]

doorgaan = "ja"
print("Welkom bij Papi Gelato!")

while doorgaan != "nee":
    bolletje = Vraag_bolletjes()
    Smaken(bolletje, Smakenlijst)
    aantalhoorntjes, aantalbakjes, toppingtype = kies_horen_of_bakje(bolletje)
    toppings = Toppings(toppingtype, Toppingslijst)
    doorgaan = meerbestellen()

totaal,totaaltopping = totaalberekenen(Toppingslijst)
bonnetje(totaal, aantalbakjes ,aantalhoorntjes, toppings,Smakenlijst,totaaltopping )