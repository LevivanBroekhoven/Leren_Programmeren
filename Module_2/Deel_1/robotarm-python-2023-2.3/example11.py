from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for y in range (2):
    for x in range(3):
        robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()