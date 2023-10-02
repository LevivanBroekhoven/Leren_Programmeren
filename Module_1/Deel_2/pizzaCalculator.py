#Levi van Broekhoven Opdracht Pizza Calculator
prijzen = {"small": 8.99,"medium": 11.99,"large": 14.99}

PizzaAantalsmall = int(input(f"hoeveel small pizza's wilt u? "))
PizzaAantalmedium = int(input(f"hoeveel medium pizza's wilt u? "))
PizzaAantallarge = int(input(f"hoeveel large pizza's wilt u? "))

prijs_small  = PizzaAantalsmall   * prijzen["small"]
prijs_medium = PizzaAantalmedium  * prijzen["medium"]
prijs_large  = PizzaAantallarge   * prijzen["large"]

totaalprijs = prijs_small + prijs_medium + prijs_large
totaalaantal = PizzaAantalsmall + PizzaAantalmedium + PizzaAantallarge

print(" ------------------------------------------")
print("                  Bonnetje                 ")
print(" ------------------------------------------")
print("                                           ")
print(f"  Aantal pizza's {totaalaantal}           ")
print(f"  Prijs {totaalprijs} euro                ")
print("                                           ")
print(" -------------------------------------------")

            