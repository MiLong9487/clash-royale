import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode([500,600])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
cardA = pygame.image.load()
class Button(pygame.sprite.Sprite):
    def __init__(self,color,width,height,position):
        pygame.sprite.Sprite.__init__(self)
        self.top_rect = pygame.rect(position,(width,height))
        self.top_color = (250,228,181)
    
    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(cardA,center=self.top_rect.center)