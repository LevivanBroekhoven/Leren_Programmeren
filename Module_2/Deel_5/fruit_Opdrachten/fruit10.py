from fruitmand import *

lijst = sorted(fruitmand, key = lambda x: x["weight"])

lijst.reverse()

for x in lijst:
    print(f"{x['name']}, {x['weight']} gram")
