import pygame

pygame.font.init()

width = 550
height = 500
fontColor = "green"

#Aligns text in the center of window
def centerText(text, textHeight):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText

def settingScene(window, scene):
    #Title
    settingSceneTxt = window.setFont(80).render("Settings", True, fontColor)

    #Render texts
    scene.blit(settingSceneTxt, centerText(settingSceneTxt,3.5))