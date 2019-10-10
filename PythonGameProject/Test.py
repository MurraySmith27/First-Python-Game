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
gravity = 10
#added 2 to the width since size is not a multiple of 10
boy_hitbox = pygame.draw.rect(gd,[0,0,0],[x,y,boy.get_size()[0],boy.get_size()[1]+2],1)
floor = pygame.draw.rect(gd, [0,0,0], [0,500,800,500])
jump = False
jumpcount = 10

#did this need to be in the while loop?
#clock.tick(30)

def moveboy():
    global x, y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
    elif keys[pygame.K_LEFT]:
        x -= 5

def fall():
    global y
    y += 10

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
    if jump:
        if not boy_hitbox.colliderect(floor):
            if jumpcount >= -10:
                y -= jumpcount * abs(jumpcount) * 0.5
                jumpcount -= 1
            else:
                jumpcount = 10
                jump = False
    gd.fill([255,255,255])
    moveboy()
    test = pygame.draw.rect(gd,[0,0,0],[x,y,boy.get_size()[0],boy.get_size()[1]+2],1)
    if not test.colliderect(floor):
        fall()
    boy_hitbox = pygame.draw.rect(gd,[0,0,0],[x,y,boy.get_size()[0],boy.get_size()[1]+2],1)
    pygame.draw.rect(gd, [0,0,0], [0,500,800,100])
    print(str(x) + ', ' + str(y))
    #print(boy_hitbox.get_size())
    #print(boy_hitbox.colliderect(floor))
    gd.blit(boy, [x, y])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()