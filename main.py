import pygame
from pygame.color import THECOLORS
import os
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT,
                       ASTEROID_MIN_RADIUS, ASTEROID_KINDS,
                       ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS)
# must be used before pygame import
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(THECOLORS["black"])
        pygame.display.flip()  # display update


if __name__ == "__main__":
    main()
