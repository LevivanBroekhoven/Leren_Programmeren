from fruitmand import *

lijst = sorted(fruitmand, key = lambda x: x["name"], reverse=True)

# lijst.reverse()

for x in lijst:
    print(f"{x['name']}, {x['weight']} gram")
