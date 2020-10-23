import pygame

class Curve:
    """Store and display a series of points in a curve"""
    def __init__(self, screen, pos, max_x):
        self.screen = screen
        self.pos = pos
        self.max_x = max_x
        self.y_values = []

    def draw(self, color):
        """draw the curve
        :returns: None
        """
        if len(self.y_values) > 1:
            pygame.draw.circle(self.screen, color, (int(self.pos[0]), self.y_values[0]), 5)
            pygame.draw.aalines(self.screen, color, False, [(x + self.pos[0], y) for x, y in enumerate(self.y_values)])

    def update(self, y):
        """add a new point to y_values
        :y: value to add
        :returns: None
        """
        self.y_values.insert(0, int(y))
        if len(self.y_values) > self.max_x:
            self.y_values.pop(-1)

    def clear(self):
        """ empty y values stored
        """
        self.y_values = []
