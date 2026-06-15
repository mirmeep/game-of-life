import pygame
from constants import TILE_WIDTH
class Tile(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    isLive: bool = False
    x: int
    y: int
    size: int
    # tile: pygame.draw.rect

    def __init__(self, screen, x: int, y: int, size: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__(self)

        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.size = size

        self.tile = self.draw(screen)
  
    
    def handle_event(self, screen, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.tile.collidepoint(event.pos):
                print(f"[{self.x}, {self.y}] clicked")
                if self.isLive:
                    # TODO: change color
                    pass
                else:
                    # TODO: change color
                    pass
                self.isLive = not self.isLive
                self.update(screen)


    def draw(self, screen: pygame.Surface) -> None:
        self.surface = pygame.Surface((self.size, self.size))
        screen.blit(self.surface, (self.x, self.y))
        self.rect = self.surface.get_rect()
        self.surface.fill(self.color)
        return pygame.draw.rect(screen, (255, 255, 255), self.rect, TILE_WIDTH)


    def update(self, dt) -> None:
        pass