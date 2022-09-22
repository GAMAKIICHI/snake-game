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

        btnTxt = createText(fontSize, text, textColor)
        btnPosition = centerText(btnTxt, buttonV, w, h)
        startBtn = pygame.draw.rect(self.scene, btnColor, (btnPosition))
        
        scene.blit(btnTxt, btnPosition)

        btnX = btnPosition[0]
        btnY = btnPosition[1]
        btnL = btnPosition[0] + btnPosition[2]
        btnW = btnPosition[1] + btnPosition[3]

        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()

            if btnX <= mouse[0] <= btnL and btnY <= mouse[1] <= btnW:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                print("Mouse is over a button")
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                print("Mouse is not on a button")



def createText(size, text, color):
    pygame.font.init()

    font = pygame.font.Font('snake/font/slkscr.ttf', size)
    text = font.render(text, True, color)
    return text

#Aligns text in the center of window
def centerText(text, textHeight, width, height):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText