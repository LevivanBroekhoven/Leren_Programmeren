from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
#pakt 4 blokken en beweegt ze 2x naar rechts en droped ze daar
for x in range(4):  
    robotArm.grab()
    for y in range(2):
        robotArm.moveRight()
    robotArm.drop()    
    if x < 4:
        for z in range (2):
            robotArm.moveLeft()
# pak blok beweeg naar rechts en drop blok
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()

# stapel op regel 3 naar regel 2 verplaatsen
for x in range(4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    if x < 3:
        robotArm.moveRight()

    



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()