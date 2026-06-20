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
                isPause = False
            
            for tile in tiles_group:
                tile.handle_event(screen, event)   

            if not isPause:
                tiles = copy.copy(start(tiles, screen))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def start(tiles, screen):  
    next = copy.copy(tiles) # Is this actually making a copy?

    # How do I make a copy before drawing it up??? Just want to change meta data and then apply the visuals?
    for tiles_row in next:
        for tile in tiles_row:
            neighbors = getNeighbors(tile, tiles)
            print(f"Neighbors of [{tile.x_index}, {tile.y_index}]:")
            for neighbor in neighbors:
                print(f"[{neighbor.x_index}, {neighbor.y_index}]")
                live_neighbors = countLiveNeighbors(neighbors)
            print(f"Live neighbors: {live_neighbors}")
            handleGameOfLifeLogic(tile, live_neighbors, screen)
    pygame.time.delay(5000)
    return next

def handleGameOfLifeLogic(tile, num_n, screen):
    if tile.isLive:
        if num_n == 0 or num_n == 1 or num_n > 3:
            tile.toggle_fill(screen)
            return
    if not tile.isLive and num_n == 3:
        tile.toggle_fill(screen)

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