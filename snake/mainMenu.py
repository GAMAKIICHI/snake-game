import pygame
from display import display
pygame.font.init()

fontColor = "green"

def button(scene, alignRect):
    startBtn = pygame.draw.rect(scene, "red", (alignRect))

def mainScene(window, scene):

    #Horizontal positioning for button
    titleHp = 3.5
    startHp = 2.5
    settingsHp = 2.1

    #Button text
    titleTxt = window.setFont(80).render("Snake", True, fontColor)
    startTxt = window.setFont(40).render("Start", True, fontColor)
    settingsTxt = window.setFont(40).render("Settings", True, fontColor)

    titleBtn = button(scene, display.centerText(titleTxt, 3.5))
    startBtn = button(scene, display.centerText(startTxt, 2.5))
    settingBtn = button(scene, display.centerText(settingsTxt, 2.1))

    #Render texts
    scene.blit(titleTxt, display.centerText(titleTxt,3.5))
    scene.blit(startTxt, display.centerText(startTxt, 2.5))
    scene.blit(settingsTxt, display.centerText(settingsTxt, 2.1))




