Geel = input("is de kaas geel?")
if Geel == "ja":
    Gaten = input("Zitten er gaten in? ")
    if Gaten == "ja":
        Duur = input("Is de kaas belachelijk duur? ")
        if Duur == "Ja":
            print("Emmenthaler")
        elif Duur == "nee":
            print("Leerdammer")
    elif Gaten == "nee":
        Hard = input("Is de kaas zo hard als steen?")
        if Hard == "ja":
            print("Parmigiano Reggiano")
        elif Hard == "nee":
            print("Goudse Kaas")
elif Geel == "nee":
    schimmel = input("Heeft de kaas blauwe schimmel")
    if schimmel == "ja":
        Korst = input("Heeft de kaas korst")
        if Korst == "ja":
            print("Blue de Rochbaron")
        elif Korst == "nee":
            print("Froume d'ambert")
    elif schimmel == "nee":
        Korst = input("Heeft de kaas korst")
        if Korst == "ja":
            print("Camembert")
        elif Korst == "nee":
            print("Mozzarella")
