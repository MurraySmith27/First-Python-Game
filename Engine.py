import pygame
from GameObjects import RedSquare
from Characters import Player
from Map import MakeMap

dead: bool
boy: Player
move_boy: bool
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ma boi")
    clock = pygame.time.Clock()

    boy = Player(20, 100, 300)

    map_image, mapGOs = MakeMap("assets/maps/map1.csv", "assets/platformer-extendedtiles-0/PNG Grass/Spritesheet/sheet.png", 70, 7)
    # Process GO size. This needs to change.
    for i in range(len(mapGOs)):
        mapGOs[i]._x *= 800 / map_image.get_width()
        mapGOs[i]._y *= 600 / map_image.get_height()
        mapGOs[i]._width *= 800 / map_image.get_width()
        mapGOs[i]._height *= 600 / map_image.get_height()
    map_image = pygame.transform.scale(map_image, (800, 600))

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


        boy.move(key_pressed, obj=mapGOs)
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
        window.blit(map_image, (0, 0))
        boy.watergun.update()
        boy.display(window)


        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
    quit()
