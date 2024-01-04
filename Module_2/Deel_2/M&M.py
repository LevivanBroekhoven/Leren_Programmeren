import random
kleuren = ('oranje', 'blauw', 'groen', 'bruin')

def vul_zak_met_mms(aantal_mms):
    zak_mms = []
    for x in range(aantal_mms):
        kleur = random.choice(kleuren)
        zak_mms.append(kleur)
    return zak_mms

aantal_mms = int(input("Hoeveel wil je toevoegen aan de zak? "))
gevulde_zak = vul_zak_met_mms(aantal_mms)
print("Inhoud van de zak M&M's:", gevulde_zak)  