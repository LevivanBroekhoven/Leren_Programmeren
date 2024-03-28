"""
    about : pyMatris is a pyGame matrix of n x m pixels
            This matrix is created to silumate Neopixel matrix boards
            for development in python so the code can be ported to micropython
            with these neopixel matrixes
    Version : 0.04
    Date    : 15 maart 2024
"""
import pygame
import pygame.sysfont as sysfont

"""
    Matrix with dymantions width, heigt to simulate a Neopixel display
    This version uses X, Y position, a neopixel matrix works with an index number.
"""
class pyMatrix():
    LINE_WIDTH 	  = 3    
    RESIZE_SCREEN_PERCENTAGE = 0.8
    """
        init function of the class
    """
    
    def __init__(self, width = 32, height = 16, colourBackground = (100, 100, 100), caption = 'Neopixel matrix', fpspeed = 60):        
        self._screen = pygame.display.set_mode()
        self.pixelsX, self.PixelsY = self._screen.get_size()
        self.pixelsX *= self.RESIZE_SCREEN_PERCENTAGE
        self.PixelsY *= self.RESIZE_SCREEN_PERCENTAGE
        #print(sysfont.get_fonts()[0])
        #self.font = pygame.font.SysFont(sysfont.get_fonts()[0], 25)
        self._oldPositions = set()
        self._maxX = width
        self._maxY = height
        self._fpspeed = fpspeed
        self._colourBackground = colourBackground
        self._squareSize       = min((self.pixelsX / self._maxX) - self.LINE_WIDTH * ((self.pixelsX + 1) / self.pixelsX)
                                    ,(self.PixelsY / self._maxY) - self.LINE_WIDTH * ((self.PixelsY + 1) / self.pixelsX)
                                    )
        self._resolution 	  = ((self._squareSize + self.LINE_WIDTH) * self._maxX
                                ,(self._squareSize + self.LINE_WIDTH) * self._maxY
                                )
        
        pygame.init()
        self._screen = pygame.display.set_mode(self._resolution)
        
        self._clock = pygame.time.Clock()  # to set max FPS
        pygame.display.set_caption(caption)
        self._drawScreen()
    
    """
        Return the NeoPixel index according to XY coordinates
    """
    def getIndex(self, posX, posY):
        if posX % 2 == 0:
            return posY + self._maxY * posX
        return self._maxY * (posX + 1) -1 - posY
    
    
    """
        Return the NeoPixel index according to XY coordinates
    """
    def getXY(self, index):
        x = index // self._maxY
        y = index % self._maxY
        if x % 2 == 1:
            y = self._maxY - y - 1
        return x, y
    
    def showNeoPixelIndex(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                x, y = self._getPixelPos(posX, posY)
                geometry = (x, y, self._squareSize, self._squareSize)
                index = self.getIndex(x,y)
                self._screen.blit(self.font.render(str(index), True, (255,255,255)), (200, 100))
                pygame.display.update()

    """
        return the width and height (in positions)  of the matrix
    """
    def getWidthHeight(self):
        return self._maxX, self._maxY
    
    """
        True if the PosX, posY is within the boundries of the matrix
    """
    def isPosAllowed(self, posX, posY):
        if posX < 0 or posY < 0:
            return False
        if posX >= self._maxX:
            return False
        if posY >= self._maxY:
            return False
        return True
    
    """
        update the matrix with a input matrix of rows, columns and color of the pixel
        R = (255,0,0)
        B = (  0,0,0)
        e.g. [ [R, B, B], [B, R, B], [B, B, R] ]
    """
    def showMatrix(self, matrix):
        self._oldPositions = set()
        w = len(matrix[0])
        h = len(matrix)
        region = None
        for y in range(h):
            for x in range(w):
                color = matrix[y][x]
                if color != 0:
                    self._oldPositions.add((x,y))
                    geometry = self._draw_square(x, y, color)
                    region = self._updateRegion(geometry, region)
                    
        geometry = self._convertRegion2Geometry(region)
        pygame.display.update(geometry)
            
    """
        clear the complete matrix
    """
    def clear(self):
        self.drawGame([], animate = True)
        
    """
        position is a list of (x, y, color)
        if color is None, the background color is reset.
        R = (255,  0,  0)
        B = (  0,  0,255)
        e.g. position = [ (1,1,R), (10,3,B) ]
    """
    def drawGame(self, positions : list, colour = None, animate = False):
        newCoordinates = set((p[0],p[1]) for p in positions )
        region = None
        # reset pixels that are no longer used
        for xy in self._oldPositions:
            if xy not in newCoordinates:
                geometry = self._draw_square(xy[0], xy[1], self._colourBackground)
                if animate:
                    pygame.display.update(geometry)
                else:
                    region = self._updateRegion(geometry, region)
                 
        for x,y,c in positions:
            if colour != None:
                c = colour
            geometry = self._draw_square(x, y, c)
            if animate:
                pygame.display.update(geometry)
            else:
                region = self._updateRegion(geometry, region)
                
        if animate == False:
            geometry = self._convertRegion2Geometry(region)
            pygame.display.update(geometry)
        self._oldPositions = newCoordinates
    
    """
        quit the matrix and the program
    """
    def quit(self):
        pygame.quit()
        quit()        
    
    """
        Get the raisen events
    """
    def getEvents(self):
        self._clock.tick(self._fpspeed)  # max FPS = 60
        return pygame.event.get()
    
    """
        return the keys pressedc (ascii value)
    """
    def getPressedKey(self):
        keys = []
        for event in self.getEvents():
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
        return keys
          
    """ ----------------------- Private functions ------------------------- """
    
    def _updateRegion(self, geometry, updateRegion):
        if updateRegion == None:
            updateRegion = [geometry[0], geometry[1], geometry[0] + geometry[2], geometry[1] + geometry[3]]
        else:
            updateRegion[0] = min(geometry[0], updateRegion[0])
            updateRegion[1] = min(geometry[1], updateRegion[1])
            updateRegion[2] = max(geometry[0] + geometry[2], updateRegion[2])
            updateRegion[3] = max(geometry[1] + geometry[3], updateRegion[3])
        return updateRegion
    
    def _convertRegion2Geometry(self, region):
        return (region[0], region[1], region[2] - region[0], region[3] - region[1])
    
    """
        from the postion posX, posY calculate and return the position in pixels.
    """
    def _getPixelPos(self, posX, posY):
        return self.LINE_WIDTH * (posX + 1) + self._squareSize * posX, self.LINE_WIDTH * (posY + 1) + self._squareSize * posY

    """
        Draw a square on the PosX, PosY location with a given colod
    """
    def _draw_square(self, posX, posY, colour = None):
        if colour == None:
            colour = self._colourBackground
        x, y = self._getPixelPos(posX, posY)
        geometry = (x, y, self._squareSize, self._squareSize)
        pygame.draw.rect(self._screen, colour, geometry)
        return geometry
    
    
    """
        Dwaw all the squares on the screen
    """
    def _draw_squares(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                self._draw_square(x, y)            
    

    """
        Redraw the complete screen
    """
    def _drawScreen(self):
        self._screen.fill((0, 0, 0))  # Fill screen with black color.
        self._draw_squares()
        pygame.display.flip()  # Update the screen.

        
if __name__ == "__main__":
    teller = 0
    import random
    COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
    COLOUR_RED        = (255,   0,   0)
    COLOUR_GREEN      = (  0, 255,   0)
    COLOUR_BLUE       = (  0,   0, 255)
    COLOUR_WHITE      = (255, 255, 255)
    COLOUR_BLACK      = (  0,   0,   0)
    COLOURS = (COLOUR_GREEN, COLOUR_WHITE, COLOUR_BLACK )

    def getRandomPos(maxX, maxY, notX = -1, notY = -1):
        x = random.randint(0,maxX-1)
        y = random.randint(0,maxY-1)
        if x == notX or y == notY:
            return getRandomPos(maxX, maxY, notX, notY)
        return x,y
    
    def change(keys: list, x,y, colour):
        if 27 in keys:	#esc
            game.quit()
        if ord("q") in keys:
            colour = random.choice(COLOURS)
        elif ord("s") in keys:
            x, y = ( 0,  1)
        elif ord("w") in keys:
            x, y = ( 0, -1)
        elif ord("a") in keys:
            x, y = (-1,  0)
        elif ord("d") in keys:
            x, y = ( 1,  0)
        return x, y, colour

    
    if True:  
        maxX, maxY  = (32,16)
        game = pyMatrix(maxX, maxY, colourBackground = COLOUR_BACKGROUND)        
        posX = maxX // 2
        posY = maxY // 2
        objectX, objectY = getRandomPos(maxX, maxY, posX, posY) 
        moveX, moveY = (1,0)
        colour = COLOUR_GREEN
        game.showNeoPixelIndex()
        speed = 10
        counter = 0
        snake = [(posX, posY)]
        while True:
            if colour == COLOUR_GREEN:
                speed = 10
            if colour == COLOUR_BLACK:
                speed = 5
            if colour == COLOUR_WHITE:
                speed = 20

            keys = game.getPressedKey()
            moveX, moveY, colour = change(keys, moveX, moveY, colour)

        
            if counter % speed == 0:
                new_head = (posX + moveX, posY + moveY)
                
                if new_head in snake:
                    game.quit()  
                else:
                    posX, posY = new_head
                    snake.insert(0, (posX, posY)) 
                    

                if objectX == posX and objectY == posY:
                    objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
                    teller += 1
                    print(teller)

                
                else:
                    snake.pop()

            positions = [(objectX, objectY, COLOUR_RED)]  
            positions.extend([(x, y, colour) for x, y in snake])  # Snake segments
            game.drawGame (positions )
            
            counter += 1
            