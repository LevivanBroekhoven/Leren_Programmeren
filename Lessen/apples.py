groen = 0
rijp = 1
rot = 2

apples =[groen,rijp,rijp,rot,groen,rot,rijp,rijp,rijp,rot,rijp,groen]
nogrijpen = []
print(apples)

for appel in apples:
    if appel == rot:
        apples.remove(appel)

for appel in apples:
    if appel == groen:
        apples.remove(appel)
        nogrijpen.append(appel)


print(apples)
print(nogrijpen)

