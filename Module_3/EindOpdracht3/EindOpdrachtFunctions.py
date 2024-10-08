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

def Smaken():
    global aantalbolletjes, Aardbeicount, Chocoladecount, Muntcount, Vanillecount
    Aardbeicount = 0
    Chocoladecount =0
    Muntcount=0
    Vanillecount=0
    
    for x in range(aantalbolletjes):
        while True:

            smaak = input(f"Welke smaak wilt u voor bolletje {x+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if smaak == "A":
                Aardbeicount += 1
                break
            if smaak == "C":
                Chocoladecount +=1
                break
            if smaak == "M":
                Muntcount +=1
                break
            if smaak == "V":
                Vanillecount += 1
                break
            else:
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
    global Chocoladecount, Vanillecount, Muntcount, Aardbeicount
    totaal = totaalberekenen()
    

    print("--------[Papi Gelato]--------")
    if Chocoladecount > 0:
        print(f"B.Chocolade {Chocoladecount} x €{PRIJSBOLLETJE}  = € {round(Chocoladecount * PRIJSBOLLETJE,2)}  ")

    if Vanillecount > 0:
        print(f"B.Vannile {Vanillecount} x €{PRIJSBOLLETJE}  = € {round(Vanillecount * PRIJSBOLLETJE,2)}  ")

    if Muntcount > 0:
        print(f"B.Munt {Muntcount} x €{PRIJSBOLLETJE}  = € {round(Muntcount * PRIJSBOLLETJE,2)}  ")

    if Aardbeicount > 0:
        print(f"B.Aardbei {Aardbeicount} x €{PRIJSBOLLETJE}  = € {round(Aardbeicount * PRIJSBOLLETJE,2)}  ")

    if aantalbakjes > 0:
        print(f"Bakjes    {aantalbakjes} x €{PRIJSBAKJE} = € {round(aantalbakjes* PRIJSBAKJE,2)}     ")

    if aantalhoorntjes > 0:
        print(f"Hoorntjes {aantalhoorntjes} x €{PRIJSHOORNTJE} = € {round(aantalhoorntjes * PRIJSHOORNTJE,2)}  ")
    print("                   ---------- +")
    print(f"Totaal             = € {float(totaal)}  ")


         
    