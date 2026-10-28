
import pygame
import sys

pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 40
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Escape")
clock = pygame.time.Clock()

# Цвета
BLACK = (20, 20, 25)
WHITE = (240, 240, 240)
GRAY = (75, 75, 85)
BLUE = (60, 140, 255)
GOLD = (255, 200, 50)
GREEN = (50, 200, 100)

font = pygame.font.SysFont("arial", 28)

# Карта: # — стена, P — игрок, E — выход
level_map = [
    "####################",
    "#P.....#...........#",
    "#......#..####.....#",
    "#.............#....#",
    "#..####.......#....#",
    "#.............#....#",
    "#.....#####........#",
    "#..............#...#",
    "#..####............#",
    "#.................E#",
    "####################",
]

walls = []
exit_rect = None
player = pygame.Rect(0, 0, 26, 26)

for row_index, row in enumerate(level_map):
    for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE

        if tile == "#":
            walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
        elif tile == "P":
            player.topleft = (x + 7, y + 7)
        elif tile == "E":
            exit_rect = pygame.Rect(x + 5, y + 5, 30, 30)

# Игровое состояние
speed = 4
running = True
won = False


def draw_text(text, x, y, color=WHITE):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


def move_player(dx, dy):
    # Движение по горизонтали
    player.x += dx
    for wall in walls:
        if player.colliderect(wall):
            if dx > 0:
                player.right = wall.left
            elif dx < 0:
                player.left = wall.right

    # Движение по вертикали
    player.y += dy
    for wall in walls:
        if player.colliderect(wall):
            if dy > 0:
                player.bottom = wall.top
            elif dy < 0:
                player.top = wall.bottom


while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and won:
            if event.key == pygame.K_r:
                player.topleft = (TILE_SIZE + 7, TILE_SIZE + 7)
                won = False

    keys = pygame.key.get_pressed()

    if not won:
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = speed

        move_player(dx, dy)

        if exit_rect and player.colliderect(exit_rect):
            won = True

    # Отрисовка
    screen.fill(BLACK)

    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)

    if exit_rect:
        pygame.draw.rect(screen, GREEN, exit_rect)

    pygame.draw.rect(screen, BLUE, player, border_radius=6)

    draw_text("DUNGEON ESCAPE", 10, 10, GOLD)

    if won:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        draw_text("YOU ESCAPED!", 285, 250, GREEN)
        draw_text("Press R to play again", 260, 300)

    pygame.display.flip()

pygame.quit()
sys.exit()
