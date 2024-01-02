import pygame # install in terminal with: pip install pygame
from SpriteSheet import SpriteSheet
import os
import sys
import random

# RobotArm class ################################################
#
#   An object of this class...
#
#   lets you load and display a yard with stacks of colored boxes
#   you can load a predefined level at the creation
#   lets you program the movement of boxes and scan their colors
#   lets you inspect the yard for debugging purposes
#
#   supported colors are: white, green, red, blue and yellow
#
# ######## methods for public use:
#   moveRight()
#     moves the robotarm one stack position to the right
#     returns True if succeeded, returns False if not possible
#
#   moveLeft()
#     moves the robotarm one stack position to the left
#     returns True if succeeded, returns False if not possible
#
#   grab()
#     lets the robotarm grab a box from the stack if there is one
#     returns True if succeeded, returns False if not possible
#
#   drop()
#     lets the robotarm drop its box to the stack if not full
#     returns True if succeeded, returns False if not possible
#
#   scan()
#      returns the color of the box at the robotarm
#
#   wait(operator)
#       waits for the the program window to be closed
#       operator is an optional function with a parameter: events {list of events}
#       the operator must/can handle each event in events
#
#   operate()
#       make the robotarm operate on keyboard-keys: LEFT, RIGHT and DOWN
#
# ######## creating and loading levels ########
#
#   loadLevel(levelName)
#     loads a predefined level for levelName {string}
#     returns True if succeeded, returns False if failed
#
#   loadMyLevel(yard, levelName)
#     loads a self made yard with a self made levelName {string}
#     where yard is a list of stacks each stack is a list of colors
#       box colors example of a yard: [['red','green'],['red','blue'],[],['green']]
#     returns True if succeeded, returns False if errors found, but sanitized
#
#   randomLevel(stacks, layers)
#     loads a simple random level with stacks and layers
#
#   loadRandomLevel(requirements )
#     loads a random level with optional requirements
#       requirements dictionary can contain key-values:
#         maxStacks {int}:  number of random stacks to provide
#         minBoxes {int}: minmum number of boxes provided per stack
#         maxBoxes {int}: maximum number of boxes provided per stack
#         maxColors {int}: maximum number of colors provided in the yard
#         requiredColors {list of string}: list of required colors
#         levelName {string}: name of the level
#
#   inspectYard()
#     prints the yard data, for inspection during debugging
#
# ###########################################################

class RobotArm:
  version = 2.3
# 2.1: incluses warnings for actions like hitting the borders
# 2.2: includes flaw terminal warnings for pointless actions
# 2.3: may grab once without warning from empty stack that was randomly sized

  _colors = [
    {"name": 'white', 'code': (255,255,255)},
    {"name": 'red', 'code': (255,0,0)},
    {"name": 'green', 'code': (0,150,0)},
    {"name": 'blue', 'code': (0,0,255)},
    {"name": 'yellow', 'code': (255,255,0)}
  ]
  _defaultlevels = [
    {'name': 'exercise 1', 'yard' : [[],["red"]]},
    {'name': 'exercise 2', 'yard' : [["blue"],[],[],[],["blue"],[],[],["blue"]]},
    {'name': 'exercise 3', 'yard' : [["white","white","white","white"]]},
    {'name': 'exercise 4', 'yard' : [["blue","white", "green","red","white"]]},
    {'name': 'exercise 6', 'yard' : [[],["red","white","red","white","red","white"]]},
    {'name': 'exercise 5', 'yard' : [["red"],["blue"],["white"],["green"],["green"],["blue"],["red"],["white"]]},

    {'name': 'exercise 7', 'yard' : [[],["blue","blue","blue","blue","blue","blue"], [],["blue","blue","blue","blue","blue","blue"], [],["blue","blue","blue","blue","blue","blue"], [],["blue","blue","blue","blue","blue","blue"],[],["blue","blue","blue","blue","blue","blue"]]},
    {'name': 'exercise 8', 'yard' : [[],["red","red","red","red","red","red","red"]]},
    {'name': 'exercise 9', 'yard' : [["blue"],["green", "green"],["white","white","white"],["red","red","red","red"]]},
    {'name': 'exercise 10', 'yard' : [["green"],["blue"],["white"],["red"],["blue"]]},
    {'name': 'exercise 11', 'yard' : {'maxStacks': 9, 'minBoxes': 1, 'maxBoxes': 1, 'requiredColors': ['white'], 'maxColors': 4}},
    {'name': 'exercise 12', 'yard' : {'maxStacks': 9, 'minBoxes': 1, 'maxBoxes': 1, 'requiredColors': ['red'], 'maxColors': 4}},
    {'name': 'exercise 13', 'yard' : [["green"],["green"],["green"],["blue"],["white"],["green"],["red"],["red"],["blue"],["green"]]},
    {'name': 'exercise 14', 'yard' : [[],["green"],["white"],["green","white"],["red","white"],["white","white"],["blue"],["blue","blue","blue"],["blue", "green", "green"],["red"]]},
    {'name': 'exercise 15', 'yard' : [[],["blue"],[],["blue"],["white"],[],["red"],["green"],["red"],["green"]]},
    {'name': 'soorten', 'yard' : {'maxStacks': 6, 'minBoxes': 1, 'maxBoxes': 1, 'requiredColors': ['red','green','blue'], 'maxColors': 3, 'endStacks':[[],['red'],['green'],['blue']]}},
    {'name': 'democratie', 'yard' : {'maxStacks': 9, 'minBoxes': 1, 'maxBoxes': 1, 'requiredColors': ['red','green','blue'], 'maxColors': 3, 'startStacks':[[]]}},
    ]
  _speeds = [{'fps': 100,'step': 1},{'fps': 150,'step': 2},{'fps': 250,'step': 4},{'fps': 400,'step': 5},{'fps': 500,'step': 10},{'fps': 500,'step': 20}]
  EMPTY = ''
  _backgroundColor = (200,200,200)
  _penColor = (0,0,0)
  _maxStacks = 10
  _maxLayers = 7
  _boxHeight = 29
  _boxWidth = 29
  _penWidth = 1
  _boxMargin = 2
  _armTopHeight = 15
  _bottomMargin = 2
  _idleAnimationTime = 300
  _screenMargin = 3
  _eventSleepTime = 300
  _eventActiveCycles = 100
  _steps = 0
  _iconImage = 'robotarm.ico'
  _hazardSprite = 'caution-icon-hi.png'
  _hazardFont = 'FreeSansBold.ttf'
  _previousAction = ''
  _actionFlaws = [
    ['left','right'],
    ['right','left'],
    ['drop','grap'],
    ['grab','drop'],
    ['scan','scan'],
    ['drop','scan'],
  ]
  reportFlaws = False
  _knownEmpty = []

  def __init__(self, levelName = ''):
    self._color = self.EMPTY
    self._stack = 0
    self._yardBottom = self._armTopHeight + (self._maxLayers + 1) * self._boxSpaceHeight() + self._penWidth
    self._armHeight = self._armTopHeight
    self._armX = 0
    self.speed = 1
    self._yard = []

    pygame.init()
    self._clock = pygame.time.Clock()

    self._screenWidth = self._stackX(self._maxStacks) + self._screenMargin
    self._screenHeight = self._layerY(-1) + self._bottomMargin + 2 * self._screenMargin
    self._screen = pygame.display.set_mode((self._screenWidth, self._screenHeight))

    assetsDir = os.path.dirname(os.path.realpath(__file__)) + '/'    # force assets to be found in directory of robotarm.py
    try:
      programIcon = pygame.image.load(assetsDir + self._iconImage)
      pygame.display.set_icon(programIcon)
      self._testImage = programIcon
    except:
      print(f' ********* icon image: {self._iconImage} not found *********')

    try:
      ss = SpriteSheet(assetsDir + self._hazardSprite)
      self._hazardSign = ss.load_strip((0,0,64,64), 4, self._backgroundColor)
    except:
      print(f' ********* hazard sprite: {self._hazardSprite} not found *********')
      exit()

    try:
      self._font = pygame.font.Font(assetsDir + self._hazardFont, 24)
    except:
      print(f' ********* font: {self._hazardFont} not found *********')
      exit()

    # Load level at creation
    if levelName != '':
      self.loadLevel(levelName)

########### ANIMATION METHODS ###########

  def _getColorCode(self, name):
    for c in self._colors:
      if c['name'] == name:
        return c['code']
    return False

  def _checkSpeed(self):
    speedInvalid = False
    if type(self.speed) is not int:
      speedInvalid = True
    if not (self.speed in range(len(self._speeds))):
      speedInvalid = True
    if speedInvalid:
      self.speed = 0 # reset speed to zero
      print('speed must be an integer between 0 and ' + str(len(self._speeds)-1))

  def _drawBoxAtPosition(self, x, y, color):
    pygame.draw.rect(self._screen, color, (x, y, self._boxWidth, self._boxHeight))
    pygame.draw.rect(self._screen, self._penColor, (x, y, self._boxWidth, self._boxHeight), self._penWidth)

  def _boxSpaceWidth(self):
    return (self._boxWidth + 2 * self._boxMargin) + self._penWidth

  def _stackX(self, stack):
    return self._screenMargin + self._boxMargin + stack * self._boxSpaceWidth() + self._penWidth

  def _boxSpaceHeight(self):
    return (self._boxHeight - self._penWidth)

  def _layerY(self,layer):
    return self._yardBottom - (layer + 1) * self._boxSpaceHeight() - self._screenMargin

  def _drawBox(self, stack, layer):
    x = self._stackX(stack) 
    y = self._layerY(layer)
    color = self._getColorCode(self._yard[stack][layer])
    self._drawBoxAtPosition(x,y,color)

  def _drawStack(self, stack):
    for l in range(len(self._yard[stack])):
      self._drawBox(stack,l)
    x = self._stackX(stack) - self._boxMargin - self._penWidth
    y = self._layerY(-1) + self._bottomMargin

    pygame.draw.lines(self._screen, self._penColor, False, [(x, y - 5), (x, y), (x + self._boxSpaceWidth(), y), (x + self._boxSpaceWidth(), y - 5)])

  def _drawArm(self):
    xm = self._armX + int(self._boxSpaceWidth()/2) - self._boxMargin
    pygame.draw.line(self._screen, self._penColor, (xm, 2), (xm, self._armHeight - 2))
    pygame.draw.lines(self._screen, self._penColor, False, [
      (self._armX - self._boxMargin,                  self._armHeight + 2), 
      (self._armX - self._boxMargin,                  self._armHeight - 2),
      (self._armX + self._boxWidth + self._penWidth,  self._armHeight - 2),
      (self._armX + self._boxWidth + self._penWidth , self._armHeight + 2)])
    if self._color > '':
      self._drawBoxAtPosition(self._armX,self._armHeight,self._getColorCode(self._color))

  def _drawState(self):
    steps = ' ['+ str(self._steps)+']' if self._steps > 0 else ''
    pygame.display.set_caption('Robotarm: ' + self._levelName + steps)
    self._screen.fill(self._backgroundColor)
    for c in range(len(self._yard)):
      self._drawStack(c)
    self._drawArm()

  def _message(self, message = 'problem!', gravity = 1):
    xm = self._armX + int(self._boxSpaceWidth()/2) - self._boxMargin - 31
    ym = 0

    text = self._font.render(message, True, (200,50,50), self._backgroundColor)
    for l in range(12):
      self._drawState()
      if gravity == 1: self._screen.blit(self._hazardSign[l % 4],(xm,ym))
      if l%2 == 0 or l >= 6:
        self._screen.blit(text, ((self._screenWidth//2) - text.get_rect().width//2,60))
      pygame.display.update()
      pygame.time.delay(100)

    self._drawState()
    pygame.display.update()

  def _animateHazard(self, message = 'problem!'):
    self._message(message, 1)

  def _animateFlaw(self, message = 'inefficiency!'):
    self._message(message, 0)

  def _animate(self, *args):
    self._checkSpeed()
    self._armX = self._stackX(self._stack)

    if (args[0] == 'down'):
      self._armHeight = self._armTopHeight
      targetLayer = len(self._yard[self._stack])
      if self._color == '':
        targetLayer -= 1
      targetHeight = self._layerY(targetLayer)
    elif (args[0] == 'left'):
      targetX = self._stackX(self._stack - 1)
    elif (args[0] == 'right'):
      targetX = self._stackX(self._stack + 1)

    ready = False
    while not ready:
      if (args[0] == 'idle'):
        ready = True
      elif (args[0] == 'down'):
        ready = self._armHeight == targetHeight
      elif (args[0] == 'up'):
        ready = self._armHeight == self._armTopHeight
      elif (args[0] == 'left') or (args[0] == 'right'):
        ready = self._armX == targetX

      for event in pygame.event.get():
        self.checkCloseEvent(event)

      self._drawState()
      pygame.display.update()

      self._clock.tick(self._speeds[self.speed]['fps'])

      if (args[0] == 'down'):
        self._armHeight += self._speeds[self.speed]['step']
        if self._armHeight > targetHeight:
          self._armHeight = targetHeight
      elif (args[0] == 'up'):
        self._armHeight -= self._speeds[self.speed]['step']
        if self._armHeight < self._armTopHeight:
          self._armHeight = self._armTopHeight
      elif (args[0] == 'left'):
        self._armX -= self._speeds[self.speed]['step']
        if self._armX < targetX:
          self._armX = targetX
      elif (args[0] == 'right'):
        self._armX += self._speeds[self.speed]['step']
        if self._armX > targetX:
          self._armX = targetX
      elif (args[0] == 'idle'):
        pygame.time.delay(self._idleAnimationTime)

  def _efficiencyCheck(self, action):
    for flaw in self._actionFlaws:
      # print(f'checking flaws for {self._previousAction} and {action}')
      # print(f'against flaws for {flaw[0]} and {flaw[1]}')
      if (self._previousAction == flaw[0] and action == flaw[1]):
        flawText = f'{flaw[1]} after {flaw[0]}? why?'
        print(f'action flaw: {flawText}' )
        if self.reportFlaws: self._animateFlaw(flawText)
    self._previousAction = action

  ########### ROBOTARM MANIPULATION ###########
  def moveRight(self):
    self._steps += 1
    self._efficiencyCheck('right')
    success = False
    if self._stack < self._maxStacks - 1:
      self._animate('right')
      self._stack += 1
      success = True
    else:
      self._animateHazard('hit right border!')
    return success

  def moveLeft(self):
    self._steps += 1
    self._efficiencyCheck('left')
    success = False
    if self._stack > 0:
      self._animate('left')
      self._stack -= 1
      success = True
    else:
      self._animateHazard('hit left border!')
    return success

  def grab(self):
    self._steps += 1
    self._efficiencyCheck('grab')
    success = False
    if self._color == self.EMPTY:
      self._animate('down')
      if len(self._yard[self._stack]) > 0:
        self._color = self._yard[self._stack][-1]
        self._yard[self._stack].pop(-1)
        success = True
      else:
        if self._knownEmpty[self._stack]:
          self._animateHazard('nothing to grab!')
        else:
          self._knownEmpty[self._stack] = True
      self._animate('up')
    else:
      self._animateHazard('robot arm occupied!')
    return success

  def drop(self):
    self._steps += 1
    self._efficiencyCheck('drop')
    success = False
    if self._color != self.EMPTY:
      if len(self._yard[self._stack]) < self._maxLayers:
        self._animate('down')
        self._yard[self._stack].append(self._color)
        self._color = self.EMPTY
        self._animate('up')
        success = True
      else:
        self._animateHazard('stack full!')
    else:
      self._animateHazard('no box to drop!')
    return success

  def scan(self):
    self._steps += 1
    self._efficiencyCheck('scan')
    return self._color

########### LEVEL & YARD lOADING & CREATION ###########

  def _checkYard(self,yard):
    success = True
    if type(yard) is not list:
      yard = []
      success = False
    for s in range(len(yard)):
      if type(yard[s]) is not list:
        yard[s] = []
        success = False
      for c in range(len(yard[s])):
        if self._getColorCode(yard[s][c]) == False:
          yard[s][c] = 'white'
          success = False
    return {'yard' : yard, 'success' : success}

  def loadMyLevel(self, yard, levelName = 'unknown level'):
    self._steps = 0
    result = self._checkYard(yard)
    self._yard = result['yard'] # sanitized yard
    success = result['success'] # where there errors?
    while len(self._yard) < self._maxStacks:
      self._yard.append([])
    self._levelName = levelName
    self._animate('idle')

    return success

  def loadLevel(self, levelName):
    success = False
    for level in self._defaultlevels:
      if levelName == level['name']:
        if type(level['yard']) is dict:
          level['yard']['levelName'] = levelName
          self.loadRandomLevel(level['yard'])
        else:
          self.loadMyLevel(level['yard'], levelName)
          self._knownEmpty = [True for stack in range(self._maxStacks)]
        success = True
    if not success:
      self.loadMyLevel([])
    return success

  def _requiredColorsFound(self, yard, requiredColors):
    colors = []
    for stack in yard:
      for color in stack:
        colors.append(color)
    for color in requiredColors:
      if colors.count(color) == 0:
        return False
    return True

  def _createRandomYard(self, maxStacks, minBoxes, maxBoxes, colors, maxColors, requiredColors, startStacks, endStacks):
    yard = [] + startStacks
    while len(yard) == 0 or not self._requiredColorsFound(yard, requiredColors):
      yard = [] + startStacks
      for l in range(maxStacks):
        random.seed()
        stack = []
        height = random.randint(minBoxes, maxBoxes)
        for b in range(height):
          color = colors[random.randint(0,len(colors)-1)]
          stack.append(color)
        yard.append(stack)
    for stack in endStacks:
      if len(yard) < 10:
        yard.append(stack)
    return yard

  def _randomColors(self, requiredColors, maxColors):
    colors = []
    for color in requiredColors:
      if not color in colors:
        colors.append(color)
    while len(colors) < maxColors:
      color = self._colors[random.randint(0,len(self._colors)-1)]['name']
      if not color in colors:
        colors.append(color)
    return colors

  def loadRandomLevel(self, requirements = {}):
    maxStacks = requirements['maxStacks'] if 'maxStacks' in requirements else 6
    maxStacks = self._maxStacks if maxStacks > self._maxStacks else maxStacks
    minBoxes = requirements['minBoxes'] if 'minBoxes' in requirements else 1
    maxBoxes = requirements['maxBoxes'] if 'maxBoxes' in requirements else 3
    maxBoxes = self._maxLayers if maxBoxes > self._maxLayers else maxBoxes
    requiredColors = requirements['requiredColors'] if 'requiredColors' in requirements else []
    levelName = requirements['levelName'] if 'levelName' in requirements else 'random level'
    maxColors = requirements['maxColors'] if 'maxColors' in requirements else 4
    startStacks = requirements['startStacks'] if 'startStacks' in requirements else []
    endStacks = requirements['endStacks'] if 'endStacks' in requirements else []

    colors = self._randomColors(requiredColors, maxColors)
    myYard = self._createRandomYard(maxStacks, minBoxes, maxBoxes, colors, maxColors, requiredColors, startStacks, endStacks)
    self.loadMyLevel(myYard, levelName)
    self._knownEmpty = [True for stack in range(self._maxStacks)]
    if minBoxes != maxBoxes:
      for stack in range(len(startStacks), len(startStacks) + maxStacks):
        self._knownEmpty[stack] = False

  def randomLevel(self, stacks, layers):
    self.loadRandomLevel({'maxStacks': stacks, 'maxBoxes': layers})

  def inspectYard(self):
    print(self._yard)

########### EVENT HANDLING ###########

  def checkCloseEvent(self,event):
    if event.type == pygame.QUIT:
      sys.exit()

  def _defaultHandler(self, events):
    for event in events:
      self.checkCloseEvent(event)

  def wait(self, handler = False):
    cycle = 0
    while True:
      events = pygame.event.get()               # get latest events
      if callable(handler):
        handler(events)
      self._defaultHandler(events)
      if len(events) > 0:                       # events happened?
        cycle = 0                               # stay awake and alert

      cycle += 1                                # prepare for sleep

      if cycle > self._eventActiveCycles:       # after 30 cycles
        pygame.time.delay(self._eventSleepTime) # go asleep for 300 milliseconds, give the processor some rest
        cycle = 0                               # wake up for events during sleep

  def _operator(self, instructions):
    for instruction in instructions:
      if instruction.type == pygame.KEYDOWN:
          if instruction.key == pygame.K_LEFT:
            self.moveLeft()
          if instruction.key == pygame.K_RIGHT:
            self.moveRight()
          if instruction.key == pygame.K_DOWN:
            if self.scan() == '':
              self.grab()
            else:
              self.drop()

  def operate(self):
    self.wait(self._operator)

if __name__ == "__main__":
  print('tested module RobotArm')
