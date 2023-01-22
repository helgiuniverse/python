import pygame
from pygame import *
from math import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
MOON_WIDTH = 20
MOON_HEIGHT = 20
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
SPACE_COLOR = "black"
EARTH_COLOR = "blue"
MOON_COLOR = "gray"

X0 = WIN_WIDTH // 2
Y0 = WIN_HEIGHT // 2

M0 = 5000
G = 1 # 6.674 * (10 ** -11)
T = 1


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Solar Mechanics v0.1")

    earth = Surface((WIN_WIDTH, WIN_HEIGHT))
    earth.fill(Color(SPACE_COLOR))
    draw.circle(earth, Color(EARTH_COLOR), (X0, Y0), 10)

    timer = pygame.time.Clock()

    moon = Surface((MOON_WIDTH, MOON_HEIGHT))
    moon.fill(Color(SPACE_COLOR))
    draw.circle(moon, Color(MOON_COLOR), (MOON_WIDTH // 2, MOON_HEIGHT // 2), 5)

    x = 100.0
    y = 290.0
    vx = 0.1
    vy = 1.5

    done = False
    while not done:
        timer.tick(50)
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
                break

        r = sqrt((x - X0)**2 + (y - Y0)**2)

        ax = M0 * (X0 - x) / r**3
        ay = M0 * (Y0 - y) / r**3

        vx += T * ax
        vy += T * ay

        x += T * vx
        y += T * vy

        screen.blit(earth, (0, 0))
        screen.blit(moon, (int(x), int(y)))
        pygame.display.update()


main()
