import pygame

class button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('button.png')
        self.size = self.image.get_size()
        self.click_box = pygame.Rect((200,200), (self.size))
        self.surface = pygame.Surface(self.size)
    def render(self, background):
        self.surface.blit(self.image,(0,0))
        background.blit(self.surface,(self.x,self.y))
