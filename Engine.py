import pygame
from GameObjects import RedSquare
from Characters import Player

dead: bool
boy: Player
move_boy: bool
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ma boi")
    clock = pygame.time.Clock()

    boy = Player(20, 0, 0)
    RS = RedSquare(0, 500)
    rs2 = RedSquare(150, 300, 200, 50)
    rs3 = RedSquare(150, 100, 50, 200)

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

        boy.move(key_pressed, obj=[RS, rs2, rs3])
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
        RS.display(window)
        boy.display(window)
        rs2.display(window)
        rs3.display(window)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
    quit()
