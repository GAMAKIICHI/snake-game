import pygame

class display:
    def __init__(self, width:int, height:int, title:str):
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

        while self.isRender:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRender = False

# Example - 
# display(500,550, "Test").render()
