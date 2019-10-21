from typing import List


class GameObject:
    _x: int
    _y: int
    _width: int
    _height: int

    def __init__(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    def hitbox(self) -> List[int]:
        raise NotImplementedError

    # added getter and setter functions - Eric
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
