import pygame
from GameObject import GameObject
from typing import List


class RedSquare(GameObject):

    _image_index: int
    _x: int
    _y: int
    _width: int
    _height: int

    def __init__(self, x: int = 0,  y: int = 0, w: int = 800,  h: int = 100):
        GameObject.__init__(self, x, y, w, h)

    def display(self, game_display):
        pygame.draw.rect(game_display,
                         (255, 0, 0, 255),
                         (self._x, self._y, self._width, self._height))

    def hitbox(self) -> List[int]:
        return [self._x, self._y, self._width, self._height]
