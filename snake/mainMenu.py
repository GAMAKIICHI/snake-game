import pygame
from display import setFont, centerText
pygame.font.init()


width = 550
height = 500
fontColor = "green"

def button(scene, alignRect):
    startBtn = pygame.draw.rect(scene, "red", (alignRect))

def mainScene(window, scene):

    #Horizontal positioning for button
    titleHp = 3.5
    startHp = 2.5
    settingsHp = 2.1

    #Button text
    titleTxt = setFont(80).render("Snake", True, fontColor)
    startTxt = setFont(40).render("Start", True, fontColor)
    settingsTxt = setFont(40).render("Settings", True, fontColor)

    centerTitle = centerText(titleTxt, titleHp, width, height)
    centerStart = centerText(startTxt, startHp, width, height)
    centerSettings = centerText(settingsTxt, settingsHp, width, height)

    titleBtn = button(scene, centerTitle)
    startBtn = button(scene, centerStart)
    settingBtn = button(scene, centerSettings)

    #Display text to window
    scene.blit(titleTxt, centerTitle)
    scene.blit(startTxt, centerStart)
    scene.blit(settingsTxt, centerSettings)




