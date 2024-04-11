# tijd = 0
# x = "AM"
# y = "PM"

# while tijd < 24:
#     tijd += 1
#     if tijd <= 12:
#         if tijd == 12:
#             x = "PM"  
#         print(f"{tijd} {x}")
#     else:
#         if tijd == 24:
#             y = "AM"  
#         print(f"{tijd - 12} {y}")
 
tijd = 0

while tijd < 24:
    tijd += 1
    if tijd <= 11:
        print(f"{tijd} AM")
    elif tijd == 12:
        print(f"{tijd } PM")
    
    elif tijd <24:
        print(f"{tijd - 12} PM")
    else:
        print(f"{tijd - 12} AM")
