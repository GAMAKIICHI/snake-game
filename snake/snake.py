import pygame

class snake():
    def __init__(self, color, scene) -> None:
        self.color = color
        self.scene = scene
    
    def snakeHead(self):
        sHead = pygame.Rect(5,5,0,0)
        drawHead = pygame.draw.rect(self.scene, "green", sHead)
