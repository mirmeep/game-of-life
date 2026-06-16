import pygame
from constants import TILE_WIDTH
class Tile(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    isLive: bool = False
    x: int
    y: int
    size: int

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
        if event.type == pygame.MOUSEBUTTONUP:
            if self.tile.collidepoint(event.pos):
                print(f"[{self.x}, {self.y}] clicked")
                if self.isLive:
                    self.fill_color = (0, 0, 0)
                    self.outline_color = (255, 255, 255)
                else:
                    self.fill_color = (255, 255, 255)
                    self.outline_color = (0, 0, 0)
                self.isLive = not self.isLive
                self.draw(screen)

    def draw(self, screen: pygame.Surface) -> None:
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.fill_color)
        screen.blit(self.surface, (self.x, self.y))
        return pygame.draw.rect(screen, self.outline_color, pygame.Rect(self.x, self.y, self.size, self.size), TILE_WIDTH)

    def update(self, dt) -> None:
        pass