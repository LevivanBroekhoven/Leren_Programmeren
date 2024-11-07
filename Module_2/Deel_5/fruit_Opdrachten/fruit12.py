from fruitmand import *

lijst = sorted(fruitmand, key = lambda x: len(x["name"]))
lijst.reverse()

langste = lijst[0]


kleurenvertaal ={
    "orange": "oranje",
    "red"   : "rood",
    "green" : "groen",
    "brown" : "bruin",
    "yellow": "geel",
    "purple": "paars",
    "pink"  : "roze"}

print(f'De {langste["name"]} ({len(langste["name"])} letters) heeft een {kleurenvertaal[langste["color"]]} kleur en weegt {langste["weight"]/1000} kg' )
