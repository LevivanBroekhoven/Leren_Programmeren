Dagentuple = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")
WerkDagen = Dagentuple[:5]
WeekendDagen = Dagentuple[5:]


print("Alle dagen van de week zijn:", end=" ")
for x in Dagentuple:
    print(x, end=", ")
print("\n")

print("De werkdagen zijn:", end=" ")
for x in WerkDagen:
    print(x, end=", ")
print("\n")

print("De weekenddagen zijn:", end=" ")
for x in WeekendDagen:
    print(x, end=", ")
print("\n")

print("Alle dagen van de week in omgekeerde volgorde zijn:", end=" ")
for x in reversed(Dagentuple):
    print(x, end=", ")
print("\n")

print("De werkdagen in omgekeerde volgorde zijn:", end=" ")
for x in reversed(WerkDagen):
    print(x, end=", ")
print("\n")

print("De weekenddagen in omgekeerde volgorde zijn:", end=" ")
for x in reversed(WeekendDagen):
    print(x, end=", ")
print("\n")