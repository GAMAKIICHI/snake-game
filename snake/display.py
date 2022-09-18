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
        self.display = pygame.display.set_mode((self.width, self.height))
    
    #Renders window
    def render(self):
        self.isRender = True
        self.setDisplay()

        #Required to close window
        while self.isRender:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRender = False
