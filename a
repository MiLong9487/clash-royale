import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode(screen_size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
class Button:
    def __init__(self,text,width,height,position):
        self.top_rect = pygame.rect(position,(width,height))
        self.top_color = (255,228,181)
