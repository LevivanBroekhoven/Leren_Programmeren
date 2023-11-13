def afronden(Bedrag):
    afronding = round(Bedrag * 100 / 5) * 5 /100
    return afronding 







Bedrag = 62.63
NieuwBedrag = afronden(Bedrag)

print (NieuwBedrag)

print("Dit is een test", round(76.63 * 100 / 5) * 5 /100)