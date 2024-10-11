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

def Smaken(aantalbolletjes, Smakenlijst):
    
    for x in range(aantalbolletjes):
        while True:

            smaak = input(f"Welke smaak wilt u voor bolletje {x+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            
            if smaak == "A":
                Smakenlijst[0]['Aardbeismaak'] += 1
        
                break
            if smaak == "C":
                Smakenlijst[1]["Chocoladesmsaak"] += 1
                break
            if smaak == "M":
                Smakenlijst[2]['Muntsmaak'] += 1
                break
            if smaak == "V":
                Smakenlijst[3]['Vanillesmaak'] += 1
                break
            else:
                print("Sorry, dat snap ik niet.")

    return(Smakenlijst)

def Toppings(BakjeFhoorntje, Toppingslijst):
    toppings = 0
  

    while True:
        topping = input("Wat voor topping wilt u? A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if topping == "A":
            ()
            break
        if topping == "B":
                toppings +=1
                Toppingslijst[0]["Slagroom"]
                break
        if topping == "C":
                Toppingslijst[1]["Sprinkels"]
                break
        if topping == "D":
            toppings+= 1
            if BakjeFhoorntje == "bakje":
                Toppingslijst[3]["CaramelsausBakje"]

            if BakjeFhoorntje == "hoorntje":
                Toppingslijst[2]["CaramelsausHoorntje"]
            break
        else:
            print("Sorry, dat snap ik niet.")

    return(toppings)

def kies_horen_of_bakje(bolletje):
    global aantalbakjes, aantalhoorntjes
    bakje = ("bakje")
    hoorntje=("hoorntje")
    toppingtype =()


    while True:
        if MIN_BOLLETJES <= bolletje <= MAX_BOLLETJES_HOORNTJE:
            hoorntjeofBakje = input(f"Wilt u deze {bolletje} bolletjes in een hoorntje of bakje? ")
            if hoorntjeofBakje == "hoorntje":
                print(f"Hier is uw {bolletje} bolletjes in een hoorntje.")
                aantalhoorntjes += 1
                toppingtype = (hoorntje)
                break
            elif hoorntjeofBakje == "bakje":
                print(f"Hier is uw {bolletje} bolletjes in een bakje.")
                aantalbakjes += 1
                toppingtype = (bakje)
                break
        if MAX_BOLLETJES_HOORNTJE <= bolletje <= MAX_BOLLETJES_BAKJE:
            print(f"Hier is uw {bolletje} bolletjes in een bakje.")
            aantalbakjes += 1
            toppingtype =(bakje)
            break

        elif bolletje > MAX_BOLLETJES_BAKJE:
            print("Sorry, zulke grote bakken hebben we niet.")
            bolletje = Vraag_bolletjes()
            
            
        else:
            print("Sorry, dat snap ik niet.")

    return(aantalhoorntjes,aantalbakjes,toppingtype)

        
          


def meerbestellen():
    jofninput = input("Wilt u nog meer bestellen? (Ja/Nee) ")
    if jofninput == "nee":
        print("Bedankt en tot ziens!")
        return("nee")

    if jofninput == "ja":
        return()
    else:
        print("Sorry, dat snap ik niet.")


def totaalberekenen(Toppingslijst):
    totaalbol = aantalbolletjes * PRIJSBOLLETJE
    totaalbak = aantalbakjes * PRIJSBAKJE
    totaalhorn = aantalhoorntjes * PRIJSHOORNTJE

    for topping_dict in Toppingslijst:
        for topping, aantal in topping_dict.items():
            if topping == "Slagroom":
                totaalslagroom = aantal * PRIJSSLAGROOM
                
            if topping == "Sprinkels":
                totaalsprinkels = aantal * PRIJSSPRINKELS
            if topping == "CaramelsausBakje":
                totaalcaramelbakje = aantal * PRIJSCARAMELBAKJE
            if topping == "CaramelsausHoorntje":
                totaalcaramelhoorntje = aantal * PRIJSCARAMELHOORNTJE
            



    totaaltopping = round(totaalslagroom + totaalsprinkels + totaalcaramelbakje + totaalcaramelhoorntje, 2)
    print(totaalslagroom)

    totaal = round(totaalbol + totaalbak + totaalhorn + totaaltopping, 2)
 



    return(totaal,totaaltopping)




def bonnetje(totaal, aantalbakjes ,aantalhoorntjes, toppings,Smakenlijst,totaaltopping ):
    
    

    print("--------[Papi Gelato]--------")

    for smaak_dict in Smakenlijst:
        for smaak, aantal in smaak_dict.items():
            if aantal > 0: 
                totaal_prijs = round(aantal * PRIJSBOLLETJE, 2) 
                print(f"{smaak}:    {aantal} bolletjes x €{PRIJSBOLLETJE} = €{totaal_prijs}")

    if aantalbakjes > 0:
        print(f"Bakjes    {aantalbakjes} x €{PRIJSBAKJE} = € {round(aantalbakjes* PRIJSBAKJE,2)}     ")

    if aantalhoorntjes > 0:
        print(f"Hoorntjes {aantalhoorntjes} x €{PRIJSHOORNTJE} = € {round(aantalhoorntjes * PRIJSHOORNTJE,2)}  ")

    if toppings  > 0:
        print(f"Topping    = € {totaaltopping}     ")
    print("                   ---------- +")
    print(f"Totaal             = € {float(totaal)}  ")


         
    