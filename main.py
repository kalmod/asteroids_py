import pygame
from pygame.color import THECOLORS
import os
from asteroid import Asteroid
from asteroidfield import AsteroidField
import asteroidfield
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
)
from player import Player, Shot
import sys

# must be used before pygame import
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyTime = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (bullets, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # pauses loop until 1/60th second passes

        for obj in updatable:
            obj.update(dt)  # player.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in bullets:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()

        # rendering
        screen.fill(THECOLORS["black"])
        for obj in drawable:
            obj.draw(screen)  # player.draw(screen)
        pygame.display.flip()  # display update

        dt = pyTime.tick(60) / 1000  # convert milliseconds to seconds


if __name__ == "__main__":
    main()
