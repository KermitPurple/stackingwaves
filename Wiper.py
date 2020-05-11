import pygame
from numpy import sin, cos

class Wiper:

    pi = 3.14159265
    points = []
    theta_scale = 3
    r_scale = 2
    speed = 0.002
    deletion_mode = False
    line_on = True
    curve_on = True

    def __init__(self, screen, pos, r, n, theta):
        self.screen = screen
        self.pos = pos
        self.r = r
        self.n = n
        self.theta = theta
        self.paused = False
        self.current_y = None

    def draw(self):
        if (self.theta < 2 * Wiper.pi or not Wiper.deletion_mode) and not self.paused:
            Wiper.points.append(self.drawcurve())
        else: 
            self.drawcurve()
        if len(Wiper.points) > 2 and Wiper.curve_on:
            pygame.draw.aalines(self.screen, self.get_color(), False, Wiper.points)
        if Wiper.line_on:
            self.drawline()

    def drawcurve(self):
        x = self.r * cos(self.theta) + self.pos[0]
        y = self.r * sin(self.theta) + self.pos[1]
        if self.n > 1:
            x, y = Wiper(self.screen, (x,y), self.r/Wiper.r_scale, self.n-1, self.theta*Wiper.theta_scale).drawcurve()
        self.current_y = int(y)
        return (int(x),int(y))

    def drawline(self):
        x = self.r * cos(self.theta) + self.pos[0]
        y = self.r * sin(self.theta) + self.pos[1]
        pygame.draw.line(self.screen, (255,255,255), self.pos, (x,y))
        if self.n > 1:
            Wiper(self.screen, (x,y), self.r/Wiper.r_scale, self.n-1, self.theta*Wiper.theta_scale).drawline()
        else:
            pygame.draw.circle(self.screen, self.get_color(),(int(x),int(y)) ,5)

    def get_color(self):
        degrees = (self.theta * 180 / Wiper.pi)%360
        color = pygame.Color(255,255,255)
        color.hsva = degrees, 100, 100
        return color

    def update(self):
        if not self.paused:
            self.theta += Wiper.speed
            if self.theta > 2 * Wiper.pi and len(Wiper.points) > 0:
                _ = Wiper.points.pop(0)
            if self.theta > 4 * Wiper.pi:
                if Wiper.deletion_mode:
                    self.theta = 0
                else:
                    self.theta = 2 * Wiper.pi

    @classmethod
    def print_controls(self):
        print("=" * 75)
        print("p = pause")
        print("c = toggle curve")
        print("l = toggle line")
        print("d = deletion mode")
        print("r = select r scale")
        print("t = select theta scale")
        print("n = select n")
        print("s = select speed")
        print("1-9 = change value for selected")
        print("=" * 75)
