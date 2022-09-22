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
        centerBtn = centerText(btnTxt, buttonV, w, h)
        startBtn = pygame.draw.rect(self.scene, btnColor, (centerBtn))
        
        scene.blit(btnTxt, centerBtn)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Button was clicked")
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                print("Not clicked")


def createText(size, text, color):
    pygame.font.init()

    font = pygame.font.Font('snake/font/slkscr.ttf', size)
    text = font.render(text, True, color)
    return text

#Aligns text in the center of window
def centerText(text, textHeight, width, height):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText