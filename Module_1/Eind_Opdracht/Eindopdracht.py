import time
import random

skip = 0
maxhp = 10
hp = 10
atk = 0
dmg = 0
day1 = 0
monster_hp_fase1 = 7
monster_hp_fase2 = 9
monster_hp_fase3 = 17
max_boss_hp = 50
sleepcount = 0
attackcount = 0

def monster_list(naam: str) -> str:
    Monsters = ("Goblin", "Slijm",)
    random_monster = random.choice(Monsters)
    return f"{naam} ziet een {random_monster}"

def monster_list_2(naam: str) -> str:
    Monsters2 = ("Golem", "Trol")
    random_monster2 = random.choice(Monsters2)
    return f"{naam} ziet een {random_monster2}"

def monster_list_3(naam: str) -> str:
    Monsters3 = ("Oni", "Spook")
    random_monster3 = random.choice(Monsters3)
    return f"{naam} ziet een {random_monster3}"

def Boss_list() -> str:
    Boss = ("Fire Storm", "Ice Storm")
    random_Boss = random.choice(Boss)
    return random_Boss

def stat_list() -> str:
    Stats = ("hp", "atk")
    random_stat = random.choice(Stats)
    return random_stat

def attack_list() -> int:
    attack = (1, 2, 3)
    damage = random.choice(attack)
    return damage

def attack_list2() -> int:
    attack = (1, 2, 3, 4, 5)
    damage = random.choice(attack)
    return damage

def attack_list3() -> int:
    attack = (3, 4, 5, 6, 7)
    damage = random.choice(attack)
    return damage

def attack_list_BOSS() -> int:
    attack = (5, 6, 7, 8, 9, 10)
    damage = random.choice(attack)
    return damage

def attack_skill_list_BOSS() -> int:
    attack = (7, 8, 9, 10, 11, 12, 13)
    damage = random.choice(attack)
    return damage

def skill_list_BOSS() -> str:
    skill = ("ATCK", "SKILL",)
    random_skill = random.choice(skill)
    return {random_skill}

def attack_list_u() -> int:
    attack = (1, 2, 3, 4, 5)
    damage_u = random.choice(attack)
    return damage_u

print(input("Druk op enter om te starten"))

print("Dit is een tekst adventure game. Het doel van het spel is om in 10 dagen een character te maken sterk genoeg om de baas te verslaan!")
time.sleep(2)

while True:
    name = input("Wat is de naam van je character? ")
    freestat = input("Je krijgt een bonus +3 voor een stat naar keuze welke kies je? (hp atk) ")

    if freestat.lower() == "hp":
        maxhp += 3 
        print("Je hebt hp gekozen")
        break
    elif freestat.lower() == "atk":
        atk += 3
        print("Je hebt atk gekozen")
        break
       
hp = maxhp
print(f"hp: {hp} atk: {atk}")
     
def fight_day():
    global  hp, atk, day1, maxhp, dmg, damage, attackcount, sleepcount

    while True:
        day1 = 0
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
                print(f"hp: {hp} atk: {atk}")

                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()
                    
                keuze_vecht1 = input("Wat wil je doen (Aanvallen, Rennen) ")
                
                if keuze_vecht1.lower() == "aanvallen":
                    damage_u = attack_list_u()
                    print("Je valt aan voor", damage_u + atk)
                    dmg += damage_u + atk
                    
                    if dmg >= monster_hp_fase1:
                        print("Je hebt Gewonnen !!")
                        dmg = 0
                        day1 = 1
                        attackcount =+ 1
                        random_stat = stat_list()
                        
                        if random_stat.lower() == "hp":
                            maxhp += 3 
                            print("Je hebt extra hp gekregen")
                        elif random_stat.lower() == "atk":
                            atk += 3
                            print("Je hebt extra atk gekregen")
                        break
                    
                if keuze_vecht1.lower() == "rennen":
                    print("Je bent weggerend")
                    time.sleep(2)
                    print("Einde dag")
                    day1 = 1
                    break

        if keuze_dag1.lower() == "slapen":
            hp = maxhp
            print(f"hp: {hp} atk: {atk}")
            print("Je hebt geslapen, je HP is weer naar zijn maximum")
            day1 = 1
            sleepcount =+ 1
            break
        if day1 == 1:
            day1 = 0
            break
           
            
            
def fight_day1():
    global  hp, atk, day1, maxhp, dmg, damage, sleepcount, attackcount

    while True:
        day1 = 0
        keuze_dag1 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

        if keuze_dag1.lower() == "vechten":
            time.sleep(2)
            print(monster_list_2(name))
            time.sleep(2)
            print("Het monster heeft 9 hp")
            time.sleep(2)
            
            while True:
                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()
                damage = attack_list2()
                print("Je wordt geraakt voor", damage)
                hp -= damage
                print(f"hp: {hp} atk: {atk}")
                
                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()
                    
                keuze_vecht1 = input("Wat wil je doen (Aanvallen, Rennen) ")
                
                if keuze_vecht1.lower() == "aanvallen":
                    damage_u = attack_list_u()
                    print("Je valt aan voor", damage_u + atk)
                    dmg += damage_u + atk
                    
                    if dmg >= monster_hp_fase2:
                        print("Je hebt Gewonnen !!")
                        dmg = 0
                        day1 = 1
                        attackcount =+ 1
                        random_stat = stat_list()
                        
                        if random_stat.lower() == "hp":
                            maxhp += 5 
                            print("Je hebt extra hp gekregen")
                        elif random_stat.lower() == "atk":
                            atk += 5
                            print("Je hebt extra atk gekregen")        
                        break
                    
                if keuze_vecht1.lower() == "rennen":
                    print("Je bent weggerend")
                    time.sleep(2)
                    print("Einde dag")
                    day1 = 1
                    break
                    
        if keuze_dag1.lower() == "slapen":
            hp = maxhp
            sleepcount =+ 1
            print(f"hp: {hp} atk: {atk}")
            print("Je hebt geslapen, je HP is weer naar zijn maximum")
            day1 = 1
            break
        if day1 == 1:
            day1 = 0
            break
        
            
    
def fight_day2():
    global  hp, atk, day1, maxhp, dmg, damage, sleepcount, attackcount

    while True:
        day1 = 0
        keuze_dag1 = input("Wat wil je vandaag doen? (Vechten, Slapen) ")

        if keuze_dag1.lower() == "vechten":
            time.sleep(2)
            print(monster_list_3(name))
            time.sleep(2)
            print("Het monster heeft 17 hp")
            time.sleep(2)
            
            while True:
                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()
                damage = attack_list3()
                print("Je wordt geraakt voor", damage)
                hp -= damage
                print(f"hp: {hp} atk: {atk}")
                
                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()
                    
                keuze_vecht1 = input("Wat wil je doen (Aanvallen, Rennen) ")
                
                if keuze_vecht1.lower() == "aanvallen":
                    damage_u = attack_list_u()
                    print("Je valt aan voor", damage_u + atk)
                    dmg += damage_u + atk
                    
                    if dmg >= monster_hp_fase3:
                        print("Je hebt Gewonnen !!")
                        dmg = 0
                        day1 = 1
                        attackcount =+ 1
                        random_stat = stat_list()
                        
                        if random_stat.lower() == "hp":
                            maxhp += 7 
                            print("Je hebt extra hp gekregen")
                        elif random_stat.lower() == "atk":
                            atk += 7
                            print("Je hebt extra atk gekregen")     
                        break
                    
                if keuze_vecht1.lower() == "rennen":
                    print("Je bent weggerend")
                    time.sleep(2)
                    print("Einde dag")
                    day1 = 1
                    break
                    
        if keuze_dag1.lower() == "slapen":
            hp = maxhp
            sleepcount += 1
            print(f"hp: {hp} atk: {atk}")
            print("Je hebt geslapen, je HP is weer naar zijn maximum")
            day1 = 1
            break
        if day1 == 1:
            day1 = 0
            break
       
            
def boss_fight():
    global hp, atk, day1, maxhp, dmg, damage, random_skill, random_boss

    while True:
        day1 = 0
        keuze_dag1 = input("Wat wil je vandaag doen? (Vechten) ")

        if keuze_dag1.lower() == "vechten":
            time.sleep(2)
            random_boss = Boss_list()
            print(f"je ziet de Boss {random_boss}")
            time.sleep(2) 

            if random_boss == "Fire Storm":
                print("De Boss heeft 50 hp en kan de SKILL Fireball gebruiken")
            elif random_boss == "Ice Storm":
                print("De Boss heeft 50 hp en kan de SKILL Iceball gebruiken")

            while True:
                random_skill = skill_list_BOSS()
            
                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()
                if random_skill == {"ATCK"}:
                    damage = attack_list_BOSS()
                    print("Je wordt geraakt voor", damage)
                    hp -= damage
                    print(f"hp: {hp} atk: {atk}")
                elif random_boss == "Fire Storm" and random_skill == {"SKILL"}:
                    damage = attack_skill_list_BOSS()
                    print("Je wordt geraakt voor", damage, "Door een fireball")
                    hp -= damage
                    print(f"hp: {hp} atk: {atk}")
                elif random_boss == "Ice Storm" and random_skill == {"SKILL"}:
                    damage = attack_skill_list_BOSS()
                    print("Je wordt geraakt door voor", damage, "Door een Iceball")
                    hp -= damage
                    print(f"hp: {hp} atk: {atk}")

                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    exit()

                keuze_vecht1 = input("Wat wil je doen (Aanvallen, Rennen) ")

                if keuze_vecht1.lower() == "aanvallen":
                    damage_u = attack_list_u()
                    print("Je valt aan voor", damage_u + atk)
                    dmg += damage_u + atk

                    if dmg >= max_boss_hp:
                        print("Je hebt Gewonnen !!")
                        dmg = 0
                        day1 = 1
                        print(f"Je hebt de Boss verslagen met{maxhp} hp en {atk} atk ")
                        print(f"je heb {sleepcount} geslapen en {attackcount} gevochten")
                        exit()

                if keuze_vecht1.lower() == "rennen":
                    print("Je bent weggerend van de boss ")
                    time.sleep(2)
                    print("Einde dag")
                    day1 = 1
                    break

                if day1 == 1:
                    day1 = 0
                    break
          
print("Dag 1")
for dag in range(1, 3):  
    fight_day()
    print(f"Dag {dag + 1}")

for dag in range(3, 6):  
    fight_day1()
    print(f"Dag {dag + 1}")

for dag in range(6, 11):  
    fight_day2()
    print(f"Dag {dag + 1}")

while True:
    print("Boss fight")
    boss_fight()