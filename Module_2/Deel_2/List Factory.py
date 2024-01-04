lijstjes = []

aantal_lijstjes = int(input("Hoeveel lijstjes? "))

for x in range(1, aantal_lijstjes + 1):
    lengte_lijst = int(input(f"Hoeveel in lijst {x}? "))
    lijst = list(range(x, (x * lengte_lijst) +1, x))
    lijstjes.append(lijst)

print(lijstjes)

