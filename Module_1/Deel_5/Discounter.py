from test_lib import *
from math import *
from test_lib import test , report


month_discount_brands = "Vespa, Kymco, Yamama"
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    # return calculated discount based on price and brand
    if brand in month_discount_brands:
        Discount = price * MONTH_DISCOUNT_PERC / 100 
    else:
        Discount = 0
    return round(Discount ,2)
    

excepted = 10.00
calculate = calc_discount (100, "Vespa" , month_discount_brands)
test ("Vespa", excepted , calculate)


excepted = 20.00
calculate = calc_discount (200, "Yamama" , month_discount_brands)
test ("Yamama", excepted , calculate)

excepted = 30.00
calculate = calc_discount (300, "Kymco" , month_discount_brands)
test ("Kymco", excepted , calculate)

report()