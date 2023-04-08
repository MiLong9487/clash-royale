import pygame
from constants import *

class Mob(pygame.sprite.Sprite):
    #__init__為卡牌之參數，根據每張卡牌"完全"重構
    def __init__(self, x, y, *enemy_list):
        pygame.sprite.Sprite.__init__(self)
        self.COST = 0
        self.DEFAULT_HP = 0
        self.DEFAULT_CD = 0
        self.DEFAULT_ATK = 0
        self.DEFAULT_SEPPD = 0
        self.ATK_RANGE = 0
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_list = enemy_list
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.float_x = x
        self.float_y = y
        self.rect.centerx = x
        self.rect.centery = y

    #有技能者須重構
    def update(self):
        if self.left_cd > 0:
            self.left_cd -= 1
        if len(self.atking_enemy) == 1:
            self.atk_enemy(self.atking_enemy.sprite)
            return
        enemy = self.find_enemy()
        if ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5 <= self.ATK_RANGE:
            self.atk_enemy(enemy)
            self.atking_enemy.add(enemy)
        else:
            pos = self.find_road(enemy)
            self.move(pos)

    #攻擊目標僅有敵方建築者須重構
    def find_enemy(self):
        min_distance = 1e5
        nearest_enemy = None
        for enemys in self.enemy_list:
            for enemy in enemys:
                distance = ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5
                if distance < min_distance:
                    nearest_enemy = enemy
                    min_distance = distance
        return nearest_enemy
    
    #無視河流者須重構
    def find_road(self, enemy):
        if (self.rect.centery < RIVER_Y - BLOCK_LENGTH and enemy.rect.centery < RIVER_Y) or (self.rect.centery > RIVER_Y and enemy.rect.centery > RIVER_Y):
            return [enemy.rect.centerx, enemy.rect.centery]
        else:
            return[min(abs(BRIDGE_X[0] - self.rect.centerx), abs(BRIDGE_X - self.rect.centerx)), RIVER_Y]

    def move(self, pos):
        dir = pygame.math.Vector2(pos[0] - self.rect.centerx, pos[1] - self.rect.centery).normalize()
        self.float_x += dir[0] * self.speed
        self.float_y += dir[1] * self.speed
        self.rect.centerx = int(self.float_x)
        self.rect.centery = int(self.float_y)

    #特殊攻擊方式者(如地獄飛龍)須重構
    def atk_enemy(self, enemy):
        if self.left_cd == 0:
            enemy.hp -= self.atk
            self.left_cd = self.cd
            if enemy.hp == 0:
                enemy.kill()

#範例:騎士 無任何特殊之處，除參數(__init__)外無須重構
class knight(Mob):
    def __init__(self, x, y, enemy_list):
        self.COST = 3
        self.DEFAULT_HP = 1000
        self.DEFAULT_CD = int(TICK * 1.2)
        self.DEFAULT_ATK = 95
        self.DEFAULT_SEPPD = 1
        self.ATK_RANGE = 30
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_list = enemy_list
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.float_x = x
        self.float_y = y
        self.rect.centerx = x
        self.rect.centery = y
class musketeer(Mob):
    def __init__(self, x, y, enemy_list):
        self.COST = 4
        self.DEFAULT_HP = 650
        self.DEFAULT_CD = int(TICK * 1.0)
        self.DEFAULT_ATK = 145
        self.DEFAULT_SEPPD = 1.2
        self.ATK_RANGE = 120
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_list = enemy_list
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.float_x = x
        self.float_y = y
        self.rect.centerx = x
        self.rect.centery = y
class princess(Mob):
    def __init__(self, x, y, enemy_list):
        self.COST = 3
        self.DEFAULT_HP = 270
        self.DEFAULT_CD = int(TICK * 1.8)
        self.DEFAULT_ATK = 120
        self.DEFAULT_SEPPD = 0.8
        self.ATK_RANGE = 260
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_list = enemy_list
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.float_x = x
        self.float_y = y
        self.rect.centerx = x
        self.rect.centery = y
class pika(Mob):
    def __init__(self, x, y, enemy_list):
        self.COST = 4
        self.DEFAULT_HP = 720
        self.DEFAULT_CD = int(TICK * 1.5)
        self.DEFAULT_ATK = 250
        self.DEFAULT_SEPPD = 1.1
        self.ATK_RANGE = 30
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_list = enemy_list
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.float_x = x
        self.float_y = y
        self.rect.centerx = x
        self.rect.centery = y