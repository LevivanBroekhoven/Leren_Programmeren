from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
Rechts = 1
Links = 1

# Jouw python instructies zet je vanaf hier:
robotArm.grab()

while robotArm.scan() !=(""):
    for x in range(Rechts):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(Links):
        robotArm.moveLeft()
    robotArm.grab()
    Rechts += 1
    Links += 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()