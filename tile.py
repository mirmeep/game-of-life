import pygame
class Tile(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    isLive: bool = False
    x: float
    y: float
    size: float

    def __init__(self, x: float, y: float, size: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "#ffffff", pygame.Rect(self.x, self.y, self.size, self.size), 2)

    def update(self, dt: float) -> None:
        # must override
        pass