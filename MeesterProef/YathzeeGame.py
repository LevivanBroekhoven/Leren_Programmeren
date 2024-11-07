from Yathzee import *

EersteWorp = fivenumbergen()
print(EersteWorp)

for x in range(3):
    redobble = input("Wil je herdobbelen?")

    if redobble == ("ja"):
        hoeveeldobble= input("Hoeveel wil je herdobbelen?")
        for x in range(hoeveeldobble):
            welkedobble = input("Welke wil je herdobbelen? ")

