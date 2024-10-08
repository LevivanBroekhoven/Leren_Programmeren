from EindOpdracht3Data import *
from EindOpdrachtFunctions import *
doorgaan = "ja"
print("Welkom bij Papi Gelato!")

while doorgaan != "nee":
    bolletje = Vraag_bolletjes()
    Smaken()
    kies_horen_of_bakje(bolletje)
    doorgaan = meerbestellen()

bonnetje(bolletje)




