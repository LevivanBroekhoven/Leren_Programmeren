StartNum = 50
som = (f"{StartNum}")
optel = StartNum + 1
uitkomst = 50
nummer = 1

while uitkomst < 1000:
    uitkomst += optel
    som = f"{som} + {optel}"
    print(f"{nummer}. {som} = {uitkomst}")
    optel += 1
    nummer += 1

 