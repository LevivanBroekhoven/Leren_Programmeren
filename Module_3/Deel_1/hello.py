def hello(getal):
    seperator = "\n"
    hallo = []
    getal2 = 1
    for x in range(getal):
        uitkomst = (f"Hallo from functie town {getal2}")
        hallo.append(uitkomst)
        getal2 += 1
    y = seperator.join(hallo)
    return(y)
    



test = hello(3)
print(test)