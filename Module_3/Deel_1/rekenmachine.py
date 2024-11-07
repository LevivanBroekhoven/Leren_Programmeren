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
    choice_ok = True
    if choice == "A":
        nummer1 = nummerV(nummer1)

        nummer2 = nummerV2(nummer2)
        print_result, result = optellen(nummer1, nummer2)


    elif choice == "B":
        nummer1 = nummerV(nummer1)

        nummer2 = nummerV2(nummer2)
        print_result, result = aftrekken(nummer1,nummer2)

         
    elif choice == "C":
        nummer1 = nummerV(nummer1)

        nummer2 = nummerV2(nummer2)
        print_result, result = keer(nummer1,nummer2)

        
    elif choice == "D":
        while True:
            nummer1 = nummerV(nummer1)
            if nummer1 != 0:
                break
        while True:
            nummer2 = nummerV2(nummer2)
            if nummer1 != 0:
                break
        print_result, result = delen(nummer1,nummer2)


    elif choice == "E":
        nummer1 = nummerV(nummer1)

        nummer2 = 1
        print_result, result = ophogen(nummer1,nummer2)


    elif choice == "F":
        nummer1 = nummerV(nummer1)

        nummer2 = 1
        print_result, result = verlagen(nummer1,nummer2)


    elif choice == "G":
        nummer1 = nummerV(nummer1)

        nummer2 = 2
        print_result, result = verdubbelen(nummer1,nummer2)


    elif choice == "H":
        nummer1 = nummerV(nummer1)

        nummer2 = 2
        print_result, result = halveren(nummer1,nummer2)


    elif nummer1 != None:
        if choice == "I":
         break

    else:
        print("Onbekende input \n")
        choice_ok = False
        
    if choice_ok:
        nummer1 = result
        print(print_result)

    




