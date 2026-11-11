
import pygame


class Player:
    def __init__(self, x, y, size=26, speed=4):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.health = 100
        self.score = 0

    def move(self, dx, dy, walls):
        self.rect.x += dx * self.speed

        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                elif dx < 0:
                    self.rect.left = wall.right

        self.rect.y += dy * self.speed

        for wall in walls:
            if self.rect.colliderect(wall):
                if dy > 0:
                    self.rect.bottom = wall.top
                elif dy < 0:
                    self.rect.top = wall.bottom

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (60, 140, 255),
            self.rect,
            border_radius=6
        )
