Naam = input("Wat is uw naam: ")
Gewicht = int(input("Wat is uw gewicht: "))
Hoed = input("Heeft u een hoge hoed: ")
lengte = int(input("Wat is uw lengte: "))
rijbewijs = input("Heeft u een vrachtwagen rijbewijs? ")
certificaat = input("Heeft u het certificaat Overleven met gevaarlijk persoon: ")
certificaat2 = int(input("Hoeveel jaar praktijkervaring met dieren-dressuur heeft u? "))
certificaat3 = int(input("Hoeveel jaar ervaring met jongleren heeft u? "))
certificaat4 = int(input("Hoeveel jaar praktijkervaring met acrobatiek heeft u? "))
diploma = input("heeft u een MBO-4 diploma ")
ondernemer = int(input("Hoelang bent u al ondernemer "))
werknemers = int(input("Hoeveel werknemers had u in dienst? "))
geslacht = input("bent u man of vrouw? of anders ")
ResultaatSollicitatie = "Wel"

MIN_GEWICHT = 90
MAX_GEWICHT = 120

MIN_LENGTE = 150
MAX_LENGTE = 220

SNOR_MIN = 10

HAAR_MIN = 20

LACH_MIN = 10



if Gewicht < MIN_GEWICHT or Gewicht > MAX_GEWICHT or Hoed == "nee" or lengte < MIN_LENGTE or lengte > MAX_LENGTE or certificaat == "nee" or rijbewijs == "nee" or diploma == "nee":
    ResultaatSollicitatie = "Niet"

elif certificaat2 < 3 or certificaat3 <= 4 and certificaat4 <= 2:
    ResultaatSollicitatie = "Niet"

if geslacht == "man":
    snor = int(input("Hoe breed is uw snor "))
    if snor < SNOR_MIN:
        ResultaatSollicitatie = "Niet"
elif geslacht == "vrouw":
    haar = int(input("Heeft u rood krulhaar en hoe lang is dat? "))
    if haar < HAAR_MIN or haar == "nee":
        ResultaatSollicitatie = "Niet"
elif geslacht == "anders":
    lach = int(input("Hoe breed is uw lach? "))
    if lach < LACH_MIN:
        ResultaatSollicitatie = "Niet"
if ondernemer <= 3 and werknemers <= 5:
    ResultaatSollicitatie = "Niet"

if ResultaatSollicitatie == "Wel":
    print(f"Hallo {Naam}, u bent {ResultaatSollicitatie} aangenomen.")

elif ResultaatSollicitatie == "Niet":
     print(f"Hallo {Naam}, u bent {ResultaatSollicitatie} aangenomen want.")
     if Gewicht < MIN_GEWICHT or Gewicht > MAX_GEWICHT:
         print("U ben te licht/ Te zwaar voor ons")
     if Hoed == "nee":
         print("u had geen hoge hoed")
     if lengte < MIN_LENGTE or lengte > MAX_LENGTE:
         print("U ben te lang/ te klein voor ons")
     if rijbewijs == "nee":
         print("U heeft geen rijbewijs")
     if diploma == "nee":
         print("u heeft geen MBO-4 Diploma")
     if certificaat == "nee":
         print("U heeft geen certificaat Overleven met gevaarlijk persoon")
     if certificaat2 < 4:
         print("U heeft niet genoeg jaar praktijkervaring met dieren-dressuur")
     if certificaat3 < 5:
         print("U heeft niet genoeg jaar ervaring met jongleren")
     if certificaat4 < 3:
         print("U heeft niet genoeg jaar praktijkervaring met acrobatiek")
     if geslacht == "man" and snor < SNOR_MIN:
         print("Uw snor is kleiner dan 10cm")
     if geslacht == "vrouw" and haar < HAAR_MIN or haar == "nee":
         print("Uw haar is korter dan 20cm of niet rood")
     if geslacht == "anders" and lach < LACH_MIN:
         print ("Uw lach is minder breed dan 10cm")