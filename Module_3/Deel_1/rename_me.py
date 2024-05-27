def De_rest(Getal:int) -> bool:
    return Getal % 2 == 0
# geeft de rest van de meegegeven int


def Draai_de_zin_om(Dezin:str) -> str:
    splitzin = Dezin.split()
    gedraaidesplitzin = splitzin[::-1]
    OmgedraaideZin  = ' '.join(gedraaidesplitzin)
    return OmgedraaideZin
# draait de zin om
 


def letterteller(woord:str) -> int:
    hetwoord = set(woord)
    aantal_Letters = len(hetwoord)
    return aantal_Letters
# Telt het aantal unieke letters in een woord



def Gemiddelde_Woord_lengte(Zin:str) -> float:
    splitzin = Zin.split()
    
    Gemiddelde = 0
    for woord in splitzin:
        Gemiddelde += len(woord)

    Gemiddelde_lengte = Gemiddelde / len(splitzin)
    return Gemiddelde_lengte
# berekent gemiddelde woordlengte



def tafels(Nummer1:int, Nummer2:int=10) -> None:
    for tafel in range(1, Nummer2+1):
        uitkomst = tafel * Nummer1
        print(f'{tafel} x {Nummer1} = {uitkomst}')
# doet het eerste nummer in een tafel tot de 2de nummer

tafels(1,10)