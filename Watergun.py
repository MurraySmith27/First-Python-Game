import math
import pygame
from GameObject import GameObject


class Watergun(GameObject):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    speed: int
    radius: int

    def __int__(self, x: int, y: int, speed: int, radius: int):
        #hitbox contained within circle
        super().__init__(x, y, radius * 2, radius * 2)
        self.speed = speed
        self.radius = radius

    def display(self, game_display, gun_fired):
        if gun_fired:
            #bullet is visible
            pygame.draw.circle(game_display, self.WHITE, (int(self._x), int(self._y)), self.radius)
        else:
            #bullet no visible
            pygame.draw.circle(game_display, self.BLACK, (int(self._x), int(self._y)), self.radius)

    #gets bullet direction
    def calc_proj(self, boy: GameObject, mouse_pos: tuple):
        x1 = boy.get_x()
        y1 = boy.get_y()
        x2 = mouse_pos[0]
        y2 = mouse_pos[1]
        bx_dist: float = x2 - x1
        by_dist: float = y2 - y1
        b_length: float = math.sqrt(bx_dist ** 2 + by_dist ** 2)
        # bullets travel relative to angle of bullet
        self.bx_dist = (bx_dist / b_length) * self.speed
        self.by_dist = (by_dist / b_length) * self.speed

    #moves bullet
    def fire(self):
        self.x += self.bx_dist
        self.y += self.by_dist
