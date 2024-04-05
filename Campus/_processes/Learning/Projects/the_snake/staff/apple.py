import pygame as pg


class Apple:
    def __init__(self, surface):
        self.surface = surface
        self.pos = (0, 0)

    def draw(self):
        rect = pg.Rect(self.pos, (80, 80))
        border_radius = 40
        pg.draw.rect(self.surface, (255, 0, 0), rect, border_radius=border_radius)


    def move(self, target):
        x = (80 * (target[0] // 80))
        y = (80 * (target[1] // 80))

        self.pos = (x, y)


