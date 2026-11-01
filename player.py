import pygame
class Player:
    def __init__(self):
        self.x = 40
        self.y = 350
        self.system = 0 #this here is system ID

    def render(self, screen):
        pygame.draw.polygon(screen, (8, 18, 74), [(self.x, self.y),(self.x - 20, self.y - 20),(self.x + 20, self.y - 20)]) 
