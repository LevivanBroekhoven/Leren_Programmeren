from StudieadviesTEXT import *

print (StudieadviesText)

aantal_weeken_vraag = int(input('Hoeveel weken ben je al bezig met de opleiding? '))
print(OPTIES)
COMPETENTIE_STELLING_1 = int(input('Ik voel stress of blokkades bij het maken van programmeeropdrachten: '))
print(OPTIES)
COMPETENTIE_STELLING_2 = int(input('Ik stel programmeeropdrachten en -uitdagingen uit: '))
print(OPTIES)
COMPETENTIE_STELLING_3 = int(input('Ik denk dat ik geen talent heb voor de opleiding: '))
print(OPTIES)
COMPETENTIE_STELLING_4 = int(input('Ik vermijd assessments (CJV) en feedback van kritische docenten: '))
print(OPTIES)
COMPETENTIE_STELLING_5 = int(input('Ik vergelijk mezelf met anderen die beter lijken te zijn: '))

if aantal_weeken_vraag >= 10:
    print(OPTIES)
    COMPETENTIE_STELLING_6 = int(input('Ik voel geen interesse in nieuwe programmeertechnieken: '))
    print(OPTIES) 
    COMPETENTIE_STELLING_7 = int(input('Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is: '))
elif aantal_weeken_vraag < 10:
    COMPETENTIE_STELLING_6 = ("Niks")
    COMPETENTIE_STELLING_7 = ("Niks")

count_altijd = 0
count_vaak = 0
count_regelmatig = 0
advies = "test"
advies2 = "test"
aatal_weken = 5

if COMPETENTIE_STELLING_1 == 0:
    count_altijd += 1
elif COMPETENTIE_STELLING_1 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_1 == 1:
    count_vaak = count_vaak + 1
if COMPETENTIE_STELLING_2 == 0:
    count_altijd = count_altijd + 1
elif COMPETENTIE_STELLING_2 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_2 == 1:
    count_vaak = count_vaak + 1
if COMPETENTIE_STELLING_3 == 0:
    count_altijd = count_altijd + 1
elif COMPETENTIE_STELLING_3 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_3 == 1:
    count_vaak = count_vaak + 1
if COMPETENTIE_STELLING_4 == 0:
    count_altijd = count_altijd + 1
elif COMPETENTIE_STELLING_4 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_4 == 1:
    count_vaak = count_vaak + 1
if COMPETENTIE_STELLING_5 == 0:
    count_altijd = count_altijd + 1
elif COMPETENTIE_STELLING_5 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_5 == 1:
    count_vaak = count_vaak + 1
if COMPETENTIE_STELLING_6 == 0:
    count_altijd = count_altijd + 1
elif COMPETENTIE_STELLING_6 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_6 == 1:
    count_vaak = count_vaak + 1
if COMPETENTIE_STELLING_7 == 0:
    count_altijd = count_altijd + 1
elif COMPETENTIE_STELLING_7 == 2:
    count_regelmatig = count_regelmatig + 1
elif COMPETENTIE_STELLING_7 == 1:
    count_vaak = count_vaak + 1

uitslag = COMPETENTIE_STELLING_1 + COMPETENTIE_STELLING_2 + COMPETENTIE_STELLING_3 + COMPETENTIE_STELLING_4 + COMPETENTIE_STELLING_5 

if aantal_weeken_vraag >= 10:
    uitslag += COMPETENTIE_STELLING_6 + COMPETENTIE_STELLING_7 

if aantal_weeken_vraag >= 10:
    aatal_weken = 7

result1 = count_altijd / aatal_weken
result2 = count_vaak / aatal_weken
result3 = count_regelmatig / aatal_weken

if aatal_weken == 7:
    if result1 >= 3.5 or result2 >= 3.5:
        advies = "True"
    if result1 >= 3.5 and result2 >= 3.5 or result3 >= 3.5:
            advies2 = "True"
if aatal_weken == 5:
    if result1 >= 2.5 or result2 >= 2.5:
        advies = "True"
    if result1 >= 2.5 and result2 >= 2.5 or result3 >= 2.5:
            advies2 = "True"


print(Studieadvies)

print (count_regelmatig, count_altijd, count_vaak )
print (result1 ,result2, result3)
if uitslag >= 2 or advies == "True":
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif uitslag == 3 or advies2 == "True":
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
