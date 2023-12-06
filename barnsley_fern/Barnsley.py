import pygame
import random

class Barnsley:
    def __init__(self, scale_x, scale_y, win_size):
        self.COLOR = (99, 183, 108)
        self.RADIUS = 1
        self.UPDATE_FACTOR = 0.5 * 3.22

        self.scale_x = scale_x
        self.scale_y = scale_y
        self.win_size = win_size
        self.updates = 25

        self.points = [(0, 0)]

        self.map = lambda x, a1, b1, a2, b2: a2 + (x - a1) / (b1 - a1) * (b2 - a2)

        self.f1 = lambda p: (0, 0.16 * p[1])
        self.f2 = lambda p: (0.85 * p[0] + 0.04 * p[1], -0.04 * p[0] + 0.85 * p[1] + 1.6)
        self.f3 = lambda p: (0.20 * p[0] - 0.26 * p[1], 0.23 * p[0] + 0.22 * p[1] + 1.6)
        self.f4 = lambda p: (-0.15 * p[0] + 0.28 * p[1], 0.26 * p[0] + 0.24 * p[1] + 0.44)

    def update(self):
        for _ in range(int(self.updates)):
            num = random.random()

            if num < 0.01:
                self.points.append(self.f1(self.points[-1]))
            elif num < 0.86:
                self.points.append(self.f2(self.points[-1]))
            elif num < 0.93:
                self.points.append(self.f3(self.points[-1]))
            else:
                self.points.append(self.f4(self.points[-1]))

        self.updates += self.UPDATE_FACTOR

    def draw(self, screen):
        for p in self.points:
            p = (
                self.map(p[0], self.scale_x[0], self.scale_x[1], 0, self.win_size[0]),
                self.map(p[1], self.scale_y[1], self.scale_y[0], 0, self.win_size[1])
            )

            pygame.draw.circle(screen, self.COLOR, p, self.RADIUS)