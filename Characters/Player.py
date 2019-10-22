from Character import Character
from typing import Dict
import pygame


class Player(Character):

    _image_index: int
    _speed: float
    _x: int
    _y: int
    _width: int = 60
    _height: int = 80

    def __init__(self, speed: float, x: int = 0,  y: int = 0):
        self._image_index = pygame.image.load("images/boy_stand_right.png").convert_alpha()

        self._speed = speed
        self._x = x
        self._y = y

    def displayPlayer(self, game_display):
        game_display.blit(self._image_index, (self._x, self._y))

    def move(self, keys_pressed: Dict[int, bool]):
        x_inc = 0
        y_inc = 0
        if keys_pressed[pygame.K_LEFT]:
            x_inc += -self._speed
        if keys_pressed[pygame.K_RIGHT]:
            x_inc += self._speed
        if keys_pressed[pygame.K_UP]:
            y_inc += - self._speed
        if keys_pressed[pygame.K_DOWN]:
            y_inc += self._speed

        self._x += x_inc
        self._y += y_inc

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
