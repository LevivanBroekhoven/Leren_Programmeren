reeks = ''
def reeksrekenen(reeks):
    nieuwereeks = ''
    lengtereeks = len(reeks)
    teller = 1

    for x in range(lengtereeks):
        if x + 1 < lengtereeks and reeks[x] == reeks[x + 1]:
            teller += 1
        else:
            nieuwereeks += str(teller) + reeks[x]

            teller= 1


    return nieuwereeks
    
    
while True:
    reeks = reeksrekenen(reeks)
    print(reeks)
    if '33' in reeks:
        break