#Levi van Broekhoven Opdracht Pizza Calculator

prijzen = {"small": 8.99, "medium": 11.99, "large": 14.99}
PizzaAantalsmall = 0
PizzaAantalmedium = 0
PizzaAantallarge = 0 

bestelling = int(input("Hoeveel pizza's wilt u? "))

for x in range(bestelling):
    while True:  
        typepizza = input(f"Wat voor type pizza wilt u hebben? voor pizza {x + 1} van de {bestelling} (small, medium, large): ")
        
        if typepizza == "small":
            PizzaAantalsmall += 1
            break
        elif typepizza == "medium":
            PizzaAantalmedium += 1
            break  
        elif typepizza == "large":
            PizzaAantallarge += 1
            break
        else:
            print("Geen geldige optie, probeer opnieuw.")


prijs_small  = PizzaAantalsmall   * prijzen["small"]
prijs_medium = PizzaAantalmedium  * prijzen["medium"]
prijs_large  = PizzaAantallarge   * prijzen["large"]

totaalprijs = round(prijs_small + prijs_medium + prijs_large ,2)


# Mooier bonnetje
print("\n ------------------------------------------")
print("                 Bonnetje                  ")
print(" ------------------------------------------")
print("                                           ")
if PizzaAantalsmall >= 1:
    print(f"  Aantal small pizza's:  {PizzaAantalsmall}   {prijs_small} euro")
if PizzaAantalmedium >= 1:
    print(f"  Aantal medium pizza's: {PizzaAantalmedium}   {prijs_medium} euro")
if PizzaAantallarge >= 1 :
    print(f"  Aantal large pizza's:  {PizzaAantallarge}   {prijs_large} euro")
print(" ------------------------------------------")
print(f"  Totaal aantal pizza's: {bestelling}     ")
print(f"  Totaalprijs: {totaalprijs} euro         ")
print("                                           ")
print(" ------------------------------------------")