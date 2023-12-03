import random
from time import *

def generate_compliments(naam: str) -> str:
    COMPLIMENTEN = ("Je maakt mooie code", "Je helpt andere met code", "Goed bezig met programmeren")
    random_compliment = random.choice(COMPLIMENTEN)
    return random_compliment + naam


print("Even geduld")
sleep(5)
print(generate_compliments(" Levi"))