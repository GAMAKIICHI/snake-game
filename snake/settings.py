import pygame
from display import createText, centerText, button

pygame.font.init()

def settingScene(scene):

    width = 550
    height = 500
    fontColor = "green"
    btnColor = "black"

    #Vertical positioning for text/buttons
    titleVp = 3.5
    volumeVp = 2.5
    colorVp = 2.1
    backVp = 1.8

    #Title text
    settingTitle = createText(80, "Settings", fontColor)
    centerTitle = centerText(settingTitle, titleVp, width, height)

    volumeTxt = createText(40, "Volume", fontColor)
    centerVolume = centerText(volumeTxt, volumeVp, width, height)

    colorTxt = createText(40, "Color", fontColor)
    centerColor = centerText(colorTxt, colorVp, width, height)

    btn = button(scene)
    backBtn = btn.createButton(scene, btnColor, "Back", fontColor, 40, backVp, width, height)

    #Display text to window
    scene.blit(settingTitle, centerTitle)
    scene.blit(volumeTxt, centerVolume)
    scene.blit(colorTxt, centerColor)