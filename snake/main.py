import sys
import pygame
from display import display
from mainMenu import *
from settings import *

width = 550
height = 500

isRunning = True

window = display(width, height, "Snake")
initDisplay = window.display()

#SCENES
SCENE_ONE = lambda : mainScene(initDisplay)
SCENE_TWO = lambda: settingScene(initDisplay)

while isRunning:

    pygame.init()
    for event in pygame.event.get():

        #EVENTS
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        

        SCENE_ONE()
        pygame.display.flip()
