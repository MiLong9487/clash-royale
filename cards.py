import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, )
        self.COST = 0
        self.HP = 0
        self.ATK_RANGE = 0
        self.ATK = 0
        self.hp_now = self.HP
        self.atk_now = self.ATK
        self.atking_enemy = pygame.sprite.GroupSingle()

    def update(self):
        if len(self.atking_enemy) == 1:
            self.atk_enemy(self.atking_enemy.sprite)
            return
        enemy = self.find_enemy()
        if ((enemy.rect.x - self.rect.x) ** 2 + (enemy.rect.y - self.rect.y) ** 2) ** 0.5 <= self.ATK_RANGE:
            self.atk_enemy(enemy)
            return

    def find_enemy(self, enemy_list):
        ...

    def atk_enemy(self, enemy):
        enemy.hp_now -= self.atk_now
        if enemy.hp_now == 0:
            enemy.kill()