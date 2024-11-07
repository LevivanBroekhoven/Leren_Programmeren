from EindOpdracht3Data import *
def PofZklant():
    while True:
        PofZklant = input("Bent u een zakelijke of een particuliere klant? P of z? ")
        if PofZklant == "Z" or "P":
            return PofZklant
        else:
            print(TXT)

            

def Literijs():
    while True:
        try:
            literijs = int(input("Hoeveel liter ijs wilt u? "))
        
            return literijs
        except ValueError:
            print(TXT)



def smakenliterijs(literijs, SmakenlijstLiter):
    for x in range(literijs):
        while True:
            smaak = input(f"Welke smaak wilt u voor Liter {x+1}? A) Aardbei, C) Chocolade of V) Vanille? ")
            if smaak == "A":
                SmakenlijstLiter[0]['Aardbei'] += 1
                break
            elif smaak == "C":
                SmakenlijstLiter[1]["Chocolade"] += 1
                break
            elif smaak == "V":
                SmakenlijstLiter[2]['Vanille'] += 1
                break
            else:
                print(TXT)
    return SmakenlijstLiter

def Vraag_bolletjes(aantalbolletjes):
    while True:
        try:
            bolletje = int(input("Hoeveel bolletjes wilt u? "))
            if bolletje < 1:
                print("U moet minstens 1 bolletje kiezen.")
            elif bolletje > MAX_BOLLETJES_BAKJE:
                print(f"Sorry, in onze bakjes kunnen maar {MAX_BOLLETJES_BAKJE} bolletjes.")
            else:
                aantalbolletjes += bolletje
                return bolletje, aantalbolletjes
        except ValueError:
            print(TXT)


def Smaken(aantalbolletjes, Smakenlijst):
    for x in range(aantalbolletjes):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje {x+1}? A) Aardbei, C) Chocolade of V) Vanille? ")
            if smaak == "A":
                Smakenlijst[0]['Aardbei'] += 1
                break
            elif smaak == "C":
                Smakenlijst[1]["Chocolade"] += 1
                break
            elif smaak == "V":
                Smakenlijst[2]['Vanille'] += 1
                break
            else:
                print(TXT)
    return Smakenlijst

def Toppings(BakjeFhoorntje, Toppingslijst):
    toppings = 0
    while True:
        topping = input("Wat voor topping wilt u? A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if topping == "A":
            break
        elif topping == "B":
            toppings += 1
            Toppingslijst[0]["Slagroom"] += 1
            break
        elif topping == "C":
            toppings += 1
            Toppingslijst[1]["Sprinkels"] += 1
            break
        elif topping == "D":
            toppings += 1
            if BakjeFhoorntje == "bakje":
                Toppingslijst[3]["CaramelsausBakje"] += 1
            elif BakjeFhoorntje == "hoorntje":
                Toppingslijst[2]["CaramelsausHoorntje"] += 1
            break
        else:
            print(TXT)
    return toppings, Toppingslijst

def kies_horen_of_bakje(bolletje, aantalhoorntjes, aantalbakjes):
    bakje = "bakje"
    hoorntje = "hoorntje"
    toppingtype = ""

    while True:
        if MIN_BOLLETJES <= bolletje <= MAX_BOLLETJES_HOORNTJE:
            hoorntjeofBakje = input(f"Wilt u deze {bolletje} bolletjes in een hoorntje of bakje? ")
            if hoorntjeofBakje == "hoorntje":
                print(f"Hier is uw {bolletje} bolletjes in een hoorntje.")
                aantalhoorntjes += 1
                toppingtype = hoorntje
                break
            elif hoorntjeofBakje == "bakje":
                print(f"Hier is uw {bolletje} bolletjes in een bakje.")
                aantalbakjes += 1
                toppingtype = bakje
                break
        if MAX_BOLLETJES_HOORNTJE <= bolletje <= MAX_BOLLETJES_BAKJE:
            print(f"Hier is uw {bolletje} bolletjes in een bakje.")
            aantalbakjes += 1
            toppingtype = bakje
            break 
        else:
            print(TXT)

    return aantalhoorntjes, aantalbakjes, toppingtype

def totaalberekenen(aantalbolletjes, aantalbakjes, aantalhoorntjes, Toppingslijst,):
    totaalbol = aantalbolletjes * PRIJSBOLLETJE
    totaalbak = aantalbakjes * PRIJSBAKJE
    totaalhorn = aantalhoorntjes * PRIJSHOORNTJE
    totaaltoppings = 0


    totaalslagroom = totaalsprinkels = totaalcaramelbakje = totaalcaramelhoorntje = 0

    for topping_dict in Toppingslijst:
        for topping, aantal in topping_dict.items():
            if topping == "Slagroom":
                totaalslagroom = aantal * PRIJSSLAGROOM
            elif topping == "Sprinkels":
                totaalsprinkels = aantal * PRIJSSPRINKELS
            elif topping == "CaramelsausBakje":
                totaalcaramelbakje = aantal * PRIJSCARAMELBAKJE
            elif topping == "CaramelsausHoorntje":
                totaalcaramelhoorntje = aantal * PRIJSCARAMELHOORNTJE

    totaaltoppings = round(totaalslagroom + totaalsprinkels + totaalcaramelbakje + totaalcaramelhoorntje, 2)
    totaal = round(totaalbol + totaalbak + totaalhorn + totaaltoppings, 2)

    return totaal, totaaltoppings

def bonnetje(totaal, aantalbakjes, aantalhoorntjes, toppings, Smakenlijst, totaaltopping, SmakenlijstLiter , PofZ):
    print("------------------Papi Gelato]-----------------")
    if PofZ == "P":
     

        for smaak_dict in Smakenlijst:
            for smaak, aantal in smaak_dict.items():
                if aantal > 0: 
                    totaal_prijs = round(aantal * PRIJSBOLLETJE, 2) 
                    print(f"{smaak:20}    {aantal} x €{PRIJSBOLLETJE} = €{totaal_prijs:.2f}") 

        if aantalbakjes > 0:
            print(f"Bakjes    {aantalbakjes:15} x €{PRIJSBAKJE:.2f} = €{round(aantalbakjes * PRIJSBAKJE, 2):.2f}")

        if aantalhoorntjes > 0:
            print(f"Hoorntjes {aantalhoorntjes:15} x €{PRIJSHOORNTJE:.2f} = €{round(aantalhoorntjes * PRIJSHOORNTJE, 2):.2f}")


        if toppings > 0:
            print(f"Toppings     {toppings:12} x €{totaaltopping:.2f} = €{round(toppings * totaaltopping, 2):.2f}")

    if PofZ == "Z":
        for smaak_dict in SmakenlijstLiter:
            for smaak, aantal in smaak_dict.items():
                if aantal > 0: 
                    totaal_prijs = round(aantal * LITERIJS, 2) 
                    print(f" L. {smaak:18}:    {aantal:3} x €{LITERIJS} = €{totaal_prijs:8.2f}") 
        
        
        btw = totaal / 100 * BTW

    print("                   -------------------------- +")
    print(f"Totaal  =                             €{float(totaal):8.2f}")
    if PofZ == "Z":
        print(f"BTW     =                             €{float(btw):8.2f}")

