#Levi van Broekhoven Opdracht Pizza Calculator
small = 6
medium = 8
large = 15

PizzaGroote = input("wat voor grote pizza wilt u? (small medium large) ")
PizzaAantal = int(input("hoeveel pizza's wilt u? "))

if PizzaGroote == ("small"):
    prijs = PizzaAantal * small
    print("----------------------------------------------------")
    print(f"| Aantal pizza's :  {PizzaAantal}                  ")
    print(f"| Groote pizza   :  {PizzaGroote}                  ")
    print(f"| Prijs          :  {prijs} euro                   ")
    print("----------------------------------------------------")
if PizzaGroote == ("medium"):
    prijs = PizzaAantal * medium
    print("----------------------------------------------------")
    print(f"| Aantal pizza's :  {PizzaAantal}                  ")
    print(f"| Groote pizza   :  {PizzaGroote}                  ")
    print(f"| Prijs          :  {prijs} euro                   ")
    print("----------------------------------------------------")
if PizzaGroote == ("large"):
    prijs = PizzaAantal * large
    print("----------------------------------------------------")
    print(f"| Aantal pizza's :  {PizzaAantal}                  ")
    print(f"| Groote pizza   :  {PizzaGroote}                  ")
    print(f"| Prijs          :  {prijs} euro                   ")
    print("----------------------------------------------------")
   