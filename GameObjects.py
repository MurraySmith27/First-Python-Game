import pygame
from typing import List, Union, Tuple

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


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

    def collides(self, obj: List[int]):
        x, y, w, h = obj
        y_collides = self._y + self._height > y and self._y < y + h
        return self.x_collides(obj) and y_collides

    def x_collides(self, obj: List[int]):
        x, y, w, h = obj
        x_collides = self._x + self._width > x and self._x < x + w
        return x_collides

    def scale(self, scale: Union[float, Tuple[float, float]]) -> None:
        if isinstance(scale, float):
            self._x *= scale
            self._width *= scale
            self._y *= scale
            self._height *= scale
        else:
            self._x *= scale[0]
            self._width *= scale[0]
            self._y *= scale[1]
            self._height *= scale[1]

    def hitbox(self) -> List[int]:
        return [self._x, self._y, self._width, self._height]

    def display(self, game_display):
        raise NotImplementedError

    def hit_by_bullet(self):
        #Need to implement
        return


class RedSquare(GameObject):
    _image_index: int
    _x: int
    _y: int
    _width: int
    _height: int

    def __init__(self, x: int = 0, y: int = 0, w: int = 800, h: int = 100):
        GameObject.__init__(self, x, y, w, h)

    def display(self, game_display):
        pygame.draw.rect(game_display,
                         (255, 0, 0, 255),
                         (self._x, self._y, self._width, self._height))

    def hit_by_bullet(self):
        return


class Border:
    """
        a class that contains 4 game objects just outside the frame so that nothing goes outside of the
        frame
        Note: we might not need this class depending on what Darren has done for us
    """

    _window_width: int
    _window_height: int
    top_border: GameObject
    bottom_border: GameObject
    right_border: GameObject
    left_border: GameObject

    def __init__(self, window_width, window_height):
        """IMPLEMENT!!!"""
        pass

    def collides(self, obj: List[int]):
        return self.top_border.collides(obj) or self.bottom_border.collides(obj) \
               or self.right_border.collides(obj) or self.left_border.collides(obj)


class Bullet(GameObject):
    _speed: int

    def __init__(self, x: int, y: int, w: int, h: int, speed: int):
        super().__init__(x, y, w, h)
        self._speed = speed
        self._w = w
        self._h = h

    def update(self):
        self._x += self._speed

    def display(self, game_display):
        pygame.draw.rect(game_display, WHITE, tuple(self.hitbox()))

    def hit_by_bullet(self):
        return


class Watergun(GameObject):
    bullet_speed: int
    radius: int
    bullets: List[Bullet]
    direction: str
    fired: False

    def __init__(self, x: int, y: int, radius: int, bullet_speed: int):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.bx_dist = 0
        self.by_dist = 0
        self.bullet_speed = bullet_speed
        self.bullets = []
        self.direction = "right"
        self.fired = False

    def display(self, game_display):
        # pygame.draw.circle(game_display, WHITE, (self._x, self._y), self.radius)
        for bullet in self.bullets:
            bullet.display(game_display)

    def update(self, obj: List[GameObject] = []):
        """
        - Update every bullet's location
        - Check if any of the bullets are colliding with any of the GameObjects (use GameObject.collides())
        - If bullet hits any GameObject, call GameObject.hit_by_bullet() and remove the bullet from the list
        """
        for bullet in self.bullets:
            bullet.update()
            for object_ in obj:
                if bullet.collides(object_.hitbox()):
                    object_.hit_by_bullet()
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

    def fire(self):
        if not self.fired and self.direction == "right":
            self.bullets.append(Bullet(self._x, self._y, 20, 10, 10))
            self.fired = True

        if not self.fired and self.direction == "left":
            self.bullets.append(Bullet(self._x, self._y, 20, 10, -10))
            self.fired = True

    def move(self, x: int, y: int):
        self._x = x
        self._y = y

    def hit_by_bullet(self):
        return