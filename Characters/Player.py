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

    def __init__(self, speed: float, x: int = 0, y: int = 0):
        super().__init__(speed, x, y)
        self._image_index = pygame.image.load(
            "images/boy_stand_right.png").convert_alpha()
        self._v0 = 70
        self._y0 = y
        self._yprev = y
        self._t = self._v0 / (2 * 0.5 * G)

    def display(self, game_display):
        """ Displays the player onto the game display
        """
        game_display.blit(self._image_index, (self._x, self._y))

    def move(self, keys_pressed: Dict[int, bool], gravity: bool = True, obj: List[GameObject] = []):

        x_inc = 0
        if keys_pressed[pygame.K_LEFT]:
            x_inc += -self._speed
        if keys_pressed[pygame.K_RIGHT]:
            x_inc += self._speed
        if keys_pressed[pygame.K_UP] and self._t == 0:
            self._t = .5
            self._y0 = self._y

        self._x += x_inc
        self._yprev = self._y
        self._y = int(self._y0 - self._v0 * self._t + 0.5 * G * self._t * self._t)

        if self._t != 0:
            self._t += .5

        for i in obj:
            hitbox = i.hitbox()

            if keys_pressed[pygame.K_RIGHT] and self.collides(hitbox):
                self._x = self._width - hitbox[0]
            elif keys_pressed[pygame.K_LEFT] and self.collides(hitbox):
                self._x = hitbox[0]

            if self.collides(hitbox) and not( hitbox[1] < self._yprev + self._height and self._yprev > hitbox[1] + hitbox[3]):
                if self._y > self._yprev and self._yprev < hitbox[1]:
                    self._y = hitbox[1] - self._height
                    self._y0 = self._y
                    self._t = 0
                elif self._y < self._yprev and self._yprev > hitbox[1]:
                    self._y = hitbox[1] + hitbox[3]
                    self._t += (2 * (self._v0 / G) - self._t)

