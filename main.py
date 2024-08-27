import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updateable_item in updateable:
            updateable_item.update(dt)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.hasCollided(bullet):
                    asteroid.split(screen)
                    bullet.kill()
            if asteroid.hasCollided(player):
                sys.exit("Game over!")

        screen.fill("black")

        for drawable_item in drawable:
            drawable_item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()