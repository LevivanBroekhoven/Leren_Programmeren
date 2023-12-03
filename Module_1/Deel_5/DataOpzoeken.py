from test_lib import test,report


def get_value(data: str, separator: str, position: int) -> str:
    values = data.split(separator)
    if position < len(values):
        return values[position]
    else:
        return None



expected = "Kat"
calculated =  get_value("Muis,Kat,Hond,Rat,Hamster", ",", 1)
test('DataOpZoeken', expected, calculated)

expected = None
calculated =  get_value("Muis,Kat,Hond,Rat,Hamster", ",", 7)
test('DataOpZoeken2', expected, calculated)

report ()


    