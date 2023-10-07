drank = True
chips = False
mijn_naam = ("Levi")
SLB_naam = ("Eugene")
gastheer = input("Naam gastheer ")
gasten = int(input("Hoeveel gasten? "))



if gastheer == mijn_naam:
    print('No Party')
elif gastheer == SLB_naam:
    print('No Party')
elif gastheer and drank == True:
    print("Start the Party")
elif gasten < 4 or gasten > 20:
    print('No Party')
elif gasten and drank and chips == True:
    print('Start the Party')
elif gastheer or gasten and chips and drank == True:
    print("Start the Party")
else:
    print('No Party')
    