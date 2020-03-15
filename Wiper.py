import pygame
from numpy import sin, cos

class Wiper:

    pi = 3.14159265
    points = []
    theta_scale = 3
    r_scale = 2

    def __init__(self, screen, pos, r, n, theta):
        self.screen = screen
        self.pos = pos
        self.r = r
        self.n = n
        self.theta = theta

    def draw(self):
        Wiper.points.append(self.drawcurve())
        if len(Wiper.points) > 2:
            pygame.draw.aalines(self.screen, self.get_color(), False, Wiper.points)

    def drawcurve(self):
        x = self.r * cos(self.theta) + self.pos[0]
        y = self.r * sin(self.theta) + self.pos[1]
        pygame.draw.line(self.screen, (255,255,255), self.pos, (x,y))
        if self.n > 1:
            return Wiper(self.screen, (x,y), self.r/Wiper.r_scale, self.n-1, self.theta*Wiper.theta_scale).drawcurve()
        else:
            pygame.draw.circle(self.screen, self.get_color(),(int(x),int(y)) ,5)
            return (int(x),int(y))

    def get_color(self):
        degrees = (self.theta * 180 / Wiper.pi)%360
        color = pygame.Color(255,255,255)
        color.hsva = degrees, 100, 100
        return color

    def update(self):
        self.theta += 0.002
        if self.theta > 2 * Wiper.pi:
            _ = Wiper.points.pop(0)
