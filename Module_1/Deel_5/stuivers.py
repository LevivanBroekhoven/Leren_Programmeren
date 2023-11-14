from math import *
from test_lib import *

AANTAL_CENTEN = 5
Bedrag1 = 76.61
Bedrag2 = 28.82
Bedrag3 = 2.23


def afronden(Bedrag:float,):
    afronding = (round(Bedrag * 100 / 5) * 5 /100)
    return '{:.2f}' .format(round(afronding, 2))






excepted = '{:.2f}' .format(round(76.60 ,2))
calculate = afronden(Bedrag1 )
test ("Afronding", excepted , calculate)

excepted = '{:.2f}' .format(round(28.80 ,2))    
calculate = afronden(Bedrag2 )
test ("Afronding", excepted , calculate)

excepted = '{:.2f}' .format(round(2.25 ,2))
calculate = afronden(Bedrag3 )
test ("Afronding", excepted , calculate)


report()
