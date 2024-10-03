print("Welkom bij Papi Gelato! Je mag alle smaken kiezen zolang het maar vanille ijs is.")

while True:
    try:
        bolletje = int(input("Hoeveel bolletjes wilt u? "))

        if 1 <= bolletje <= 3:
            while True:
                hoorntjeofBakje = input(f"Wilt u deze {bolletje} bolletjes in een hoorntje of bakje? ")
                if hoorntjeofBakje == "hoorntje":
                    print(f"Hier is uw {bolletje} bolletjes in een hoorntje.")
                    break
                elif hoorntjeofBakje == "bakje":
                    print(f"Hier is uw {bolletje} bolletjes in een bakje.")
                    break
                else:
                    print("Sorry dat snap ik niet")


        elif 4 <= bolletje <= 8:
            print(f"Hier is uw {bolletje} bolletjes in een bakje.")

        elif bolletje > 8:
            print("Sorry, zulke grote bakken hebben we niet.")

        else:
            print("Graag een geldig aantal bolletjes in te voeren.")

        jofninput = input("Wilt u nog meer bestellen? (Ja/Nee) ")
        if jofninput == "nee":
            print("Bedankt en tot ziens!")
            break
        if jofninput == "ja":
            ()
        else:
            print("Sorry, dat snap ik niet.")

    except ValueError:
        print("Sorry, dat snap ik niet.")
