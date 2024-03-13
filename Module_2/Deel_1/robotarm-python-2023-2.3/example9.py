from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for y in range(3):
    robotArm.moveRight()
for v in range(4):
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(5):
            robotArm.moveLeft()
robotArm.moveLeft()
for v in range(3):
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(5):
            robotArm.moveLeft()
robotArm.moveLeft()
for v in range(2):
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(5):
            robotArm.moveLeft()
robotArm.moveLeft()
for v in range(1):
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()