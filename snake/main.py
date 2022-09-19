import pygame
from display import display
from mainMenu import *
from settings import *

width = 550
height = 500

window = display(width, height, "Snake")
menuScene = window.setDisplay()

mainScene(window, menuScene)
#settingScene(window,menuScene)
window.render()