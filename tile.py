import pygame
from constants import TILE_WIDTH
class Tile(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    isLive: bool = False
    justClicked: bool = False
    x: int
    y: int
    size: int

    _isDragging: bool = False
    _justClickedItems = []
    _toggleStatus = True # when dragging, control whether same isLive statuses of tiles are toggled

    def __init__(self, screen, x: int, y: int, size: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__(self)

        self.fill_color = (0, 0, 0)
        self.outline_color = (255, 255, 255)
        self.x = x
        self.y = y
        self.size = size
        self.tile = self.draw(screen)
    
    def handle_event(self, screen, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.tile.collidepoint(event.pos):  
                print(f"[{self.x}, {self.y}] clicked")
                self.handle_pointer_down(screen)

        if event.type == pygame.MOUSEMOTION:
            if self.tile.collidepoint(event.pos):
                self.handle_dragging(screen)

        if event.type == pygame.MOUSEBUTTONUP:
            if self.tile.collidepoint(event.pos):
                self.handle_pointer_up(screen)     
    
    def handle_pointer_down(self, screen):
        Tile._isDragging = True
        self.justClicked = True
        Tile._justClickedItems.append(self)
        Tile._toggleStatus = self.isLive
        self.toggle_fill(screen)
    
    def handle_dragging(self, screen):
        if Tile._isDragging and not self.justClicked and Tile._toggleStatus is self.isLive:
            self.justClicked = True
            Tile._justClickedItems.append(self)
            self.toggle_fill(screen)

    @staticmethod
    def handle_pointer_up(self):
        Tile._isDragging = False
        for tile in Tile._justClickedItems:
            tile.justClicked = False
            Tile._justClickedItems = []

    def toggle_fill(self, screen):
        if self.isLive:
            self.fill_color = (0, 0, 0)
        else:
            self.fill_color = (255, 255, 255)
        self.isLive = not self.isLive
        self.draw(screen)  
        print(self.isLive) 

    def draw(self, screen: pygame.Surface) -> None:
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.fill_color)
        screen.blit(self.surface, (self.x, self.y))
        return pygame.draw.rect(screen, self.outline_color, pygame.Rect(self.x, self.y, self.size, self.size), TILE_WIDTH)

    def update(self, dt) -> None:
        pass