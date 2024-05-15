from fruitmand import *
kleurenlijst = []
rond = 0
nietrond = 0

for x in (fruitmand):
    kleurenlijst.append(x['color'])
    print(x['color'])


kleurC = input("Welke kleur wil je kiezen? ")

if kleurC not in kleurenlijst:
    print("keuze niet in de opties")

for x in (fruitmand):
    if (x['color']) == kleurC:
        r_or_nr= (x['round'])
        if r_or_nr == True:
            rond +=1
        else:
            nietrond += 1
        

if rond > nietrond:
    X = rond - nietrond
elif nietrond > rond:
    X = nietrond - rond
else:
    X = rond


if rond > nietrond:
    print(f"{X} meer ronde vruchten dan niet ronde vruchten in de kleur {kleurC}")
          
if nietrond > rond:
    print(f"Er zijn {X} minder ronde vruchten dan niet ronde vruchten in de kleur {kleurC}")

if nietrond == rond:
    (f"Er zijn {X} ronde vruchten en {X} niet ronde vruchten in de kleur {kleurC}")