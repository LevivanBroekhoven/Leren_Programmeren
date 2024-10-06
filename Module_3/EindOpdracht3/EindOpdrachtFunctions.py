from EindOpdracht3Data import *
aantalbolletjes = 0
    
def Vraag_bolletjes():
    global aantalbolletjes
    while True:
        try:
            bolletje = int(input("Hoeveel bolletjes wilt u? "))
            aantalbolletjes += bolletje
            return(bolletje)
        
        except ValueError:
            print("Sorry, dat snap ik niet.")


def kies_horen_of_bakje(bolletje):

    while True:
        if MIN_BOLLETJES <= bolletje <= MAX_BOLLETJES_HOORNTJE:
            hoorntjeofBakje = input(f"Wilt u deze {bolletje} bolletjes in een hoorntje of bakje? ")
            if hoorntjeofBakje == "hoorntje":
                print(f"Hier is uw {bolletje} bolletjes in een hoorntje.")
                break
            elif hoorntjeofBakje == "bakje":
                print(f"Hier is uw {bolletje} bolletjes in een bakje.")
                break
        if MAX_BOLLETJES_HOORNTJE <= bolletje <= MAX_BOLLETJES_BAKJE:
            print(f"Hier is uw {bolletje} bolletjes in een bakje.")
            break

        elif bolletje > MAX_BOLLETJES_BAKJE:
            print("Sorry, zulke grote bakken hebben we niet.")
            bolletje = Vraag_bolletjes()
            
            
        else:
            print("Sorry, dat snap ik niet.")

        
          


def meerbestellen():
    jofninput = input("Wilt u nog meer bestellen? (Ja/Nee) ")
    if jofninput == "nee":
        print("Bedankt en tot ziens!")
        return("nee")

    if jofninput == "ja":
        return()
    else:
        print("Sorry, dat snap ik niet.")

def bonnetje(bolletjes):
    global aantalbolletjes

    

    print("-----[Papi Gelato]-----")
    print(f"Bolletjes = {aantalbolletjes}")


         
    