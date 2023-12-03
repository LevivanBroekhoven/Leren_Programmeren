import time
from time import *
import random
skip = 0
maxhp = 10
hp = 10
atk = 0
Dmg = 0
Day1 = 0
Day2 = 0
Day3 = 0
Day4 = 0
Day5 = 0
Day6 = 0
Day7 = 0
Day8 = 0 
Day9 = 0
Day10 = 0


def Monster_Lijst(naam: str) -> str:
    Monsters = ("Goblin", "Slijm",)
    random_monster = random.choice(Monsters)
    return  naam + " ziet een " + random_monster

def Monster_Lijst2(naam: str) -> str:
    Monsters2 = ("Golem", "Trol")
    random_monster2 = random.choice(Monsters2)
    return  naam + " ziet een " + random_monster2

def Monster_Lijst3(naam: str) -> str:
    Monsters3 = ("Oni", "")
    random_monster3 = random.choice(Monsters3)
    return  naam + " ziet een " + random_monster3

def Stat_Lijst() -> str :
    Stats = ("hp","atk")
    random_stats = random.choice(Stats)
    return random_stats

def attack_Lijst() -> int:
    attack = (1, 2, 3)
    damage = random.choice(attack)
    return damage

def attack_LijstU() -> int:
    attack = (1, 2, 3, 4, 5)
    damageU = random.choice(attack)
    return damageU

print (input("Druk op enter om te starten"))

UitlegTof = input("Wil je de uitleg horen? ")

if UitlegTof.lower() == "ja":
    print("Dit is een tekst adventure game het doel van het spel is om in 10 dagen een character te maken sterk genoeg om de baas te verslaan!")
    sleep(3)
    skip = 1

if UitlegTof.lower() == "nee":
    skip = 1

if skip == 1:
    Name = input("Wat is de naam van je character? ")
    freestat = input("Je krijgt een bonus +3 voor een stat naar keuze welke kies je? (hp atk) ")

    if freestat.lower() == "hp":
        maxhp += 3 
        print("Je hebt hp gekozen")
    elif freestat.lower() == "atk":
        atk += 3
        print("Je hebt atk gekozen")

hp = maxhp
print (hp, atk)

print("DAY 1")

KeuzeDag1 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag1.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht1 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht1 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day1 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht1 == "Rennen":
            Day1 = 1
            break

if KeuzeDag1.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day1 = 1

if Day1 == 1:
    print("DAY 2")
KeuzeDag2 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag2.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht2 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht2 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day2 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht2 == "Rennen":
            Day2 = 1
            break

if KeuzeDag2.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day2 = 1

if Day2 == 1:
    print("DAY 3")
KeuzeDag3 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag3.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht3 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht3 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day3 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht3 == "Rennen":
            Day3 = 1
            break

if KeuzeDag3.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day3 = 1

if Day3 == 1:
    print("DAY 4")
KeuzeDag4 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag4.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht4 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht4 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day4 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht4 == "Rennen":
            Day4 = 1
            break

if KeuzeDag4.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day4 = 1

if Day4 == 1:
    print("DAY 5")
KeuzeDag5 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag5.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht5 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht5 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day5 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht5 == "Rennen":
            Day5 = 1
            break

if KeuzeDag5.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day5 = 1

if Day5 == 1:
    print("DAY 6")
KeuzeDag6 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag6.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht6 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht6 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day6 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht6 == "Rennen":
            Day6 = 1
            break

if KeuzeDag6.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day6 = 1

if Day6 == 1:
    print("DAY 7")
KeuzeDag7 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag7.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht7 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht7 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day7 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht5 == "Rennen":
            Day7 = 1
            break

if KeuzeDag7.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day7 = 1

if Day7 == 1:
    print("DAY 8")
KeuzeDag8 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag8.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht8 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht8 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day8 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht8 == "Rennen":
            Day8 = 1
            break

if KeuzeDag8.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day8 = 1

if Day8 == 1:
    print("DAY 9")
KeuzeDag9 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag9.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht9 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht9 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day9 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht9 == "Rennen":
            Day9 = 1
            break

if KeuzeDag9.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day9 = 1

if Day9 == 1:
    print("DAY 10")
KeuzeDag10 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

if KeuzeDag10.lower() == "vechten":
    sleep(2)
    print(Monster_Lijst(Name))
    sleep(2)
    print("Het monster heeft 7 hp")
    sleep(2)
    while True:
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        damage = attack_Lijst()
        print("Je wordt geraakt voor", damage)
        hp -= damage
        print (hp, atk)
        if hp <= 0:
            print("Je ben dood GAME OVER!!!")
            exit()
        KeuzeVecht10 = input ("Wat wil je doen (Aanvallen, Rennen) ")
        if KeuzeVecht10 == "Aanvallen":
            damageU = attack_LijstU()
            print("Je valt aan voor", damageU + atk)
            Dmg += damageU + atk
            if Dmg >= 7:
                print("Je hebt Gewonnen !!")
                Dmg = 0
                Day10 = 1
                randomstat = Stat_Lijst()
                if randomstat.lower() == "hp":
                    maxhp += 3 
                    print("Je heb extra hp gekregen")
                elif randomstat.lower() == "atk":
                    atk += 3
                    print("Je heb extra atk gekregen")    
                break
        if KeuzeVecht10 == "Rennen":
            Day10 = 1
            break

if KeuzeDag10.lower() == "slapen":
    hp = maxhp
    print (hp, atk)
    print("Je hebt geslapen, je HP is weer naar zijn maximum")
    Day10 = 1




