Naam = input("Wat is uw naam: ")
Gewicht = input("Weegt u zwaarder dan 90kg en lichter dan 120kg (ja/nee): ")
Hoed = input("Heeft u een hoge hoed (ja/nee): ")
lengte = input("Ben u langer dan 150cm en korter dan 220cm (ja/nee): ")
certificaat = input("Heeft u het certificaat Overleven met gevaarlijk persoon (ja/nee): ")
certificaat2 = int(input("Hoeveel jaar praktijkervaring met dieren-dressuur heeft u? "))
certificaat3 = int(input("Hoeveel jaar ervaring met jongleren heeft u? "))
certificaat4 = int(input("Hoeveel jaar praktijkervaring met acrobatiek heeft u? "))
ResultaatSollicitatie = "Wel"

if Gewicht == 'nee' or Hoed == 'nee' or lengte == 'nee' or certificaat == 'nee':
    ResultaatSollicitatie = 'Niet '
elif certificaat2 <= 4 or certificaat3 <= 5 or certificaat4 <= 3:
    ResultaatSollicitatie = 'Niet '

print(f"Hallo {Naam}, u bent {ResultaatSollicitatie}aangenomen.")