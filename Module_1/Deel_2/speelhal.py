aantal_mensen = int(input("met hoeveel mensen ga je? "))
aantal_minuten_VR = int(input("hoeveel minuten VR wil je? "))


ENTRE = 745
PRIJSVRPER5MINUTEN = 37
HOEVEELMINUTEN = 5

minuten_VR = aantal_minuten_VR / HOEVEELMINUTEN
prijs_VR = minuten_VR * PRIJSVRPER5MINUTEN
totale_kostepp = prijs_VR + ENTRE

totale_kostenC = totale_kostepp * aantal_mensen
totale_kostenE = round(totale_kostenC / 100 ,2)



print("Dit geweldige dagje-uit met" ,aantal_mensen,"mensen in de Speelhal met",aantal_minuten_VR,"minuten VR kost je maar",totale_kostenE,"euro totaal")