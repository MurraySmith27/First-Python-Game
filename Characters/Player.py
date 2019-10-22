from Character import Character
from typing import Dict, List
import pygame
from GameObject import GameObject

G = 20


class Player(Character):
    _image_index: int
    _v0: float
    _t: float
    _y0: float
    _yprev: float
    _standing_on: GameObject

    def __init__(self, speed: float, x: int = 0, y: int = 0):
        super().__init__(speed, x, y)
        self._image_index = pygame.image.load("images/boy_stand_right.png").convert_alpha()
        self._v0 = 100
        self._y0 = y
        self._yprev = y
        self._t = self._v0 / (2 * 0.5 * G)
        self._standing_on = None

    def display(self, game_display):
        """ Displays the player onto the game display
        """
        game_display.blit(self._image_index, (self._x, self._y))

    def move(self, keys_pressed: Dict[int, bool], gravity: bool = True, obj: List[GameObject] = []):

        # movement along the x axis
        x_inc = 0
        if keys_pressed[pygame.K_LEFT]:
            x_inc += -self._speed
        if keys_pressed[pygame.K_RIGHT]:
            x_inc += self._speed
        # movement along the y axis, with gravity
        if keys_pressed[pygame.K_UP] and self._t == 0:
            self._t = 1
            self._y0 = self._y

        # update the position of the player according to change in position
        x_prev = self._x
        self._x += x_inc
        self._yprev = self._y
        self._y = self._gravity()

        if self._t != 0:
            self._t += 1

        # collision
        for i in obj:
            hitbox = i.hitbox()
            if self.collides(hitbox):

                x_prev_between = x_prev + self._width > hitbox[0] and x_prev < hitbox[0] + hitbox[2]
                case_b = self._y + self._height > hitbox[1] >= self._yprev + self._height
                case_c = self._y < hitbox[1] + hitbox[3] <= self._yprev

                # landing
                if x_prev_between and case_b:
                    self._y = hitbox[1] - self._height
                    self._y0 = self._y
                    self._t = 0
                    self._standing_on = i

                # player colliding with the bottom of the game object
                elif x_prev_between and case_c:
                    self._y = hitbox[1] + hitbox[3]
                    self._t += (2 * (self._v0 / G) - self._t)

                # collision by the sides
                elif x_prev + self._width <= hitbox[0]:
                    self._x = hitbox[0] - self._width
                elif x_prev >= hitbox[0] + hitbox[2]:
                    self._x = hitbox[0] + hitbox[2]

            # to check if player falls of the game object it was standing on
            elif self._standing_on is i and not self.x_collides(hitbox) and self._t == 0:
                self._t = self._v0 / G
                self._y0 = 2 * self._y - self._gravity()
                self._standing_on = None

    def _gravity(self, t: float = -1):
        """calculates the new position of the player after <t> units has passed
        """
        if t == -1:
            t = self._t
        return int(self._y0 - self._v0 * t + 0.5 * G * t * t)
