import pygame
import os
from Wiper import Wiper
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 1300, 650
screen = pygame.display.set_mode(size)
wiper = Wiper(screen, (int(size[0]/4), int(size[1]/2)), 100, 1, 0)
Wiper.print_controls()
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
                elif selected == 's':
                    if new == 1:
                        if Wiper.speed != 0.0001:
                            Wiper.speed = 0.0001
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 2:
                        if Wiper.speed != 0.0005:
                            Wiper.speed = 0.0005
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 3:
                        if Wiper.speed != 0.001:
                            Wiper.speed = 0.001
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 4:
                        if Wiper.speed != 0.002:
                            Wiper.speed = 0.002
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 5:
                        if Wiper.speed != 0.003:
                            Wiper.speed = 0.003
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 6:
                        if Wiper.speed != 0.004:
                            Wiper.speed = 0.004
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 7:
                        if Wiper.speed != 0.005:
                            Wiper.speed = 0.005
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 8:
                        if Wiper.speed != 0.02:
                            Wiper.speed = 0.02
                            wiper.theta = 0
                            Wiper.points = []
                    elif new == 9:
                        if Wiper.speed != 0.05:
                            Wiper.speed = 0.05
                            wiper.theta = 0
                            Wiper.points = []
            elif event.unicode == 'r' or event.unicode == 'n' or event.unicode == 's':
                selected = str(event.unicode)
            elif event.unicode == 't':
                selected = "theta"
            elif event.unicode == 'p':
                wiper.paused = not wiper.paused
            elif event.unicode == 'd':
                Wiper.deletion_mode = not Wiper.deletion_mode
                wiper.theta = 0
                Wiper.points = []
            elif event.unicode == 'l':
                Wiper.line_on = not Wiper.line_on
            elif event.unicode == 'c':
                Wiper.curve_on = not Wiper.curve_on
    screen.fill((0,0,0))
    wiper.update()
    wiper.draw()
    pygame.display.update()
