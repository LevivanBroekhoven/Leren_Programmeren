from math import *
from test_lib import *


Bedrag1 = 76.61
Bedrag2 = 28.82
Bedrag3 = 2.23


def afrondenOpStuivers(Bedrag:float,):
    CENTEN = 5
    afronding = (round(Bedrag * 100 / CENTEN) * CENTEN /100)
    return round(afronding, 2)






excepted = round(76.60 ,2)
calculate = afrondenOpStuivers(Bedrag1 )
test ("Afronding 76.61", excepted , calculate)

excepted = round(28.80 ,2)   
calculate = afrondenOpStuivers(Bedrag2 )
test ("Afronding 28.82", excepted , calculate)

excepted = round(2.25 ,2)
calculate = afrondenOpStuivers(Bedrag3 )
test ("Afronding 2.23", excepted , calculate)


report()
