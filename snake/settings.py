import pygame
from display import setFont, centerText

pygame.font.init()


width = 550
height = 500
fontColor = "green"

def settingScene(window, scene):
    #Title
    settingSceneTxt = setFont(80).render("Settings", True, fontColor)

    #Render texts
    scene.blit(settingSceneTxt, centerText(settingSceneTxt,3.5, width, height))
