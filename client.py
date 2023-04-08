import pygame
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
        self.choosed = False
    def choose(self):
        if not self.choosed:
            for button in button_group:
                if button.choosed:
                    button.choosed = False
                    button.rect.centery += 10
            self.choosed = True
            self.rect.centery -= 10
        else:
            self.choosed = False
            self.rect.centery += 10


button_group = pygame.sprite.Group()
button1 = Button(54,54,27,507)
button2 = Button(54,54,81,507)
button3 = Button(54,54,135,507)
button4 = Button(54,54,189,507)
button5 = Button(54,54,243,507)
button_group.add(button1,button2,button3,button4,button5)
image1 = pygame.image.load("knife.jpg")
image2 = pygame.image.load("musketeer.jpg")
image3 = pygame.image.load("pika.jpg")
image4 = pygame.image.load("princess.jpg")

while running:
    for event in pygame.event.get():
        position = None
        if event.type == pygame.QUIT:
            running = False
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_posy > 480 and mouse_posy < 534:
                    if mouse_posx > 54 and mouse_posx < 108:
                        button2.choose()
                    elif mouse_posx > 108 and mouse_posx < 162:
                        button3.choose()
                    elif mouse_posx > 162 and mouse_posx < 216:
                        button4.choose()
                    elif mouse_posx > 216 and mouse_posx < 270:
                        button5.choose()
                else:
                    for button in button_group:
                        if button.choosed:
                            button.choosed = False
                            button.rect.centery += 10
                            position = (mouse_posx, mouse_posy)
                            
    pygame.display.flip()
    screen.fill((0,0,0))
    button_group.draw(screen)
    screen.blit(image1,(button2.rect))
    screen.blit(image2,(button3.rect))
    screen.blit(image3,(button4.rect))
    screen.blit(image4,(button5.rect))

    
    
