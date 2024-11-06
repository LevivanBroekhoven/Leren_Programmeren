from EindOpdracht3Data import *
from EindOpdrachtFunctions import *

aantalbolletjes = 0
aantalbakjes = 0
aantalhoorntjes = 0
Smakenlijst = [{'Aardbei': 0}, {'Chocolade': 0},{'Vanille': 0}]
SmakenlijstLiter = [{'Aardbei': 0}, {'Chocolade': 0},{'Vanille': 0}]
Toppingslijst = [{'Slagroom': 0}, {'Sprinkels': 0}, {'CaramelsausHoorntje': 0}, {'CaramelsausBakje': 0}]

doorgaan = "ja"
print("Welkom bij Papi Gelato!")
PofZ = PofZklant()

if PofZ == "P":
    while doorgaan != "nee":
        bolletje, aantalbolletjes = Vraag_bolletjes(aantalbolletjes)
        aantalhoorntjes, aantalbakjes, toppingtype = kies_horen_of_bakje(bolletje, aantalhoorntjes, aantalbakjes)
        Smakenlijst = Smaken(bolletje, Smakenlijst)
        toppings, Toppingslijst = Toppings(toppingtype, Toppingslijst)
        doorgaan = input("Wilt u nog meer bestellen? (Ja/Nee) ")
        

    totaal, totaaltopping = totaalberekenen(aantalbolletjes, aantalbakjes, aantalhoorntjes, Toppingslijst)
    bonnetje(totaal, aantalbakjes, aantalhoorntjes, toppings, Smakenlijst, totaaltopping)
    print("Bedankt en tot ziens!")

elif PofZ == "Z":
    print("U bent een zakelijke klant")
    literijs = Literijs()
    SmakenlijstLiter = smakenliterijs(literijs, SmakenlijstLiter)
    bonnetjeZakkelijk(SmakenlijstLiter, literijs)


