import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            direction1 = self.velocity.rotate(rand_angle)
            direction2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a = Asteroid(self.position.x, self.position.y, new_radius)
            b = Asteroid(self.position.x, self.position.y, new_radius)
            a.velocity = direction1 * 1.2
            b.velocity = direction2 * 1.2