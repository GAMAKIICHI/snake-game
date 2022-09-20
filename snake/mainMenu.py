import pygame
from display import createText, centerText, button

width = 550
height = 500
fontColor = "green"

def mainScene(scene):

    #Vertical positioning for button
    titleVp = 3.5
    startVp = 2.5
    settingsVp = 2.1

    #title text
    titleTxt = createText(80, "Snake", fontColor)
    centerTitle = centerText(titleTxt, titleVp, width, height)

    #Button
    btn = button(scene)
    startBtn = btn.createButton(scene, "black", "Start", fontColor, 40, startVp, width, height)
    settingBtn = btn.createButton(scene, "black", "Setting", fontColor, 40, settingsVp, width, height)

    #Display text to window
    scene.blit(titleTxt, centerTitle)




