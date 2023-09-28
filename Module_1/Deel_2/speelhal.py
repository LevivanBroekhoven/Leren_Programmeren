aantal_mensen = int(input("met hoeveel mensen ga je? "))
aantal_minuten_VR = int(input("hoeveel minuten VR wil je? "))


ENTRE = 7.45
PRIJSVRPER5MINUTEN = 0.37
HOEVEELMINUTEN = 5

minuten_VR = aantal_minuten_VR / HOEVEELMINUTEN
prijs_VR = minuten_VR * PRIJSVRPER5MINUTEN
totale_kostepp = prijs_VR + ENTRE
totale_kosten = totale_kostepp * aantal_mensen



print("Dit geweldige dagje-uit met" ,aantal_mensen,"mensen in de Speelhal met",aantal_minuten_VR,"minuten VR kost je maar",round(totale_kosten,2),"euro totaal")