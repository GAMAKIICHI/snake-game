import pygame
from display import display

pygame.font.init()

fontColor = "green"

def settingScene(window, scene):
    #Title
    settingSceneTxt = window.setFont(80).render("Settings", True, fontColor)

    #Render texts
    scene.blit(settingSceneTxt, display.centerText(settingSceneTxt,3.5))
