import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode(screen_size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False