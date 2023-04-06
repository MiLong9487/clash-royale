import pygame
path = './image/'
images = {}
def load_images(card):
    images[card] = []
    for i in range(3):
        images[card].append(pygame.image.load(path+card+str(i)).convert)
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = ''
        if not self.name in images:
            load_images(self.name)
        self.image = images[self.name]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]