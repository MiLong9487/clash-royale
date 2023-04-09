import cards
import connect_server
import pygame
from constants import *

pygame.init()
clock = pygame.time.Clock()
team = []
connect = connect_server.UDPServer()
running = True

while len(team) != 2:
    msgs = connect.recv()
    for msg in msgs:
        if msg[0] == 'connect to server' and not msg[1] in team:
            team.append(msg[1])
connect.send('start', team[0])
connect.send('start', team[1])

blue_building_group = pygame.sprite.Group()
blue_ground_group = pygame.sprite.Group()
blue_air_group = pygame.sprite.Group()
red_building_group = pygame.sprite.Group()
red_ground_group = pygame.sprite.Group()
red_air_group = pygame.sprite.Group()

blue_king_tower = cards.KingTower((135, 435), red_ground_group, red_air_group)
blue_princess_tower_0 = cards.PrincessTower((53, 382), red_ground_group, red_air_group)
blue_princess_tower_1 = cards.PrincessTower((217, 382), red_ground_group, red_air_group)
red_king_tower = cards.KingTower((135, 45), blue_ground_group, blue_air_group)
red_princess_tower_0 = cards.PrincessTower((53, 98), blue_ground_group, blue_air_group)
red_princess_tower_1 = cards.PrincessTower((217, 98), blue_ground_group, blue_air_group)

blue_building_group.add(blue_king_tower, blue_princess_tower_0, blue_princess_tower_1)
red_building_group.add(red_king_tower, red_princess_tower_0, red_princess_tower_1)

while running:
    clock.tick(TPS)
    recvs = connect.recv()
    for recv in recvs:
        if recv['addr'] == team[0]:
            card = globals()[recv['info']['card']](recv['info']['pos'], red_ground_group, red_air_group, red_building_group)
        elif recv['addr'] == team[1]:
            card = globals()[recv['info']['card']](recv['info']['pos'], blue_ground_group, blue_air_group, blue_building_group)
        
    blue_building_group.update()
    blue_ground_group.update()
    blue_air_group.update()
    red_building_group.update()
    red_ground_group.update()
    red_air_group.update()

    if blue_king_tower.hp == 0:
        connect.send('lose', team[0])
        connect.send('win', team[1])
        running = False
    if red_king_tower.hp == 0:
        connect.send('win', team[0])
        connect.send('lose', team[1])
        running = False


    info_to_blue = []
    info_to_red = []
    for sprite in blue_building_group:
        info_to_blue.append([sprite.name, sprite.topleft, sprite.hp, 'self'])
        info_to_red.append([sprite.name, sprite.topleft, sprite.hp, 'enemy'])
    for sprite in blue_ground_group:
        info_to_blue.append([sprite.name, sprite.topleft, sprite.hp, 'self'])
        info_to_red.append([sprite.name, sprite.topleft, sprite.hp, 'enemy'])
    for sprite in blue_air_group:
        info_to_blue.append([sprite.name, sprite.topleft, sprite.hp, 'self'])
        info_to_red.append([sprite.name, sprite.topleft, sprite.hp, 'enemy'])
    for sprite in red_building_group:
        info_to_blue.append([sprite.name, sprite.topleft, sprite.hp, 'enemy'])
        info_to_red.append([sprite.name, sprite.topleft, sprite.hp, 'self'])
    for sprite in red_ground_group:
        info_to_blue.append([sprite.name, sprite.topleft, sprite.hp, 'enemy'])
        info_to_red.append([sprite.name, sprite.topleft, sprite.hp, 'self'])
    for sprite in red_air_group:
        info_to_blue.append([sprite.name, sprite.topleft, sprite.hp, 'enemy'])
        info_to_red.append([sprite.name, sprite.topleft, sprite.hp, 'self'])

    connect.send(info_to_blue, team[0])
    connect.send(info_to_red, team[1])