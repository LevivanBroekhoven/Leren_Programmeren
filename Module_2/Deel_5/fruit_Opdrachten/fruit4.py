from fruitmand import *
import random
fruitaantal = int(input("Aantal? "))

for x in range(fruitaantal):
    print(fruitmand[random.randint(0,len(fruitmand)-1)]['name'])