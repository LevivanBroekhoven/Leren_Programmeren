gastheer = False
gasten = False
drank = False
chips = True

if gasten and drank and chips == True:
    print('Start the Party')
elif gastheer or gasten and chips and drank == True:
    print("Start the Party")
elif gastheer and drank == True:
    print("Start the Party")
else:
    print('No Party')