import pygame,sys
from constants import *

pygame.init()
screen = pygame.display.set_mode([300,640])

running = True

class Button(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("")
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
    

button_group = pygame.sprite.Group()
button = Button(50,50,100,100)
button_group.add(button)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    button_group.draw(screen)
    

