import pygame
from constants import TILE_WIDTH
class Tile(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    isLive: bool = False
    x: float
    y: float
    size: int
    tile: pygame.draw.rect

    def __init__(self, screen, x: float, y: float, size: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__(self)

        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.size = size

        self.tile = self.draw(screen)
        # TODO: create a surface

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
        return pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size), TILE_WIDTH)


    def update(self, dt) -> None:
        pass