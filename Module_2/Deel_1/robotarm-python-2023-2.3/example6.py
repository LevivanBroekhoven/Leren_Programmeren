from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

for x in range(3):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if x < 2:
        for y in range(1):
            robotArm.moveLeft()
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()