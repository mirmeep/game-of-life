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
    tiles_group = pygame.sprite.Group()

    Tile.containers = (tiles_group, updatable, drawable)

    screen.fill("black")

    tiles = drawBoard(screen)
    for i, tiles_row in enumerate(tiles):
        for j, tile in enumerate(tiles_row):
            pass
 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start(tiles_group)
            
            for tile in tiles_group:
                tile.handle_event(screen, event)   
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def start(tiles_group):
    # TODO: For every live cell, store in array (current alive array) to determine next array using game of life rules. Next array becomes current   
    current = []
    for tile in tiles_group:
        if tile.isLive:
            current.append(tile)

    for tile in current:
        print(f"[{tile.x_index}, {tile.y_index}]")

    # TODO: Based on the current tiles coords, calculate neighbors based on their coords

def drawBoard(screen):
    tiles = []
    y = 0
    for y_index in range(BOARD_HEIGHT):
        tiles_row = []
        x = 0-TILE_SIZE
        for x_index in range(BOARD_WIDTH):
            x += TILE_SIZE
            tile = Tile(screen, x, y, x_index, y_index, TILE_SIZE)
            tiles_row.append(tile)        
        y += TILE_SIZE
        tiles.append(tiles_row)
    return tiles
        
if __name__ == "__main__":
    main()