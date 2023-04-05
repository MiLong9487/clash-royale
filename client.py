import pygame,sys
from constants import *

pygame.init()
screen = pygame.display.set_mode([270,540])

running = True

class Button(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill((250,250,250))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

button_group = pygame.sprite.Group()
button1 = Button(54,54,27,507)
button2 = Button(54,54,81,507)
button3 = Button(54,54,135,507)
button4 = Button(54,54,189,507)
button5 = Button(54,54,243,507)
button_group.add(button1,button2,button3,button4,button5)


moving = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
        if moving:
            if event.type == pygame.MOUSEMOTION:
                if mouse_posx > 54 and mouse_posx < 108 and mouse_posy > 480 and mouse_posy < 534:
                    button2.rect.center = pygame.mouse.get_pos()
                if mouse_posx > 108 and mouse_posx < 162 and mouse_posy > 480 and mouse_posy < 534:
                    button3.rect.center = pygame.mouse.get_pos()
                if mouse_posx > 162 and mouse_posx < 216 and mouse_posy > 480 and mouse_posy < 534:
                    button4.rect.center = pygame.mouse.get_pos()
                if mouse_posx > 216 and mouse_posx < 270 and mouse_posy > 480 and mouse_posy < 534:
                    button5.rect.center = pygame.mouse.get_pos()
    pygame.display.flip()
    screen.fill((0,0,0))
    button_group.draw(screen)
    
