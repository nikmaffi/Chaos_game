import pygame
import random

class Sierpinski:
    def __init__(self, vertex, start):
        self.DICE = 6
        self.COLOR = (255, 255, 255)
        self.RADIUS = 1

        self.vertex = vertex
        self.points = [start]

    def update(self):
        num = int(random.random() * self.DICE + 1)
        target = (-1, -1)
        start = self.points[-1]

        if num in [1, 2]:
            target = self.vertex[0]
        elif num in [3, 4]:
            target = self.vertex[1]
        else:
            target = self.vertex[2]

        diffx = abs(target[0] - start[0]) // 2
        diffy = abs(target[1] - start[1]) // 2

        self.points.append((diffx + min(target[0], start[0]), diffy + min(target[1], start[1])))

    def draw(self, screen):
        for v in self.vertex:
            pygame.draw.circle(screen, self.COLOR, v, self.RADIUS)

        for point in self.points:
            pygame.draw.circle(screen, self.COLOR, point, self.RADIUS)