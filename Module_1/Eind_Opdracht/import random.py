import random
hp = 0

hitpoints = " "
def monster_list_hp(hitpoints: str ) -> int:
    Monstershp = ("5","6", "7")
    random_monsterhp = random.choice(Monstershp)
    return f"{hitpoints} {random_monsterhp}"

hp = (monster_list_hp(hp)) 

print (hp)  