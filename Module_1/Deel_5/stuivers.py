def afronden(Bedrag):
    afronding = round(Bedrag * 100 / 5) * 5 /100
    return afronding 



Bedrag = 62.63
afgerond_Bedrag = afronden(Bedrag)

print (afgerond_Bedrag) 

