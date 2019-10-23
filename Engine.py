import pygame
from Characters.Player import Player
from Characters.RedSquare import RedSquare
from Watergun import Watergun

dead: bool
boy: Player
gun: Watergun
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ma boi")
    clock = pygame.time.Clock()

    boy = Player(20, 0, 0)
    RS = RedSquare(0, 500)
    rs2 = RedSquare(150, 300, 50, 50)
    boy_hitbox = boy.hitbox()
    gun = Watergun(int(boy_hitbox[0] + boy_hitbox[2] / 2), int(boy_hitbox[1] + boy_hitbox[3] / 2), 10, 5)

    key_pressed = {pygame.K_UP: False, pygame.K_DOWN: False,
                   pygame.K_RIGHT: False, pygame.K_LEFT: False}
    gun_fired = False

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
                gun_fired = True

                # bullet travels from Player to mouse position
                gun.calc_proj(boy, pygame.mouse.get_pos())

        boy.move(key_pressed, obj=[RS, rs2])
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
        gun.display(window, gun_fired)
        RS.display(window)
        boy.display(window)
        rs2.display(window)
        clock.tick(60)
        # clock.tick(120)
        pygame.display.flip()
    pygame.quit()
    quit()
