import pygame
from display import display

pygame.font.init()

width = 550
height = 500

window = display(width, height, "Snake")
menuScene = window.setDisplay()

def centerText(text, textHeight):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText

title = window.setFont().render("Snake", True, "green")

menuScene.blit(title,centerText(title,2.5))
window.render()



