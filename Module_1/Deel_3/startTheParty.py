<<<<<<< Updated upstream
drank = True
chips = False
mijn_naam = ("Levi")
SLB_naam = ("Eugene")
gastheer = input("Naam gastheer ")
gasten = int(input("Hoeveel gasten? "))
=======
gastheer = True
gasten = False
drank = True
chips = False
jouw_naam = "Levi"
slber_naam = "Oorschot"
naam_gastheer = input("naam gastheer ")
>>>>>>> Stashed changes

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
elif naam_gastheer is not  jouw_naam or slber_naam:
    gastheer = False
elif gastheer or gasten and chips and drank == True:
    print("Start the Party")
<<<<<<< Updated upstream
=======
elif gastheer and drank == True:
    print("Start the Party")

elif gastheer == False and naam_gastheer == ("Levi"):
    print("No Party? ")
>>>>>>> Stashed changes
else:
    print('No Party')
