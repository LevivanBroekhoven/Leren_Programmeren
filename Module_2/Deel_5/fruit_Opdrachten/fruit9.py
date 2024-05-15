from fruitmand import *
index = 0

for x in fruitmand:
    if (x['name']) == "druif":
        fruitmand.pop(index)
    index += 1

for x in (fruitmand):
    print(x['color'])
