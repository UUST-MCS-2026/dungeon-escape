
import pygame
import sys

from player import Player
from level import create_level
from ui import draw_hud, draw_message, draw_menu, draw_game_over


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

title_font = pygame.font.SysFont("arial", 42)
font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)


# Состояния игры
MENU = "menu"
PLAYING = "playing"
WON = "won"
GAME_OVER = "game_over"

game_state = MENU


# Создание уровня и игрока
walls, player_start, exit_rect = create_level()
player = Player(*player_start)


def restart_game():
    global player, exit_rect, game_state

    new_walls, start, new_exit = create_level()

    walls.clear()
    walls.extend(new_walls)

    player = Player(*start)
    exit_rect = new_exit

    game_state = PLAYING


# Главный игровой цикл
running = True

while running:
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Главное меню
            if game_state == MENU:
                if event.key == pygame.K_RETURN:
                    game_state = PLAYING
                elif event.key == pygame.K_ESCAPE:
                    running = False

            # Выход из игры
            elif event.key == pygame.K_ESCAPE:
                running = False

            # Перезапуск после победы или поражения
            elif game_state in (WON, GAME_OVER):
                if event.key == pygame.K_r:
                    restart_game()

    # Игровой процесс
    if game_state == PLAYING:

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

        # Проверка здоровья
        if player.health <= 0:
            game_state = GAME_OVER

        # Проверка выхода
        elif exit_rect and player.rect.colliderect(exit_rect):
            game_state = WON

    # Отрисовка
    screen.fill(BLACK)

    if game_state == MENU:

        draw_menu(screen, title_font, small_font)

    elif game_state in (PLAYING, WON, GAME_OVER):

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
        if game_state == WON:
            draw_message(
                screen,
                font,
                "YOU ESCAPED!",
                "Press R to play again"
            )

        # Экран поражения
        elif game_state == GAME_OVER:
            draw_game_over(screen, font)

    pygame.display.flip()


pygame.quit()
sys.exit()
