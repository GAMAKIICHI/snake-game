import pygame

#This code creates and displays a window based on size given
# Example - 
# display(500,550, "Test").render()

class display:
    def __init__(self, width:int, height:int, title:str = "Title"):
        pygame.init()

        (self.width, self.height) = (width, height)
        self.title = title

        pygame.display.set_caption(title)

    #initialize a window to display
    def setDisplay(self):
        display = pygame.display.set_mode((self.width, self.height))
        
        return display

    #Renders window
    def render(self):
        self.isRender = True

        #Required to close window
        while self.isRender:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRender = False

class button():
    def __init__(self, scene) -> None:
        self.scene = scene
    
    def createButton(self, scene, btnColor:str, text:str, textColor:str, fontSize:int, buttonV:int, w:int, h:int):

        btnTxt = createText(fontSize, text, textColor)
        centerBtn = centerText(btnTxt, buttonV, w, h)
        startBtn = pygame.draw.rect(self.scene, btnColor, (centerBtn))
        scene.blit(btnTxt, centerBtn)

        mouse = pygame.mouse.get_pos()
        while True:
            scene.blit(btnTxt, centerBtn)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Button was clicked")
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def createText(size, text, color):
    pygame.font.init()

    font = pygame.font.Font('snake/font/slkscr.ttf', size)
    text = font.render(text, True, color)
    return text

#Aligns text in the center of window
def centerText(text, textHeight, width, height):
    alignText = text.get_rect(center = (width/2,height/textHeight))
    return alignText