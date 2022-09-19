from dis import dis
import pygame
from display import display

width = 550
height = 500

pygame.font.init()

window = display(width, height, "Snake")
menuScene = window.setDisplay()

font = pygame.font.Font('snake/font/slkscr.ttf', 80)
text = font.render("Snake", True, "green")
menuScene.blit(text,(0,0))


window.render()



