import pygame
import os
from Wiper import Wiper
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 650,650
screen = pygame.display.set_mode(size)
wiper = Wiper(screen, (int(size[0]/2), int(size[1]/2)), 100, 1, 0)
selected = 'n'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode >= '1' and event.unicode <= '9':
                new = int(event.unicode)
                if selected == 'n':
                    if wiper.n != new:
                        wiper.n = new 
                        wiper.theta = 0
                        Wiper.points = []
                elif selected == 'r':
                    if Wiper.r_scale != new:
                        Wiper.r_scale = new 
                        wiper.theta = 0
                        Wiper.points = []
                elif selected == 'theta':
                    if Wiper.theta_scale != new:
                        Wiper.theta_scale = new 
                        wiper.theta = 0
                        Wiper.points = []
            elif event.unicode == 'r' or event.unicode == 'n':
                selected = str(event.unicode)
            elif event.unicode == 't':
                selected = "theta"
    screen.fill((0,0,0))
    wiper.draw()
    wiper.update()
    pygame.display.update()
