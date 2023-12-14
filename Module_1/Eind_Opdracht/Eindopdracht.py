import time
import random

skip = 0
maxhp = 10
hp = 10
atk = 0
dmg = 0
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0
day6 = 0
day7 = 0
day8 = 0 
day9 = 0
day10 = 0

def monster_list(naam: str) -> str:
    Monsters = ("Goblin", "Slijm",)
    random_monster = random.choice(Monsters)
    return f"{naam} ziet een {random_monster}"

def monster_list_2(naam: str) -> str:
    Monsters2 = ("Golem", "Trol")
    random_monster2 = random.choice(Monsters2)
    return f"{naam} ziet een {random_monster2}"

def monster_list_3(naam: str) -> str:
    Monsters3 = ("Oni", "")
    random_monster3 = random.choice(Monsters3)
    return f"{naam} ziet een {random_monster3}"

def stat_list() -> str:
    Stats = ("hp", "atk")
    random_stat = random.choice(Stats)
    return random_stat

def attack_list() -> int:
    attack = (1, 2, 3)
    damage = random.choice(attack)
    return damage

def attack_list_u() -> int:
    attack = (1, 2, 3, 4, 5)
    damage_u = random.choice(attack)
    return damage_u

print(input("Druk op enter om te starten"))

uitleg_tof = input("Wil je de uitleg horen? ")

if uitleg_tof.lower() == "ja":
    print("Dit is een tekst adventure game. Het doel van het spel is om in 10 dagen een character te maken sterk genoeg om de baas te verslaan!")
    time.sleep(3)
    skip = 1

if uitleg_tof.lower() == "nee":
    skip = 1

if skip == 1:
    while True:
        name = input("Wat is de naam van je character? ")
        freestat = input("Je krijgt een bonus +3 voor een stat naar keuze welke kies je? (hp atk) ")

        if freestat.lower() == "hp":
            maxhp += 3 
            print("Je hebt hp gekozen")
        elif freestat.lower() == "atk":
            atk += 3
            print("Je hebt atk gekozen")
        if name and freestat:
            break

hp = maxhp
print(hp, atk)

print("day 1")
while True:
    keuze_dag1 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag1.lower() == "vechten":
        time.sleep(2)
        print(monster_list(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht1 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht1.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day1 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht1.lower() == "rennen":
                day1 = 1
                break
    if keuze_dag1.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day1 = 1
        break
    if keuze_dag1:
        break


if day1 == 1:
    print("day 2")
while True:
    keuze_dag2 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag2.lower() == "vechten":
        time.sleep(2)
        print(monster_list(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht2 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht2.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day1 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht2.lower() == "rennen":
                day2 = 1
                break
    if keuze_dag2.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day2 = 1
        break
    if keuze_dag2:
        break


if day2 == 1:
    print("day 3")
while True:
    keuze_dag3 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag3.lower() == "vechten":
        time.sleep(2)
        print(monster_list(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht3 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht3.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day3 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht3.lower() == "rennen":
                day3 = 1
                break
    if keuze_dag3.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day3 = 1
        break
    if keuze_dag3:
        break


if day3 == 1:
    print("day 4")
while True:
    keuze_dag4 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag4.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht4 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht4.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day4 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht4.lower() == "rennen":
                day4 = 1
                break
    if keuze_dag4.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day4 = 1
        break
    if keuze_dag4:
        break


if day4 == 1:
    print("day 5")
while True:
    keuze_dag5 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag5.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht5 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht5.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day5 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht5.lower() == "rennen":
                day5 = 1
                break
    if keuze_dag5.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day5 = 1
        break
    if keuze_dag5:
        break


if day5 == 1:
    print("day 6")
while True:
    keuze_dag6 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag6.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht6 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht6.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day6 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht6.lower() == "rennen":
                day6 = 1
                break
    if keuze_dag6.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day6 = 1
        break
    if keuze_dag6:
        break


if day6 == 1:
    print("day 7")
while True:
    keuze_dag7 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag7.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht7 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht7.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day7 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht7.lower() == "rennen":
                day7 = 1
                break
    if keuze_dag7.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day7 = 1
        break
    if keuze_dag7:
        break


if day7 == 1:
    print("day 8")
while True:
    keuze_dag8 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag8.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht8 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht8.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day8 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht8.lower() == "rennen":
                day8 = 1
                break
    if keuze_dag8.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day8 = 1
        break
    if keuze_dag8:
        break


if day8 == 1:
    print("day 9")
while True:
    keuze_dag9 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag9.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht9 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht9.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day9 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht9.lower() == "rennen":
                day9 = 1
                break
    if keuze_dag9.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day9 = 1
        break
    if keuze_dag9:
        break


if day9 == 1:
    print("day 10")
while True:
    keuze_dag10 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

    if keuze_dag10.lower() == "vechten":
        time.sleep(2)
        print(monster_list_2(name))
        time.sleep(2)
        print("Het monster heeft 7 hp")
        time.sleep(2)
        while True:
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            damage = attack_list()
            print("Je wordt geraakt voor", damage)
            hp -= damage
            print(hp, atk)
            if hp <= 0:
                print("Je bent dood GAME OVER!!!")
                exit()
            keuze_vecht10 = input("Wat wil je doen (Aanvallen, Rennen) ")
            if keuze_vecht10.lower() == "aanvallen":
                damage_u = attack_list_u()
                print("Je valt aan voor", damage_u + atk)
                dmg += damage_u + atk
                if dmg >= 7:
                    print("Je hebt Gewonnen !!")
                    dmg = 0
                    day10 = 1
                    random_stat = stat_list()
                    if random_stat.lower() == "hp":
                        maxhp += 3 
                        print("Je hebt extra hp gekregen")
                    elif random_stat.lower() == "atk":
                        atk += 3
                        print("Je hebt extra atk gekregen")    
                    break
            if keuze_vecht10.lower() == "rennen":
                day10 = 1
                break
    if keuze_dag10.lower() == "slapen":
        hp = maxhp
        print(hp, atk)
        print("Je hebt geslapen, je HP is weer naar zijn maximum")
        day10 = 1
        break
    if keuze_dag10:
        break




