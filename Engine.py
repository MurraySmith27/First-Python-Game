import pygame
from Characters.Player import Player
from Characters.RedSquare import RedSquare


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
    rs2 = RedSquare(150, 300, 50, 50)

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

        boy.move(key_pressed, obj=[RS, rs2])
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 800, 600))
        RS.display(window)
        boy.display(window)
        rs2.display(window)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
    quit()
