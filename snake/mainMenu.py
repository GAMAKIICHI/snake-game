import pygame
from display import display

pygame.font.init()

width = 550
height = 500
fontColor = "green"

window = display(width, height, "Snake")
menuScene = window.setDisplay()

#Aligns text in the center of window
def centerText(text, textHeight):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText

def mainScene(window, scene):
    #Title
    titleTxt = window.setFont(80).render("Snake", True, fontColor)

    #Buttons
    startBtn = window.setFont(48).render("Start", True, fontColor)
    settingsBtn = window.setFont(48).render("Top Scores", True, fontColor)

    #Render texts
    scene.blit(titleTxt, centerText(titleTxt,2.5))
    scene.blit(startBtn, centerText(startBtn, 1.8))
    scene.blit(settingsBtn, centerText(settingsBtn, 1.5))

mainScene(window, menuScene)
window.render()



