
import pygame
import sys

from player import Player
from level import create_level
from ui import draw_hud, draw_message


# Инициализация игры
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (20, 20, 25)
GRAY = (75, 75, 85)
GREEN = (50, 200, 100)
GOLD = (255, 200, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Escape")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)


# Создание уровня и игрока
walls, player_start, exit_rect = create_level()
player = Player(*player_start)

running = True
won = False


def restart_game():
    global player, won, exit_rect

    new_walls, start, new_exit = create_level()

    walls.clear()
    walls.extend(new_walls)

    player = Player(*start)
    exit_rect = new_exit
    won = False


# Главный игровой цикл
while running:
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and won:
            if event.key == pygame.K_r:
                restart_game()

    # Управление игроком
    if not won:
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1

        player.move(dx, dy, walls)

        # Проверка выхода
        if exit_rect and player.rect.colliderect(exit_rect):
            won = True

    # Отрисовка
    screen.fill(BLACK)

    # Стены
    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)

    # Выход
    if exit_rect:
        pygame.draw.rect(screen, GREEN, exit_rect)

    # Игрок
    player.draw(screen)

    # Заголовок
    title = font.render("DUNGEON ESCAPE", True, GOLD)
    screen.blit(title, (10, 10))

    # Интерфейс
    draw_hud(screen, font, player.health, player.score)

    # Экран победы
    if won:
        draw_message(
            screen,
            font,
            "YOU ESCAPED!",
            "Press R to play again"
        )

    pygame.display.flip()


pygame.quit()
sys.exit()
