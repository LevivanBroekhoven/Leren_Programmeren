from RFunctions import *
nummer1 = None
nummer2 = 0


while True:
    if nummer1 != None:
        print(f"Wat wilt u doen met de uitkomst {nummer1} ")
    if nummer1 != None:
        choice = input("\n A)getallen optellen,\n B)getallen aftrekken,\n C)getallen vermenigvuldigen,\n D)getallen delen,\n E)getal ophogen,\n F)getal verlagen,\n G)getal verdubbelen\n H)getal halveren?\n I) stoppen\n")
    else:
        choice = input("wat wilt u doen?\n A)getallen optellen,\n B)getallen aftrekken,\n C)getallen vermenigvuldigen,\n D)getallen delen,\n E)getal ophogen,\n F)getal verlagen,\n G)getal verdubbelen\n H)getal halveren?\n")

    if choice == "A":
        nummer1 = nummerV(nummer1)

        nummer2 = nummerV2(nummer2)
        a,b = optellen(nummer1, nummer2)
        nummer1 = b
        print(a)

    if choice == "B":
        nummer1 = nummerV(nummer1)

        nummer2 = nummerV2(nummer2)
        a, b = aftrekken(nummer1,nummer2)
        nummer1 = b 
        print(a)
         
    if choice == "C":
        nummer1 = nummerV(nummer1)

        nummer2 = nummerV2(nummer2)
        a, b = keer(nummer1,nummer2)
        nummer1 = b 
        print(a)
        
    if choice == "D":
        while True:
            nummer1 = nummerV(nummer1)
            if nummer1 != 0:
                break
        while True:
            nummer2 = nummerV2(nummer2)
            if nummer1 != 0:
                break
        a, b = delen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "E":
        nummer1 = nummerV(nummer1)

        nummer2 = 1
        a, b = ophogen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "F":
        nummer1 = nummerV(nummer1)

        nummer2 = 1
        a, b = verlagen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "G":
        nummer1 = nummerV(nummer1)

        nummer2 = 2
        a, b = verdubbelen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "h":
        nummer1 = nummerV(nummer1)

        nummer2 = 2
        a, b = halveren(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if nummer1 != None:
        if choice == "I":
         break

    




