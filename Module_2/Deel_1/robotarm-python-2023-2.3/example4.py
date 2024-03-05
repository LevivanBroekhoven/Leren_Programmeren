from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    for y in range(2):
        robotArm.moveRight()
    robotArm.drop()
    if x < 4:
        for z in range (2):
            robotArm.moveLeft()

for x in range(4):
    robotArm.grab()
    for a in range(1):
        robotArm.moveLeft()
    robotArm.drop()
    for b in range (1):
        robotArm.moveRight()

robotArm.grab()
for v in range(1):
    robotArm.moveLeft()
    robotArm.drop()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()