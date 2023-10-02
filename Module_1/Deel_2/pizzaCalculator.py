small = 1
medium = 2
large = 3

PizzaGroote = input("wat voor grote pizza wilt u? (small medium large) ")
PizzaAantal = (input("hoeveel pizza's wilt u? "))

if PizzaGroote == ("small"):
    prijs = PizzaAantal * small
    print(f" Uw {PizzaAantal } {PizzaGroote} Pizza's kosten {prijs} euro" )
if PizzaGroote == ("medium"):
    prijs = PizzaAantal * medium
    print(f" Uw {PizzaAantal } {PizzaGroote} Pizza's kosten {prijs} euro" )
if PizzaGroote == ("large"):
    prijs = PizzaAantal * large
    print(f" Uw {PizzaAantal } {PizzaGroote} Pizza's kosten {prijs} euro" )
   