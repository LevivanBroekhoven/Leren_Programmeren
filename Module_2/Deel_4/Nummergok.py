import random 
ronde = 1
getal = 1 #random.randint(1,1)
aantalgok = 0
punten = 0

while ronde < 3:
    while aantalgok < 10:
        print(f"ronde {ronde}")
        gok = int(input("getal "))
        if gok == getal:
            ronde += 1
            punten +=1
            print("Geraden")
            print(f"punten {punten}")
            aantalgok = 0
            if ronde != 3:
                Doorgaan = input("Wil je doorgaan? ")
                if Doorgaan == "ja":
                    break
            else:
                exit(aantalgok)
        else:
            print("fout")
        
print("test")