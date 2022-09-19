import pygame
from display import display

pygame.font.init()

width = 550
height = 500

window = display(width, height, "Snake")
menuScene = window.setDisplay()

text = window.setFont().render("Snake", True, "green")

menuScene.blit(text,(50,50))
window.render()



