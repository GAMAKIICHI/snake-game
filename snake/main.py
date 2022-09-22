import pygame
from display import display
from mainMenu import *
from settings import *

width = 550
height = 500

window = display(width, height, "Snake")
initDisplay = window.display()

SCENE_ONE = mainScene(initDisplay)
SCENE_TWO = settingScene(initDisplay)

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
