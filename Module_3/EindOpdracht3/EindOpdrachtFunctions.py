from EindOpdracht3Data import *
aantalbolletjes = 0
aantalbakjes = 0
aantalhoorntjes = 0
    
def Vraag_bolletjes():
    global aantalbolletjes
    while True:
        try:
            bolletje = int(input("Hoeveel bolletjes wilt u? "))
            aantalbolletjes += bolletje
            return(bolletje)
        
        except ValueError:
            print("Sorry, dat snap ik niet.")


def kies_horen_of_bakje(bolletje):
    global aantalbakjes, aantalhoorntjes

    while True:
        if MIN_BOLLETJES <= bolletje <= MAX_BOLLETJES_HOORNTJE:
            hoorntjeofBakje = input(f"Wilt u deze {bolletje} bolletjes in een hoorntje of bakje? ")
            if hoorntjeofBakje == "hoorntje":
                print(f"Hier is uw {bolletje} bolletjes in een hoorntje.")
                aantalhoorntjes += 1
                break
            elif hoorntjeofBakje == "bakje":
                print(f"Hier is uw {bolletje} bolletjes in een bakje.")
                aantalbakjes += 1
                break
        if MAX_BOLLETJES_HOORNTJE <= bolletje <= MAX_BOLLETJES_BAKJE:
            print(f"Hier is uw {bolletje} bolletjes in een bakje.")
            aantalbakjes += 1
            break

        elif bolletje > MAX_BOLLETJES_BAKJE:
            print("Sorry, zulke grote bakken hebben we niet.")
            bolletje = Vraag_bolletjes()
            
            
        else:
            print("Sorry, dat snap ik niet.")

        
          


def meerbestellen():
    jofninput = input("Wilt u nog meer bestellen? (Ja/Nee) ")
    if jofninput == "nee":
        print("Bedankt en tot ziens!")
        return("nee")

    if jofninput == "ja":
        return()
    else:
        print("Sorry, dat snap ik niet.")


def totaalberekenen():
    global aantalbolletjes, aantalbakjes, aantalhoorntjes
    totaalbol = aantalbolletjes * PRIJSBOLLETJE
    totaalbak = aantalbakjes * PRIJSBAKJE
    totaalhorn = aantalhoorntjes * PRIJSHOORNTJE

    totaal = round(totaalbol + totaalbak + totaalhorn, 2)



    return(totaal)




def bonnetje(totaal):
    totaal = totaalberekenen()
    

    print("--------[Papi Gelato]--------")
    if aantalbolletjes > 0:
        print(f"Bolletjes {aantalbolletjes} x €{PRIJSBOLLETJE}  = € {round(aantalbolletjes * PRIJSBOLLETJE,2)}  ")
    if aantalbakjes > 0:
        print(f"Bakjes    {aantalbakjes} x €{PRIJSBAKJE} = € {round(aantalbakjes* PRIJSBAKJE,2)}     ")
    if aantalhoorntjes > 0:
        print(f"Hoorntjes {aantalhoorntjes} x €{PRIJSHOORNTJE} = € {round(aantalhoorntjes * PRIJSHOORNTJE,2)}  ")
    print("                   ---------- +")
    print(f"Totaal             = € {float(totaal)}  ")


         
    