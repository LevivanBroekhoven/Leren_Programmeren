#Opdracht 1
for cijfer in range(1, 14):  
    print("\n")
    print(f"tafel van {cijfer}")
    for x in range(1, 11):  
        antwoord = x * cijfer
        print(f"{x} x {cijfer} = {antwoord}")


#Opdracht 2
lijst = [5, 12, 19, 27, 3]
print(lijst)

#Opdracht 3
lijst.append(25)
print(lijst)


#Opdracht 4
print(f"{len(lijst)} elementen zitten in de lijst {lijst}")

#Opdracht 5
print(lijst)
lijst.remove(12)
print(f"{len(lijst)} elementen zitten in de lijst {lijst}")


#Opdracht 6
print(lijst.pop(0))
print(f"{len(lijst)} elementen zitten in de lijst {lijst}")


#Opdracht 7
lijst.insert(0, 36)
print(f"{len(lijst)} elementen zitten in de lijst {lijst}")


#Opdracht 8
totaal = 0
for nummer in lijst:
    if nummer >= 10:
        totaal += nummer


print(f"{len(lijst)} elementen zitten in de lijst {lijst} en het totaal is {(sum(lijst))}  {(totaal)}")

#Opdracht 9
lijst.clear()
print(f"{len(lijst)} elementen zitten in de lijst {lijst} en het totaal is {(sum(lijst))}")


#Opdracht 10
lijst.extend(range(1,4))
print(f"{len(lijst)} elementen zitten in de lijst {lijst} en het totaal is {(sum(lijst))}")


#Opdracht 11
lijst.extend(range(4,51))
print(f"{len(lijst)} elementen zitten in de lijst {lijst} en het totaal is {(sum(lijst))}")

#Opdracht 12
print(f"{len(lijst)} elementen zitten in de lijst {lijst} en het totaal is {(sum(lijst))} en de positie van het element met de value 25 is {lijst.index(25)}")

#Opdracht 13
lijst[0], lijst[-1] = lijst[-1], lijst[0]
print(f"{len(lijst)} elementen zitten in de lijst {lijst} en het totaal is {(sum(lijst))} en de positie van het element met de value 25 is {lijst.index(25)}")

#Opdracht 14
LijstOpd14 = [1,"aap",2,"apen",3,"watermeloen",15, 27, 15, "Lekker bezig","6"]
