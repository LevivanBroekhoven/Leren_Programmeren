crosaint = int(input("hoeveel crosaintjes wil je? "))
stokbrood = int(input("hoeveel stokbroodjes wil je? "))
kortingbon = int(input("hoeveel kortingsbonnen heb je? "))

CROSAINTP = 39
STOKBROODP = 278
KORTINGBON = 50

crosaintprijs = CROSAINTP * crosaint
stokbroodprijs = STOKBROODP *stokbrood
kortingbonprijs = KORTINGBON * kortingbon

antwoordC = crosaintprijs + stokbroodprijs - kortingbonprijs
antwoordE = round(antwoordC /100 ,2)
print ("De feestlunch kost je bij de bakker",antwoordE,"euro voor",crosaint,"crossaints en",stokbrood, "stokbroden als de",kortingbon,"kortingsbonnen nog geldig zijn!.")