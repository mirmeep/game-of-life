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

    tiles = drawBoard(screen)
    for i, tiles_row in enumerate(tiles):
        for j, tile in enumerate(tiles_row):
            print(f"{tile}: [{i}, {j}]")

    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def drawBoard(screen):
    tiles = []
    y = 0
    for _ in range(BOARD_HEIGHT):
        tiles_row = []
        x = 0-TILE_SIZE
        for _ in range(BOARD_WIDTH):
            x += TILE_SIZE 
            tile = Tile(x, y, TILE_SIZE)
            tiles_row.append(tile)
            tile.draw(screen)
        y += TILE_SIZE
        tiles.append(tiles_row)

    return tiles
        
            

if __name__ == "__main__":
    main()
