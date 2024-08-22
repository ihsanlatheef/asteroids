import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updateable, drawable)
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updateable_item in updateable:
            updateable_item.update(dt)

        screen.fill("black")

        for drawable_item in drawable:
            drawable_item.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()