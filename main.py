import pygame
import copy
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

    isPause = True
    steps_count = 0

    tiles = drawBoard(screen)
    for i, tiles_row in enumerate(tiles):
        for j, tile in enumerate(tiles_row):
            print(f"tile is[{i}, {j}]")
            print(f"tile is [{tile.x_index}, {tile.y_index}]")
 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if isPause:
                    isPause = False
                    print("game start")
                else:
                    isPause = True
                    print("game pause")
            
            for tile in tiles_group:
                tile.handle_event(screen, event)   

        if not isPause: 
            steps_count += 1
            print(steps_count) 
            tiles = start(tiles)            
            toggle(tiles, screen)
            pygame.display.update()
            pygame.time.delay(3000)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def toggle(tiles, screen):
    for tiles_row in tiles:
        for tile in tiles_row:
            if tile.isLive is not tile.nextIsLive:
                tile.toggle_fill(screen)

def start(tiles):  
    for tiles_row in tiles:
        for tile in tiles_row:
            neighbors = getNeighbors(tile, tiles)
            live_neighbors = countLiveNeighbors(neighbors)
            handleGameOfLifeLogic(tile, live_neighbors)
    return tiles

def handleGameOfLifeLogic(tile, num_n):
    if tile.isLive:
        if num_n == 0 or num_n == 1 or num_n > 3:
            tile.nextIsLive = False
            print(f"[{tile.x_index}, {tile.y_index}] is now Dead")
            return
        if num_n == 2 or num_n == 3:
            print(f"[{tile.x_index}, {tile.y_index}] STILL Live")
            return
    if not tile.isLive and num_n == 3:
        tile.nextIsLive = True
        print(f"[{tile.x_index}, {tile.y_index}] is now Live")
        return


def countLiveNeighbors(neighbors):
    num_live_neighbors = 0
    for neighbor in neighbors:
        if neighbor.isLive:
            num_live_neighbors += 1
    return num_live_neighbors

def getNeighbors(tile, tiles):
    neighbors = []
    x = tile.x_index
    y = tile.y_index

    # Upper left
    if x-1 >= 0 and y-1 >= 0:
        neighbors.append(tiles[x-1][y-1])
    
    # Top
    if y-1 >= 0:
        neighbors.append(tiles[x][y-1])
    
    # Upper right
    if x+1 < BOARD_WIDTH and y-1 >= 0:
        neighbors.append(tiles[x+1][y-1])

    # Left
    if x-1 >= 0:
        neighbors.append(tiles[x-1][y])

    # Right
    if x+1 < BOARD_WIDTH:
        neighbors.append(tiles[x+1][y])
    
    # Bottom left
    if x-1 >= 0 and y+1 < BOARD_HEIGHT:
        neighbors.append(tiles[x-1][y+1])

    # Bottom
    if y+1 < BOARD_HEIGHT:
        neighbors.append(tiles[x][y+1])

    # Bottom right
    if x+1 < BOARD_WIDTH and y+1 < BOARD_HEIGHT:
        neighbors.append(tiles[x+1][y+1])

    return neighbors

def drawBoard(screen):
    tiles = []
    y = 0
    for x_index in range(BOARD_HEIGHT):
        tiles_row = []
        x = 0-TILE_SIZE
        for y_index in range(BOARD_WIDTH):
            x += TILE_SIZE
            tile = Tile(screen, x, y, x_index, y_index, TILE_SIZE)
            tiles_row.append(tile)        
        y += TILE_SIZE
        tiles.append(tiles_row)
    return tiles
        
if __name__ == "__main__":
    main()