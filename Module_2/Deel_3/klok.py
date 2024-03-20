tijd = 0
x = "AM"
y = "PM"

while tijd < 24:
    tijd += 1
    if tijd <= 12:
        if tijd == 12:
            x = "PM"  
        print(f"{tijd} {x}")
    else:
        if tijd == 24:
            y = "AM"  
        print(f"{tijd - 12} {y}")
