crosaint = int(input("hoeveel crosaintjes wil je? "))
stokbrood = int(input("hoeveel stokbroodjes wil je? "))
kortingbon = int(input("hoeveel kortingsbonnen heb je? "))

CROSAINTP = 0.39
STOKBROODP = 2.78
KORTINGBON = 0.50

crosaintprijs = CROSAINTP * crosaint
stokbroodprijs = STOKBROODP *stokbrood
kortingbonprijs = KORTINGBON * kortingbon

antwoord = crosaintprijs + stokbroodprijs - kortingbonprijs
print ("De feestlunch kost je bij de bakker",round(antwoord,2),"euro voor",crosaint,"crossaints en",stokbrood, "stokbroden als de",kortingbon,"kortingsbonnen nog geldig zijn!.")