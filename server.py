import cards
import connect_server
import pygame
import time

pygame.init()
clock = pygame.time.Clock()
team = []
connect = connect_server.UDPServer()
running = True

while len(team) != 2:
    msgs = connect.recv()
    if msgs:
        for msg in msgs:
            if msg['info'] == 'connect to server' and not msg['addr'] in team:
                team.append(msg['addr'])
connect.send('start', team[0])
connect.send('start', team[1])
ack_blue = False
ack_red = False
while not (ack_blue and ack_red):
    msgs = connect.recv()
    if msgs:
        for msg in msgs:
            if msg['info'] == 'ack':
                if msg['addr'] == team[0]:
                    ack_blue = True
                elif msg['addr'] == team[1]:
                    ack_red = True

blue_building_group = pygame.sprite.Group()
blue_ground_group = pygame.sprite.Group()
blue_air_group = pygame.sprite.Group()
red_building_group = pygame.sprite.Group()
red_ground_group = pygame.sprite.Group()
red_air_group = pygame.sprite.Group()

blue_king_tower = cards.KingTower((135, 435), red_ground_group, red_air_group)
blue_princess_tower_0 = cards.PrincessTower((60, 380), red_ground_group, red_air_group)
blue_princess_tower_1 = cards.PrincessTower((210, 380), red_ground_group, red_air_group)
red_king_tower = cards.KingTower((135, 45), blue_ground_group, blue_air_group)
red_princess_tower_0 = cards.PrincessTower((60, 100), blue_ground_group, blue_air_group)
red_princess_tower_1 = cards.PrincessTower((210, 100), blue_ground_group, blue_air_group)

blue_building_group.add(blue_king_tower, blue_princess_tower_0, blue_princess_tower_1)
red_building_group.add(red_king_tower, red_princess_tower_0, red_princess_tower_1)

while running:
    clock.tick(20)
    recvs = connect.recv()
    if recvs:
        for recv in recvs:
            card_name = recv['info']['card']
            pos = recv['info']['pos']
            if recv['addr'] == team[0]:
                card = getattr(cards,card_name.capitalize())(pos, red_ground_group, red_air_group, red_building_group)
                globals()['blue_{}_group'.format(card.TYPE)].add(card)
            elif recv['addr'] == team[1]:
                pos[0] = 270 - pos[0]
                pos[1] = 480 - pos[1]
                card = getattr(cards,card_name.capitalize())(recv['info']['pos'], blue_ground_group, blue_air_group, blue_building_group)
                globals()['red_{}_group'.format(card.TYPE)].add(card)
            
    blue_building_group.update()
    blue_ground_group.update()
    blue_air_group.update()
    red_building_group.update()
    red_ground_group.update()
    red_air_group.update()

    if blue_king_tower.hp == 0:
        connect.send('lose', team[0])
        connect.send('win', team[1])
        while connect.send_buffer:pass
        time.sleep(1)
        running = False
    if red_king_tower.hp == 0:
        connect.send('win', team[0])
        connect.send('lose', team[1])
        while connect.send_buffer:pass
        time.sleep(1)
        running = False


    info_to_blue = []
    info_to_red = []
    for sprite in blue_building_group:
        info_to_blue.append([sprite.NAME, sprite.rect.topleft, sprite.hp, 'self'])
        info_to_red.append([sprite.NAME, (270-sprite.rect.right,480-sprite.rect.bottom), sprite.hp, 'enemy'])
    for sprite in blue_ground_group:
        info_to_blue.append([sprite.NAME, sprite.rect.topleft, sprite.hp, 'self'])
        info_to_red.append([sprite.NAME, (270-sprite.rect.right,480-sprite.rect.bottom), sprite.hp, 'enemy'])
    for sprite in blue_air_group:
        info_to_blue.append([sprite.NAME, sprite.rect.topleft, sprite.hp, 'self'])
        info_to_red.append([sprite.NAME, (270-sprite.rect.right,480-sprite.rect.bottom), sprite.hp, 'enemy'])
    for sprite in red_building_group:
        info_to_blue.append([sprite.NAME, sprite.rect.topleft, sprite.hp, 'enemy'])
        info_to_red.append([sprite.NAME, (270-sprite.rect.right,480-sprite.rect.bottom), sprite.hp, 'self'])
    for sprite in red_ground_group:
        info_to_blue.append([sprite.NAME, sprite.rect.topleft, sprite.hp, 'enemy'])
        info_to_red.append([sprite.NAME, (270-sprite.rect.right,480-sprite.rect.bottom), sprite.hp, 'self'])
    for sprite in red_air_group:
        info_to_blue.append([sprite.NAME, sprite.rect.topleft, sprite.hp, 'enemy'])
        info_to_red.append([sprite.NAME, (270-sprite.rect.right,480-sprite.rect.bottom), sprite.hp, 'self'])

    connect.send(info_to_blue, team[0])
    connect.send(info_to_red, team[1])