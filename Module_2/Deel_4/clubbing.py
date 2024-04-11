PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

bandje = False

    
#bouw hieronder de floowchart na
leeftijd = int(input("Hoe oud ben je? "))
naam = input("wat is je naam? ")

if leeftijd < 18:
    print("Sorry je mag niet naar binnen")
    print(f"Probeer het opnieuw in {18 - leeftijd} jaar")
    quit()

if naam not in VIP_LIST:
    if leeftijd >= 21:
        print("Je krijgt van mij een stempel")
if naam in VIP_LIST:
    bandje = True
    print("je krijgt een bandje")
    if leeftijd >= 21:
        bandjeblauw = True
    elif leeftijd < 21:
        bandjerood = True
        

Drinkvraag = input("wat wil je drinken ")

if Drinkvraag == 'cola':
    if bandje == True:
        print("alstublieft complimenten van het huis")
    if bandje == False:
        print("Betalen")


if Drinkvraag not in DRANKJES:
    print("Sorry geen idee wat je bedoel hier een glaasje water")
