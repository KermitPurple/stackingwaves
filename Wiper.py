import pygame
from numpy import sin, cos

class Wiper:

    pi = 3.14159265

    def __init__(self, screen, pos, r, n, theta):
        self.screen = screen
        self.pos = pos
        self.r = r
        self.n = n
        self.theta = theta

    def draw(self):
        x = self.r * cos(self.theta) + self.pos[0]
        y = self.r * sin(self.theta) + self.pos[1]
        pygame.draw.line(self.screen, (255,255,255), self.pos, (x,y))
