from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
test = 1

# Jouw python instructies zet je vanaf hier:
robotArm.grab()

while robotArm.scan() !=(""):
    for x in range(test):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(test):
        robotArm.moveLeft()
    robotArm.grab()
    test += 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()