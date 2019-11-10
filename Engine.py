import pygame
from Characters import Player
from Map import *
from Constants import *

dead: bool
boy: Player
move_boy: bool

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((FRAME_WIDTH, FRAME_HEIGHT))
    pygame.display.set_caption("ma boi")
    clock = pygame.time.Clock()

    boy = Player(BOY_SPEED, 100, 300)

    map_image, mapGOs = \
        MakeMap("assets/maps/map1.csv", "assets/platformer-extendedtiles-0/PNG Grass/Spritesheet/sheet.png", 70, 7)
    # Process GO size. This needs to change.
    for i in range(len(mapGOs)):
        mapGOs[i].scale((FRAME_WIDTH / map_image.get_width(),
                         FRAME_HEIGHT / map_image.get_height()))
    map_image = pygame.transform.scale(map_image, (FRAME_WIDTH, FRAME_HEIGHT))

    map_position = [0, 0]

    key_pressed = {pygame.K_UP: False, pygame.K_DOWN: False,
                   pygame.K_RIGHT: False, pygame.K_LEFT: False}

    dead = False
    while not dead:

        for event in pygame.event.get():
            # stop running when the window is closed
            if event.type == pygame.QUIT:
                dead = True
                break
            print(event)

            if event.type == pygame.KEYDOWN:
                key_pressed[int(event.key)] = True

            if event.type == pygame.KEYUP:
                key_pressed[int(event.key)] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                boy.watergun.fire()

            if event.type == pygame.MOUSEBUTTONUP:
                boy.watergun.fired = False
        boy_x_prev = boy._x
        boy.move(key_pressed, obj=mapGOs)
        boy_delta_x = boy._x - boy_x_prev
        bg = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        window.blit(bg, (0, 0))
        map_position = map_update(map_position, mapGOs, boy_delta_x)
        window.blit(map_image, map_position)
        boy.watergun.update()
        boy.display(window)
        clock.tick(FRAME_RATE)
        pygame.display.flip()
    pygame.quit()
    quit()
