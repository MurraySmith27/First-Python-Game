from typing import List
from GameObject import GameObject


class Character(GameObject):
    _speed: float

    def __init__(self, speed: float, x: int = 0, y: int = 0):
        super().__init__(x, y, 60, 80)
        self._speed = speed

    def collides(self, obj: List[int]):
        x, y, w, h = obj
        x_collides = self._x + self._width > x and self._x < x + w
        y_collides = self._y + self._height > y and self._y < y + h
        return x_collides and y_collides

    def x_collides(self, obj: List[int]):
        x, y, w, h = obj
        x_collides = self._x + self._width > x and self._x < x + w
        return x_collides

    def move(self, keys_pressed):
        raise NotImplementedError

    def display(self, window):
        raise NotImplementedError

    def hitbox(self) -> List[int]:
        return [self._x, self._y, self._width, self._height]
