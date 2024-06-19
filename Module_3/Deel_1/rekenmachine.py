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
        if nummer1 == None:
             while True:
                try:
                    nummer1 = float(input("welk getal? "))
                    break
                except:
                    print("geen geldig getal")
        while True:
            try:
                nummer2 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        a,b = optellen(nummer1, nummer2)
        nummer1 = b
        print(a)

    if choice == "B":
        if nummer1 == None:
            while True:
                try:
                    nummer1 = float(input("welk getal? "))
                    break
                except:
                    print("geen geldig getal")
        while True:
            try:
                nummer2 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        a, b = aftrekken(nummer1,nummer2)
        nummer1 = b 
        print(a)
         
    if choice == "C":
        if nummer1 == None:
            while True:
                try:
                    nummer1 = float(input("welk getal? "))
                    break
                except:
                    print("geen geldig getal")
                 
        while True:
            try:
                nummer2 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        a, b = keer(nummer1,nummer2)
        nummer1 = b 
        print(a)
        
    if choice == "D":
        if nummer1 == None:
            while True:
                try:
                    nummer1 = float(input("welk getal? "))
                    break
                except:
                    print("geen geldig getal")
            
        while True:
            try:
                nummer2 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        a, b = delen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "E":
        if nummer1 == None:
            try:
                nummer1 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        nummer2 = 1
        a, b = ophogen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "F":
        if nummer1 == None:
            try:
                nummer1 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        nummer2 = 1
        a, b = verlagen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "G":   
        if nummer1 == None:
            try:
                nummer1 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        nummer2 = 2
        a, b = verdubbelen(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if choice == "h":
        if nummer1 == None:
            try:
                nummer1 = float(input("welk getal? "))
                break
            except:
                print("geen geldig getal")
        nummer2 = 2
        a, b = halveren(nummer1,nummer2)
        nummer1 = b 
        print(a)

    if nummer1 != None:
        if choice == "I":
         break




