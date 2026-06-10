import pygame
from constants import *
from logger import log_state
from tile import Tile

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    tiles = pygame.sprite.Group()

    Tile.containers = (tiles, updatable, drawable)

    # TODO: Create tileboard. Tileboard will handle creating tiles
    while True:
        screen.fill("black")
        tile = Tile(30, 30, TILE_SIZE)
        tile.draw(screen)

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
