from traceback import print_tb
import pygame

#This code creates and displays a window based on size given
# Example - 
# display(500,550, "Test").render()

class display:
    def __init__(self, width:int, height:int, title:str = "Title"):

        (self.width, self.height) = (width, height)
        self.title = title

        pygame.display.set_caption(title)

    #initialize a window to display
    def display(self):
        display = pygame.display.set_mode((self.width, self.height))
        
        return display

class button():
    def __init__(self, scene) -> None:
        self.scene = scene
    
    def createButton(self, scene, btnColor:str, text:str, textColor:str, fontSize:int, buttonV:int, w:int, h:int):

        isClicked = False

        btnTxt = createText(fontSize, text, textColor)
        btnPosition = centerText(btnTxt, buttonV, w, h)
        drawBtn = pygame.draw.rect(self.scene, btnColor, (btnPosition))
        
        scene.blit(btnTxt, btnPosition)

        btnX = btnPosition[0]
        btnY = btnPosition[1]
        btnW = btnPosition[0] + btnPosition[2]
        btnH = btnPosition[1] + btnPosition[3]

        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()

            print(f"Button: {text}")
            print(f"Button X: {btnX} Button Y: {btnY}")
            print(f"Width: {btnW} Height: {btnH}")
            print(f"MouseX: {mouse[0]} MouseY: {mouse[1]}\n")
            print("Mouse is not on a button")

            if btnX <= mouse[0] <= btnW and btnY <= mouse[1] <= btnH:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                print("Mouse is over a button")

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        return isClicked



def createText(size, text, color):
    pygame.font.init()

    font = pygame.font.Font('snake/font/slkscr.ttf', size)
    text = font.render(text, True, color)
    return text

#Aligns text in the center of window
def centerText(text, textHeight, width, height):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText