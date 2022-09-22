import pygame
from display import createText, centerText, button

def mainScene(scene):

    width = 550
    height = 500
    fontColor = "green"
    btnColor = "red"

    #Vertical positioning for button
    titleVp = 3.5
    startVp = 2.5
    settingsVp = 2.1

    #title text
    titleTxt = createText(80, "Snake", fontColor)
    centerTitle = centerText(titleTxt, titleVp, width, height)

    #Button
    btn = button(scene)
    startBtn = btn.createButton(scene, btnColor, "Start", fontColor, 40, startVp, width, height)
    settingBtn = btn.createButton(scene, btnColor, "Setting", fontColor, 40, settingsVp, width, height)

    #Display text to window
    scene.blit(titleTxt, centerTitle)




