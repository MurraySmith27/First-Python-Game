import pygame
from Character import Character


class RedSquare(Character):

    _image_index: int
    _x: int
    _y: int
    _width: int = 800
    _height: int = 100
    def __init__(self, x: int = 0,  y: int = 0):

        self._x = x
        self._y = y

    def displayRS(self, game_display):
        pygame.draw.rect(game_display, (255, 0, 0, 255), (0, 500, 800, 100))

    def getX(self):
        x = self._x
        return x
    def getY(self):
        y = self._y
        return y
    def getWidth(self):
        Width = self._width
        return Width
    def getHeight(self):
        Height = self._height
        return Height