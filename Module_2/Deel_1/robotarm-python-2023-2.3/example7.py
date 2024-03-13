from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for x in range(30):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    if x == 5 or x == 11 or x == 17 or x == 23:
        for y in range(2):
            robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()