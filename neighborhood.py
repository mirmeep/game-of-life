import pygame
from constants import *

def countLiveNeighbors(neighbors): # TODO: functionally filter and get length
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
    if x+1 < BOARD_HEIGHT and y-1 >= 0:
        neighbors.append(tiles[x+1][y-1])

    # Left
    if x-1 >= 0:
        neighbors.append(tiles[x-1][y])

    # Right
    if x+1 < BOARD_HEIGHT:
        neighbors.append(tiles[x+1][y])
    
    # Bottom left
    if x-1 >= 0 and y+1 < BOARD_WIDTH:
        neighbors.append(tiles[x-1][y+1])

    # Bottom
    if y+1 < BOARD_WIDTH:
        neighbors.append(tiles[x][y+1])

    # Bottom right
    if x+1 < BOARD_HEIGHT and y+1 < BOARD_WIDTH:
        neighbors.append(tiles[x+1][y+1])

    return neighbors