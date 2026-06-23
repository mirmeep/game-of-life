import pygame
from constants import *
from logger import log_state
from tile import Tile
from neighborhood import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")

    initializeSpriteGroups()

    tiles = drawBoard(screen)
    isPause = True
    steps_count = 0
 
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
            
            for tiles_row in tiles:
                for tile in tiles_row:
                    tile.handle_event(screen, event)   

        if not isPause: 
            steps_count += 1
            # print(f"Step {steps_count}") # Include if you want! 
            tiles = start(tiles)            
            toggle(tiles, screen)
            pygame.display.update()
            pygame.time.delay(100)
        pygame.display.flip()

def initializeSpriteGroups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()

    Tile.containers = (tiles_group, updatable, drawable)

def toggle(tiles, screen): 
    for tiles_row in tiles:
        for tile in tiles_row:
            if tile.isLive is not tile.nextIsLive:
                tile.toggle_fill(screen)

def start(tiles):  
    for tiles_row in tiles:
        for tile in tiles_row:
            neighbors = getNeighbors(tile, tiles) # TODO: optimize- only getNeighbors of live cells (this didn't work- perhaps, second order neighbors of each live cell?)
            live_neighbors = countLiveNeighbors(neighbors)
            handleGameOfLifeLogic(tile, live_neighbors)
    return tiles

def handleGameOfLifeLogic(tile, num_n):
    if tile.isLive:
        if num_n == 0 or num_n == 1 or num_n > 3:
            tile.nextIsLive = False
            return
        if num_n == 2 or num_n == 3:
            return
    if not tile.isLive and num_n == 3:
        tile.nextIsLive = True
        return

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