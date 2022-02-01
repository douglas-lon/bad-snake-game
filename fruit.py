import pygame

class Fruit:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, surface):
        
        pygame.draw.rect(surface, 'purple', self.rect)