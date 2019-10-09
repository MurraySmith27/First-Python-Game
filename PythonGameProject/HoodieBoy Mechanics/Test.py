import pygame

pygame.init()

#initialize variables
x = 0
y = 0
run = True
moveright = False
moveleft = False
gd = pygame.display.set_mode([800, 600])
boy = pygame.image.load('boy_stand_right.png').convert_alpha()
clock = pygame.time.Clock()
gravity = 2
boy_hitbox = pygame.draw.rect(gd,[0,0,0],[x,y,boy.get_size()[0],boy.get_size()[1]])
floor = pygame.draw.rect(gd, [0,0,0], [0,500,800,100])

#did this need to be in the while loop?
clock.tick(60)

def moveboy():
    global x, y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 1
    elif keys[pygame.K_LEFT]:
        x -= 1

def detect_collision():
    global x, y

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    moveboy()
    boy_hitbox.move(x,y)
    pygame.draw.rect(gd, [0,0,0], [0,500,800,100])
    if not boy_hitbox.colliderect(floor):
        y += gravity
    gd.fill([255,255,255])
    gd.blit(boy, [x, y])
    pygame.display.update()
pygame.quit()
quit()