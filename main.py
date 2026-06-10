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

    screen.fill("black")
    drawBoard(screen)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


def drawBoard(screen):
    y = 0
    for i in range(BOARD_HEIGHT):
        x = 0-TILE_SIZE
        for j in range(BOARD_WIDTH):
            x += TILE_SIZE 
            Tile(x, y, TILE_SIZE).draw(screen)
        y += TILE_SIZE
        
            

if __name__ == "__main__":
    main()
