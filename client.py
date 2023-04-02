import pygame,sys
from constants import *

pygame.init()
screen = pygame.display.set_mode([300,640])

running = True

class Button(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill((250,250,250))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

button_group = pygame.sprite.Group()
button = Button(50,50,100,100)
button_group.add(button)


moving = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
    
    if moving:
        if event.type == pygame.MOUSEMOTION:
            button.rect.center = pygame.mouse.get_pos()
    pygame.display.flip()
    screen.fill((0,0,0))
    button_group.draw(screen)
    
