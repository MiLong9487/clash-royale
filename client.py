import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
cardA = python.image.load()
class Button:
    def __init__(self,image,width,height,position):
        self.top_rect = pygame.rect(position,(width,height))
        self.top_color = (255,228,181)
    
    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(cardA,center=self.top_rect.center)