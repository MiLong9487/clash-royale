import pygame

SCREEN_SIZE = (360, 640)
BATTLEGROUND_SIZE = (270,480)
RIVER_Y = 240
BLOCK_LENGTH = 15
BRIDGE_X = (53, 217)
TPS = 20

class Mob(pygame.sprite.Sprite):
    #__init__為卡牌之參數，根據每張卡牌"完全"重構
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = ''
        self.TYPE = ''
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
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = 0
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.float_x = pos[0]
        self.float_y = pos[1]
        self.rect.center = pos

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
        min_distance = 1e3
        nearest_enemy = None
        for enemy_list in self.enemy_lists:
            if not enemy_list:continue
            for enemy in enemy_list:
                distance = ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5
                if distance < min_distance:
                    nearest_enemy = enemy
                    min_distance = distance
        return nearest_enemy
    
    #無視河流者須重構
    def find_road(self, enemy):
        if (self.rect.centery < RIVER_Y + BLOCK_LENGTH and enemy.rect.centery < RIVER_Y + BLOCK_LENGTH) or (self.rect.centery > RIVER_Y - BLOCK_LENGTH and enemy.rect.centery > RIVER_Y - BLOCK_LENGTH):
            return [enemy.rect.centerx, enemy.rect.centery]
        else:
            if abs(BRIDGE_X[0] - self.rect.centerx) < abs(BRIDGE_X[1] - self.rect.centerx):
                nearest_bridge = (BRIDGE_X[0], RIVER_Y)
            else:
                nearest_bridge = (BRIDGE_X[1], RIVER_Y)
            return nearest_bridge

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
            if enemy.hp < 0:
                enemy.hp == 0
                enemy.kill()
            self.left_cd = self.cd

#範例:騎士 無任何特殊之處，除參數(__init__)外無須重構
class Knight(Mob):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = 'knight'
        self.TYPE = 'ground'
        self.DEFAULT_HP = 1000
        self.DEFAULT_CD = int(TPS * 1.2)
        self.DEFAULT_ATK = 95
        self.DEFAULT_SEPPD = 1
        self.ATK_RANGE = 30
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.float_x = pos[0]
        self.float_y = pos[1]
        self.rect.center = pos

class Musketeer(Mob):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = 'musketeer'
        self.TYPE = 'ground'
        self.DEFAULT_HP = 650
        self.DEFAULT_CD = int(TPS * 1.0)
        self.DEFAULT_ATK = 145
        self.DEFAULT_SEPPD = 1.2
        self.ATK_RANGE = 120
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.float_x = pos[0]
        self.float_y = pos[1]
        self.rect.center = pos

class Princess(Mob):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = 'princess'
        self.TYPE = 'ground'
        self.DEFAULT_HP = 270
        self.DEFAULT_CD = int(TPS * 1.8)
        self.DEFAULT_ATK = 120
        self.DEFAULT_SEPPD = 0.8
        self.ATK_RANGE = 260
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.float_x = pos[0]
        self.float_y = pos[1]
        self.rect.center = pos

class Pika(Mob):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = 'pika'
        self.TYPE = 'ground'
        self.DEFAULT_HP = 720
        self.DEFAULT_CD = int(TPS * 1.5)
        self.DEFAULT_ATK = 250
        self.DEFAULT_SEPPD = 1.1
        self.ATK_RANGE = 30
        self.hp = self.DEFAULT_HP
        self.cd = self.DEFAULT_CD
        self.atk = self.DEFAULT_ATK
        self.speed = self.DEFAULT_SEPPD
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.left_cd = self.cd
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.float_x = pos[0]
        self.float_y = pos[1]
        self.rect.center = pos



class Building(pygame.sprite.Sprite):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = ''
        self.TYPE = 'building'
        self.ATK_RANGE = 0
        self.hp = 0
        self.DEFAULT_CD = 0
        self.atk = 0
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.cd = self.DEFAULT_CD
        self.left_cd = 0
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.rect.center = pos

    def update(self):
        if self.left_cd > 0:
            self.left_cd -= 1
        if len(self.atking_enemy) == 1:
            self.atk_enemy(self.atking_enemy.sprite)
            return
        enemy = self.find_enemy()
        if enemy:
            if ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5 <= self.ATK_RANGE:
                self.atk_enemy(enemy)
                self.atking_enemy.add(enemy)

    def find_enemy(self):
        min_distance = 1e3
        nearest_enemy = None
        for enemy_list in self.enemy_lists:
            if not enemy_list:continue
            for enemy in enemy_list:
                distance = ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5
                if distance < min_distance:
                    nearest_enemy = enemy
                    min_distance = distance
        return nearest_enemy

    def atk_enemy(self, enemy):
        if self.left_cd == 0:
            enemy.hp -= self.atk
            if enemy.hp < 0:
                enemy.hp == 0
            self.left_cd = self.cd
            if enemy.hp == 0:
                enemy.kill()

class KingTower(Building):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = 'king_tower'
        self.TYPE = 'building'
        self.ATK_RANGE = 0
        self.hp = 3000
        self.DEFAULT_CD = int(TPS * 1.0)
        self.atk = 0
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.cd = self.DEFAULT_CD
        self.left_cd = 0
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.rect.center = pos

class PrincessTower(Building):
    def __init__(self, pos, *enemy_lists):
        pygame.sprite.Sprite.__init__(self)
        self.NAME = 'princess_tower'
        self.TYPE = 'building'
        self.ATK_RANGE = 0
        self.hp = 2000
        self.DEFAULT_CD = int(TPS * 1.0)
        self.atk = 0
        self.enemy_lists = enemy_lists
        self.atking_enemy = pygame.sprite.GroupSingle()
        self.cd = self.DEFAULT_CD
        self.left_cd = 0
        self.surface = pygame.Surface((30,30))
        self.rect = self.surface.get_rect()
        self.rect.center = pos