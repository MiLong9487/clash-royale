import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_list):
        pygame.sprite.Sprite.__init__(self)
        self.COST = 0
        self.DEFAULT_HP = 0
        self.DEFAULT_ATK = 0
        self.ATK_RANGE = 0
        self.DEFAULT_SEPPD = 0
        self.hp = self.DEFAULT_HP
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_list = enemy_list
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.float_x = x
        self.float_y = y
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        if len(self.atking_enemy) == 1:
            self.atk_enemy(self.atking_enemy.sprite)
            return
        enemy = self.find_enemy()
        if ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5 <= self.ATK_RANGE:
            self.atk_enemy(enemy)
            self.atking_enemy.add(enemy)
        else:
            self.move(enemy)

    def find_enemy(self):
        min_distance = 1e5
        nearest_enemy = None
        for enemy in self.enemy_list:
            distance = ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5
            if distance < min_distance:
                nearest_enemy = enemy
                min_distance = distance
        return nearest_enemy

    def move(self, enemy):
        dir = pygame.math.Vector2(enemy.rect.centerx - self.rect.centerx, enemy.rect.centery - self.rect.centery).normalize()
        self.float_x += dir[0] * self.speed
        self.float_y += dir[1] * self.speed
        self.rect.centerx

    def atk_enemy(self, enemy):
        enemy.hp -= self.atk
        if enemy.hp == 0:
            enemy.kill()