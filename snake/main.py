import pygame
from display import display
from mainMenu import *

width = 550
height = 500

window = display(width, height, "Snake")
menuScene = window.setDisplay()

mainScene(window, menuScene)
window.render()