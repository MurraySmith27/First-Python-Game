import pygame
from typing import List, Dict

from pygame.rect import Rect

from GameObjects import GameObject, Watergun

G = 20


class _Character(GameObject):
    _speed: float

    def __init__(self, speed: float, x: int = 0, y: int = 0):
        """add health attribute here"""
        super().__init__(x, y, 60, 80)
        self._speed = speed

    def move(self, keys_pressed):
        raise NotImplementedError

    def display(self, window):
        raise NotImplementedError

    def hit_by_bullet(self):
        raise NotImplementedError


class Player(_Character):
    _image_index: int
    _speed: float
    _v0: float
    _y0: float
    _xprev: float
    _yprev: float
    _standing_on: GameObject
    watergun: Watergun

    def __init__(self, speed: float, x: int = 0, y: int = 0):
        super().__init__(speed, x, y)
        self._image = pygame.image.load("assets/boy_stand_right.png")
        self._image_index = self._image.convert_alpha()
        self._v0 = 100
        self._y0 = y
        self._yprev = y
        self._t = self._v0 / (2 * 0.5 * G)
        self.watergun = Watergun(self._x + self._image.get_rect().w, (self._y + self._image.get_rect().w) // 2, 10, 10)
        self._standing_on = None
        self._xprev = self._x

    def display(self, game_display):
        """ Displays the player onto the game display
        """
        game_display.blit(self._image_index, (self._x, self._y))
        self.watergun.display(game_display)

    def move(self, keys_pressed: Dict[int, bool], gravity: bool = True, obj: List[GameObject] = []):

        # movement along the x axis
        x_inc = 0
        if keys_pressed[pygame.K_LEFT]:
            '''change the self.direction for bullet implementation'''
            x_inc += -self._speed
        if keys_pressed[pygame.K_RIGHT]:
            '''change the self.direction for bullet implementation'''
            x_inc += self._speed
        # movement along the y axis, with gravity
        if keys_pressed[pygame.K_UP] and self._t == 0:
            self._t = 1
            self._y0 = self._y

        # update the position of the player according to change in position
        self._xprev = self._x
        self._x += x_inc
        self._yprev = self._y
        self._y = self._gravity()

        if self._t != 0:
            self._t += 1

        # collision
        for i in obj:
            hitbox = i.hitbox()
            if self.collides(hitbox):

                x_prev_between = self._xprev + self._width > hitbox[0] and self._xprev < hitbox[0] + hitbox[2]
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
                elif self._xprev + self._width <= hitbox[0]:
                    self._x = hitbox[0] - self._width
                elif self._xprev >= hitbox[0] + hitbox[2]:
                    self._x = hitbox[0] + hitbox[2]

            elif self._movement_overshoot(hitbox):
                '''
                If i + i._width is between prev position of the player and current position of the 
                player 
                '''
                pass

            # to check if player falls of the game object it was standing on
            elif self._standing_on is i and not self.x_collides(hitbox) and self._t == 0:
                self._t = self._v0 / G
                self._y0 = 2 * self._y - self._gravity()
                self._standing_on = None

        self.watergun.move(self._x + 60, self._y + 40)
        self.watergun.update(obj)

    def _movement_overshoot(self, obj_hitbox: List[int]) -> bool:

        return self._movement_overshoot_x(obj_hitbox) or self._movement_overshoot_y(obj_hitbox)

    def _movement_overshoot_x(self, obj_hitbox: List[int]) -> bool:
        x_collides = self._xprev + self._width < obj_hitbox[0] and obj_hitbox[0] + obj_hitbox[2] < self._x
        x_collides = x_collides or self._xprev > obj_hitbox[0] + obj_hitbox[2] and self._x < obj_hitbox[0]
        return x_collides

    def _movement_overshoot_y(self, obj_hitbox: List[int]) -> bool:
        y_collides = self._yprev + self._height < obj_hitbox[1] and obj_hitbox[1] + obj_hitbox[3] < self._y
        y_collides = y_collides or self._yprev > obj_hitbox[1] + obj_hitbox[3] and self._y < obj_hitbox[3]
        return y_collides

    def _gravity(self, t: float = -1):
        """calculates the new position of the player after <t> units has passed
        """
        if t == -1:
            t = self._t
        return int(self._y0 - self._v0 * t + 0.5 * G * t * t)

    def hit_by_bullet(self):
        """
        Decrease the health of the player
        """
        pass
