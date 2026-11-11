
import pygame


TILE_SIZE = 40

LEVEL_MAP = [
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


def create_level():
    walls = []
    player_start = (TILE_SIZE + 7, TILE_SIZE + 7)
    exit_rect = None

    for row_index, row in enumerate(LEVEL_MAP):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE

            if tile == "#":
                walls.append(
                    pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                )
            elif tile == "P":
                player_start = (x + 7, y + 7)
            elif tile == "E":
                exit_rect = pygame.Rect(x + 5, y + 5, 30, 30)

    return walls, player_start, exit_rect
