import pygame
from display import display
from mainMenu import *
from settings import *

width = 550
height = 500

window = display(width, height, "Snake")
initDisplay = window.setDisplay()

SCENE_ONE = mainScene(initDisplay)
SCENE_TWO = settingScene(initDisplay)

SCENE_ONE
window.render()