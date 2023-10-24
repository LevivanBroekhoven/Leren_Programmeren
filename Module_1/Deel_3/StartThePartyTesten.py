drank = True
chips = True
aantal_gasten = 22
mijn_naam = ("Levi")
SLB_naam = ("Eugene")
gastheer = input("Naam gastheer ")
gasten = aantal_gasten > 4 and aantal_gasten < 20

party_gasten = gasten and chips and drank and gastheer != SLB_naam
party_gastheer = gastheer and drank and gastheer != SLB_naam
party_me = gastheer == mijn_naam  

if party_gasten or party_gastheer or party_me == True:
    print("Start the party")
else:
    print('No Party')

    