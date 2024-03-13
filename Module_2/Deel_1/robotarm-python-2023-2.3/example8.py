from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for v in range(7):
    
    for x in range (1):
        robotArm.grab()
        for y in range(8):
            robotArm.moveRight()
        for z in range(1):
            robotArm.drop()
        for c in range(8):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()