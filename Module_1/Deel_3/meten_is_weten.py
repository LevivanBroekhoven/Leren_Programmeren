a = input("voeg een getal toe ")
b = input("voeg een getal toe ")
a = a
b = b
if a > b:
    max = a
    min = b
    print(f" a is het grootste getal: {max}")
elif a < b:
    min = a
    max = b
    print(f"a is het kleinste getal: {min}")
else:
    a == b
    print("a en b zijn even groot")

print (f"Het minimum is {min}")
print (f"Het maximum is {max}")