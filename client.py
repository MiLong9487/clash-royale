import pygame.sys
from constants import *

pygame.init()
screen = pygame.display.set_mode([500,600])

running = True




class Button(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect = [pos_x,pos_y]
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
button_group = pygame.sprite.Group()
button = Button(50,50,100,100,(250,250,250))
button_group.add(button)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    button_group.draw(screen)

