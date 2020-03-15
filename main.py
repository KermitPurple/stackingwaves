import pygame
import os
from Wiper import Wiper
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 650,650
screen = pygame.display.set_mode(size)
wiper = Wiper(screen, (int(size[0]/2), int(size[1]/2)), 150, 1, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode >= '1' and event.unicode <= '9':
                new_n = int(event.unicode)
                if wiper.n != new_n:
                    wiper.n = new_n 
                    wiper.theta = 0
                    Wiper.points = []
    screen.fill((0,0,0))
    wiper.draw()
    wiper.update()
    pygame.display.update()
