
import pygame

WHITE = (240, 240, 240)
GOLD = (255, 200, 50)
DARK = (20, 20, 25)


def draw_hud(screen, font, health, score):
    """Отображает здоровье игрока и количество очков."""
    health_text = font.render(f"Здоровье: {health}", True, WHITE)
    score_text = font.render(f"Очки: {score}", True, GOLD)

    screen.blit(health_text, (10, 45))
    screen.blit(score_text, (10, 75))


def draw_message(screen, font, title, subtitle):
    """Отображает сообщение по центру экрана."""
    width, height = screen.get_size()

    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    title_image = font.render(title, True, GOLD)
    subtitle_image = font.render(subtitle, True, WHITE)

    screen.blit(
        title_image,
        title_image.get_rect(
            center=(width // 2, height // 2 - 25)
        )
    )

    screen.blit(
        subtitle_image,
        subtitle_image.get_rect(
            center=(width // 2, height // 2 + 20)
        )
    )


def draw_menu(screen, title_font, text_font):
    """Отображает главное меню игры."""
    screen.fill(DARK)

    width, height = screen.get_size()

    title = title_font.render("DUNGEON ESCAPE", True, GOLD)
    start = text_font.render("Press ENTER to start", True, WHITE)
    quit_text = text_font.render("Press ESC to quit", True, WHITE)

    screen.blit(
        title,
        title.get_rect(center=(width // 2, height // 2 - 60))
    )

    screen.blit(
        start,
        start.get_rect(center=(width // 2, height // 2 + 10))
    )

    screen.blit(
        quit_text,
        quit_text.get_rect(center=(width // 2, height // 2 + 50))
    )


def draw_game_over(screen, font):
    """Отображает экран проигрыша."""
    draw_message(
        screen,
        font,
        "GAME OVER",
        "Press R to try again"
    )
