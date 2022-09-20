import pygame
from display import setFont, centerText, buttton
pygame.font.init()


width = 550
height = 500
fontColor = "green"

def button(scene, alignRect):
    startBtn = pygame.draw.rect(scene, "red", (alignRect))

def mainScene(scene):

    #Horizontal positioning for button
    titleHp = 3.5
    startHp = 2.5
    settingsHp = 2.1

    #Button text
    titleTxt = setFont(80).render("Snake", True, fontColor)
    startTxt = setFont(40).render("Start", True, fontColor)
    settingsTxt = setFont(40).render("Settings", True, fontColor)

    #Button alignment
    centerTitle = centerText(titleTxt, titleHp, width, height)
    centerStart = centerText(startTxt, startHp, width, height)
    centerSettings = centerText(settingsTxt, settingsHp, width, height)

    #Button
    btn = button(scene)
    btnColor = "red"
    titleBtn = btn.createButton(btnColor, centerTitle)
    startBtn = btn.createButton(btnColor, centerStart)
    settingBtn = btn.createButton(btnColor, centerSettings)

    #Display text to window
    scene.blit(titleTxt, centerTitle)
    scene.blit(startTxt, centerStart)
    scene.blit(settingsTxt, centerSettings)




