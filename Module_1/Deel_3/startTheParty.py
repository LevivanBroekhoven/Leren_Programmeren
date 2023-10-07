gasten = True
drank = True
chips = True
mijn_naam = ("Levi")
SLB_naam = ("Eugene")
gastheer = input("Naam gastheer")



if gastheer == mijn_naam:
    print('No Party')
elif gastheer == SLB_naam:
    print('No Party')
elif gastheer == (" "):
    gastheer == False
elif gasten and drank and chips == True:
    print('Start the Party')
elif gastheer or gasten and chips and drank == True:
    print("Start the Party")
elif gastheer and drank == True:
    print("Start the Party")
else:
    print('No Party')