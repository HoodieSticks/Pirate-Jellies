import math ## We'll probably end up needing this eventually
import pygame

pygame.mixer.pre_init(22050, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

## ********** CONSTANTS ***************
white = pygame.Color('white')
black = pygame.Color('black')
red = pygame.Color('red')
blue = pygame.Color('blue')
green = pygame.Color('green')
yellow = pygame.Color('yellow')
## I recently found out those were built in, so might as well use them

winheight = 600
winlength = 800

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

## Game states - not in use, but will be eventually
PLAYING = 0
MAINMENU = 1
PAUSED = 2

## Sounds - these are just placeholders
boop = pygame.mixer.Sound('boop.wav') # I'm told wav files work better than mp3's
kaboom = pygame.mixer.Sound('kaboom.wav')

## Fonts - not in use, but probably will be eventually
font1 = pygame.font.SysFont('timesnewroman', 24)

## ************************************

win = pygame.display.set_mode((winlength, winheight)) # creates the window

pygame.display.set_caption('Captain WiFi') # sets the window caption


class player(object):
    def __init__(self, startingX, startingY):
        '''
        Player must be initialized with starting x and y coordinates.
        '''
        self.x = startingX
        self.y = startingY
        self.facing = NORTH
        self.speed = 3
        self.radius = 25
    
    def draw(self):
        '''
        Draws the player character
        '''
        pygame.draw.rect(win, green, (self.x - self.radius, self.y - self.radius, \
                                      self.radius*2, self.radius*2))
        if self.facing == NORTH:
            pygame.draw.line(win, black, (self.x, self.y), (self.x, self.y - self.radius), 2)
        elif self.facing == EAST:
            pygame.draw.line(win, black, (self.x, self.y), (self.x + self.radius, self.y), 2)
        elif self.facing == SOUTH:
            pygame.draw.line(win, black, (self.x, self.y), (self.x, self.y + self.radius), 2)
        elif self.facing == WEST:
            pygame.draw.line(win, black, (self.x, self.y), (self.x - self.radius, self.y), 2)
        else:
            print('Error: player is not facing a valid direction.')
            running = False
    
    def moveNorth(self):
        self.y -= self.speed
    
    def moveEast(self):
        self.x += self.speed
    
    def moveSouth(self):
        self.y += self.speed
    
    def moveWest(self):
        self.x -= self.speed
        
    def checkFacing(self):
        '''
        checks where the mouse is and updates the facing property
        '''
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        
        Xdist = abs(mouseX - self.x)
        Ydist = abs(mouseY - self.y)
        
        if Ydist >= Xdist and self.y >= mouseY:
            self.facing = NORTH
        elif Ydist >= Xdist:
            self.facing = SOUTH
        elif Ydist < Xdist and self.x <= mouseX:
            self.facing = EAST
        else:
            self.facing = WEST

## Main loop
captain = player(500, 500)

running = True
while running:
    pygame.time.delay(10) ## apparently this helps with inputs
    
    pygame.draw.rect(win, white, (0, 0, winlength, winheight)) # draws the background
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # what happens when X is pressed
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 32: # what happens when space is pressed
                ## idk maybe space can be a pause button
                print("Space doesn't do anything ya dingus")
                
        elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1): # left mouse button
            boop.play()
        
        elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3): # right mouse button
            kaboom.play()
     
    keys = pygame.key.get_pressed() # keys is a giant array of booleans
    if keys[pygame.K_w]:
        captain.moveNorth()
    if keys[pygame.K_d]:
        captain.moveEast()
    if keys[pygame.K_s]:
        captain.moveSouth()
    if keys[pygame.K_a]:
        captain.moveWest()
    ## Don't use elifs, or else diagonal mvmt won't be possible
    
    captain.checkFacing()
    captain.draw()
    
    pygame.display.update() # put this at the end of your main loop

pygame.quit() # put this at the end of all your pygame files