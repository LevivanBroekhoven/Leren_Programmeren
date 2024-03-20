from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
# beweeg 7x naar rechts
for x in range(7):
    robotArm.moveRight()

#pak 1 blok en beweeg naar rechts en drop
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

#Beweeg 7 blokken naar rechts
for x in range(7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()