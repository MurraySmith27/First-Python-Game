import pygame

pygame.init()  # Function that initiates all imported pygame modules (basically makes pygame work)

# This is the game i'm making it will feature a little guy with a bowl cut and a bunch of hoodies that do different things lets go!

# defining x and y positioning values as well as velocity values for movement

x = 0
y = 0
xvel = 0
yvel = 0
xacc = 0
yacc = 2

# Function that creates a window or screen, return type: Surface

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('My Boy')

boy1 = pygame.image.load('TheBoyStandingRight.png').convert_alpha()

index = boy1


def render(image, x, y):
    gameDisplay.blit(image, (x, y))


# Creating a clock object that tracks time

clock = pygame.time.Clock()

dead = False  # have not died yet when the game starts

while not dead:

    # Checking every frame to see if pygame.QUIT == True. When it is true, dead = True and it exits the while loop, runnning pygame.quit() then quit(), closing the game.

    # pygame.event.get() is a never ending array of events, so for each one python spits out the text of that event, until dead=True

    # This for loop will be used for event listening for the whole program

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            dead = True
        print(event)
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                xacc = -1
                xvel = -1
                animatingLeft = True
            if event.key == pygame.K_RIGHT:
                xacc = 1
                xvel = 1
                animatingRight = True
            lastFacingRight = False
            lastFacingLeft = False
        # if event.key == pygame.K_UP:

        if event.type == pygame.KEYUP:

            animatingLeft = False
            animatingRight = False

            if event.key == pygame.K_RIGHT:
                if event.type == pygame.KEYDOWN and event.key != pygame.K_LEFT:
                    xacc = 0
                    xvel = 0
            if event.key == pygame.K_LEFT:
                if event.type == pygame.KEYDOWN and event.key != pygame.K_RIGHT:
                    xacc = 0
                    xvel = 0

    # telling the computer to stop the boy if his foot touches something red
    ybottomcorner = y + 80
    if gameDisplay.get_at((x, ybottomcorner)) == (255, 0, 0, 255):
        yacc = 0
        yvel = 0
    else:
        yacc = 2

    # acceleration and velocity operators
    xvel += xacc
    yvel += yacc
    x += xvel
    y += yvel

    # setting maximum speeds
    if xvel >= 10:
        xvel = 10
    if yvel >= 10:
        yvel = 10
    if xvel <= -10:
        xvel = -10
    if yvel <= -10:
        yvel = -10

    # making sure the boy can't leave the window (the boy is 57x78 pixels)
    if x <= 0:
        x = 0
    if y <= 0:
        y = 0
    if x >= 800 - 57:
        x = 800 - 57
    if y >= 600 - 79:
        y = 600 - 79

    # ------Render Here------
    # always render from back to front (background first)

    pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 800, 600))

    pygame.draw.rect(gameDisplay, (255, 0, 0, 255), (0, 500, 800, 100))

    render(index, x, y)

    # -----------------------

    pygame.display.flip()

    # setting the frame rate
    clock.tick(60)
pygame.quit()

quit()
