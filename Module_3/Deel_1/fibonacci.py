def fibonacci(herhaalx):
    x = 0
    getal1 = 0
    getal2 = 1
    reeks = [getal1 , getal2]
    while x <= herhaalx:
        result = getal1 + getal2
        getal1 = getal2
        getal2 = result
        x += 1
        reeks.append(result)
    return(reeks)
    

antwoord = fibonacci(7)
print(antwoord)





















fibonacci(7)