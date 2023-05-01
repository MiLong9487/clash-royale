import pygame
import connect_client

pygame.init()
screen = pygame.display.set_mode([270,540])
connect = connect_client.UDPClient()
clock = pygame.time.Clock()

images = {}
images['knight'] = pygame.image.load('./image/knight.jpg')
images['musketeer'] = pygame.image.load('./image/musketeer.jpg')
images['pika'] = pygame.image.load('./image/pika.jpg')
images['princess'] = pygame.image.load('./image/princess.jpg')
images['king_tower'] = pygame.image.load('./image/king_tower.jpg')
images['princess_tower'] = pygame.image.load('./image/princess_tower.jpg')

costs = {'knight':3,'musketeer':4,'pika':4,'princess':3}

running = True

class Button(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,card=None):
        pygame.sprite.Sprite.__init__(self)
        self.card = card
        self.image = images[card]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.choosed = False
    def choose(self):
        if not self.choosed:
            for button in button_group:
                if button.choosed:
                    button.choosed = False
                    button.rect.centery += 10
            self.choosed = True
            self.rect.centery -= 10
        else:
            self.choosed = False
            self.rect.centery += 10

def display(card, pos, hp, team):
    image = images[card]
    image.convert()
    image = pygame.transform.scale(image, (30,30))
    if team == 'enemy':
        image = pygame.transform.rotate(image, 180)
    screen.blit(image, pos)

font_name = pygame.font.match_font('arial')
def draw_text(text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text_surface, text_rect)

def end(text):
    while True:
        draw_text(text, 30, 135, 240)
        pygame.display.flip()
        screen.fill((0,0,0))
        button_group.draw(screen)

button_group = pygame.sprite.Group()
button0 = Button(81,507,'knight')
button1 = Button(135,507,'musketeer')
button2 = Button(189,507,'pika')
button3 = Button(243,507,'princess')
button_group.add(button0,button1,button2,button3)

water = 5

while True:
    draw_text('waiting for start', 30, 135, 240)
    recv = connect.recv()
    if type(recv) == str and recv == 'start':
        connect.send('ack')
        break

    pygame.display.flip()
    screen.fill((0,0,0))
    button_group.draw(screen)

while running:
    clock.tick(20)
    water += 0.018
    if water > 10:
        water = 10
    for event in pygame.event.get():
        position = None
        if event.type == pygame.QUIT:
            running = False
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_posy > 480 and mouse_posy < 534:
                if mouse_posx > 54 and mouse_posx < 108:
                    button0.choose()
                elif mouse_posx > 108 and mouse_posx < 162:
                    button1.choose()
                elif mouse_posx > 162 and mouse_posx < 216:
                    button2.choose()
                elif mouse_posx > 216 and mouse_posx < 270:
                    button3.choose()
            else:
                for button in button_group:
                    if button.choosed and water >= costs[button.card]:
                        water -= costs[button.card]
                        button.choosed = False
                        button.rect.centery += 10
                        info_to_server = {'card':button.card, 'pos':[mouse_posx,mouse_posy]}
                        connect.send(info_to_server)

    recv = connect.recv()
    if recv:
        if recv == 'win' or recv == 'lose':
            end(recv)
        for info in recv:
            display(*info)

    draw_text(str(int(water)), 10, 10, 530)

    pygame.display.flip()
    screen.fill((0,0,0))
    button_group.draw(screen)

pygame.quit()