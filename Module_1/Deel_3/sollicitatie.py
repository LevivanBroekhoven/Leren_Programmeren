Naam = input("Wat is uw naam: ")
Gewicht = input("Weegt u zwaarder dan 90kg en lichter dan 120kg: ")
Hoed = input("Heeft u een hoge hoed: ")
lengte = input("Ben u langer dan 150cm en korter dan 220cm: ")
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

if Gewicht == "nee" or Hoed == "nee" or lengte == "nee" or certificaat == "nee" or rijbewijs == "nee" or diploma == "nee":
    ResultaatSollicitatie = "Niet"

elif certificaat2 < 3 or certificaat3 <= 4 and certificaat4 <= 2:
    ResultaatSollicitatie = "Niet"

if geslacht == "man":
    snor = input("Is uw snor breder dan 10cm? ")
    if snor == "nee":
        ResultaatSollicitatie = "Niet"
elif geslacht == "vrouw":
    haar = input("Heeft u rood krulhaar langer dan 20cm? ")
    if haar == "nee":
        ResultaatSollicitatie = "Niet"
elif geslacht == "anders":
    lach = input("Heeft u een lach breder dan 10cm? ")
    if lach == "nee":
        ResultaatSollicitatie = "Niet"
if ondernemer <= 3 and werknemers <= 5:
    ResultaatSollicitatie = "Niet"

if ResultaatSollicitatie == "Wel":
    print(f"Hallo {Naam}, u bent {ResultaatSollicitatie} aangenomen.")

elif ResultaatSollicitatie == "Niet":
     print(f"Hallo {Naam}, u bent {ResultaatSollicitatie} aangenomen want.")
     if Gewicht == "nee":
         print("U ben te licht/ Te zwaar voor ons")
     if Hoed == "nee":
         print("u had geen hoge hoed")
     if lengte == "nee":
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
     if geslacht == "man" and snor == "nee":
         print("Uw snor is kleiner dan 10cm")
     if geslacht == "vrouw" and haar == "nee":
         print("Uw haar is korter dan 20cm of niet rood")
     if geslacht == "anders" and lach == "nee":
         print ("Uw lach is minder breed dan 10cm")