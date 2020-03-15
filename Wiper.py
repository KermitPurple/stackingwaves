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
        self.drawcurve()
        self.drawline()

    def drawcurve(self, arr = []):
        for i in range(100):
            theta = i/50 * Wiper.pi
            x = self.r * cos(theta) + self.pos[0]
            y = self.r * sin(theta) + self.pos[1]
            if self.n > 1:
                Wiper(self.screen, (x,y), self.r/3, self.n-1, self.theta*3).drawcurve()
            else:
                arr.append((x,y))
        pygame.draw.polygon(self.screen, (255,255,255), arr, 1)



    def drawline(self):
        x = self.r * cos(self.theta) + self.pos[0]
        y = self.r * sin(self.theta) + self.pos[1]
        pygame.draw.line(self.screen, (255,255,255), self.pos, (x,y))
        if self.n > 1:
            Wiper(self.screen, (x,y), self.r/3, self.n-1, self.theta*3).drawline()

    def update(self):
        self.theta += 0.0005
