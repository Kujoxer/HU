#import math
import random
import pygame as pg

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class AiSnake:
    def __init__(self, surface):
        self.surface = surface
        self.pos = (0, 0)
        self.speed = 80

    def draw(self):
        rect = pg.Rect(self.pos, (80, 80))
        border_radius = 10
        pg.draw.rect(self.surface, (0, 200, 0), rect, border_radius=border_radius)

    def move_towards_apple(self, apple_pos):
        snake_x, snake_y = self.pos
        apple_x, apple_y = apple_pos
        self.direction = self.pos
        #random.choice([UP, DOWN, LEFT, RIGHT])
        if apple_x < snake_x:
            self.direction = LEFT
        elif apple_x > snake_x:
            self.direction = RIGHT
        elif apple_y < snake_y:
            self.direction = UP
        elif apple_y > snake_y:
            self.direction = DOWN

        self.pos = (snake_x + self.direction[0]*self.speed, snake_y + self.direction[1]*self.speed)

