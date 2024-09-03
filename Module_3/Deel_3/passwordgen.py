import string
import random
import time


opnieuw = True
letters = string.ascii_lowercase
hoofdletters = string.ascii_uppercase
tekens = '@#$%&_?'
getallen = '0123456789'


while opnieuw == True:
    randomhoofdletters = random.randint(2,6)
    randomgetallen = random.randint(4,7)
    randomletters = random.randint(8,10)
    wachtwoord = ''
    
    for x in range(8):
        wachtwoord += random.choice(letters)

    for x in range(randomhoofdletters):
        wachtwoord += random.choice(hoofdletters)

    for x in range(3):
        wachtwoord += random.choice(tekens)

    for x in range(randomgetallen):
        wachtwoord += random.choice(getallen)



    #time.sleep(3)
    wachtwoord = ''.join(random.sample(wachtwoord, len(wachtwoord)))
    

    if len(wachtwoord) == 24:
        if wachtwoord[11] and wachtwoord[12] not in hoofdletters:
            if wachtwoord[23] not in letters:
                if wachtwoord[0] and wachtwoord[23] not in tekens:
                    if wachtwoord[0] and wachtwoord[1] and wachtwoord[2] not in getallen:
                        opnieuw = False
                        print(wachtwoord)
                        print(len(wachtwoord))
                        print(wachtwoord[11], wachtwoord[12])
                        print(wachtwoord[23])
                        print(wachtwoord[0], wachtwoord[23])
                        print(wachtwoord[0] and wachtwoord[1] and wachtwoord[2])
    else:
        ()
        
    
    
