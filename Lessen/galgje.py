from string import ascii_lowercase
teraden = ("astronaut")
Geraden = '-' * len(teraden)

while True:
    def get_letter() -> str:
        while True:
            letter = input("welke letter? ")
            if letter not in ascii_lowercase:
                print("letter doen")
            elif len(letter) != 1:
                print("maar 1 letter")
            else:
                return letter
            
    lettergeraden = get_letter()



    if lettergeraden in teraden:
        print(f"{lettergeraden} zit in het woord")
        geraden_list = list(Geraden)

        for x in range(len(teraden)):
            if teraden[x] == lettergeraden:
                geraden_list[x] = lettergeraden
            
        Geraden = "".join(geraden_list)
        print(Geraden)
        


    if lettergeraden not in teraden:
        print("fout letter zit niet in het woord")

    if Geraden == teraden:
        print("je heb het woord goed geraden !!!")
        break