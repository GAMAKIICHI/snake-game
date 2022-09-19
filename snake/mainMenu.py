import pygame
from display import display

pygame.font.init()

width = 550
height = 500
fontColor = "green"

window = display(width, height, "Snake")
menuScene = window.setDisplay()

def centerText(text, textHeight):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText

titleTxt = window.setFont(80).render("Snake", True, fontColor)
startBtn = window.setFont(48).render("Start", True, fontColor)
hiScoreBtn = window.setFont(48).render("Top Scores", True, fontColor)

menuScene.blit(titleTxt, centerText(titleTxt,2.5))
menuScene.blit(startBtn, centerText(startBtn, 1.8))
menuScene.blit(hiScoreBtn, centerText(hiScoreBtn, 1.5))
window.render()



