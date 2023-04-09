import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode([270,540])

images = {}
images['knight'] = pygame.image.load('./image/knight.jpg')
images['musketeer'] = pygame.image.load('./image/musketeer.jpg')
images['pika'] = pygame.image.load('./image/pika.jpg')
images['princess'] = pygame.image.load('./image/princess.jpg')

running = True

class Button(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,card=None):
        pygame.sprite.Sprite.__init__(self)
        self.card = card
        self.image = images[card]
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

def display(card, pos, hp, team):
    image = images[card]
    image.convert()
    image = pygame.transform.scale(image, (30,30))
    if team == 'enemy':
        image = pygame.transform.rotate(image, 180)
    screen.blit(image, pos)

button_group = pygame.sprite.Group()
button0 = Button(81,507,'knight')
button1 = Button(135,507,'musketeer')
button2 = Button(189,507,'pika')
button3 = Button(243,507,'princess')
button_group.add(button0,button1,button2,button3)



while running:
    for event in pygame.event.get():
        position = None
        if event.type == pygame.QUIT:
            running = False
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_posy > 480 and mouse_posy < 534:
                if mouse_posx > 54 and mouse_posx < 108:
                    button0.choose()
                elif mouse_posx > 108 and mouse_posx < 162:
                    button1.choose()
                elif mouse_posx > 162 and mouse_posx < 216:
                    button2.choose()
                elif mouse_posx > 216 and mouse_posx < 270:
                    button3.choose()
            else:
                for button in button_group:
                    if button.choosed:
                        button.choosed = False
                        button.rect.centery += 10
                        position = (mouse_posx, mouse_posy)

    pygame.display.flip()
    screen.fill((0,0,0))
    button_group.draw(screen)