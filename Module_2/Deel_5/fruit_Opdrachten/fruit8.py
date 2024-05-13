from fruitmand import *
totaal = 0
for x in fruitmand:
    totaal += (x['weight'])

print(totaal)
totaal = 0

fruitmand.append({'name': 'Meloen',
                  'weight' : 2200})

for x in fruitmand:
    totaal += (x['weight'])


print(totaal)
