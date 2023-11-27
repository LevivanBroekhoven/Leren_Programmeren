def get_value(data: str, separator: str, position: int) -> str:
    values = data.split(separator)
    if position < len(values):
        return values[position]
    else:
        return "Position out of range"

resultaat = get_value("Muis,Kat,Hond,Rat,Hamster", ",", 0   )
print(resultaat)


    