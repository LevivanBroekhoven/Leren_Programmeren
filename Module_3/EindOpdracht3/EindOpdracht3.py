from EindOpdracht3Data import *
from EindOpdrachtFunctions import *
doorgaan = "ja"
print("Welkom bij Papi Gelato! Je mag alle smaken kiezen zolang het maar vanille ijs is.")

while doorgaan != "nee":
    bolletje = Vraag_bolletjes()
    kies_horen_of_bakje(bolletje)
    doorgaan = meerbestellen()







