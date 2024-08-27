import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def hasCollided(self, other_circle):
        # Calculate the distance between the two circle centers
        distance = self.position.distance_to(other_circle.position)
        
        # Check if the distance is less than the sum of the radii
        if distance <= self.radius + other_circle.radius:
            return True
        else:
            return False