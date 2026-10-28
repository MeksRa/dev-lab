import random
import sys

import pygame
from pygame.font import Font
from pygame.time import Clock

# pip install pygame-ce
# cuz the standard 'pygame' doesn't work yet in version 3.14.7


class DodgySquare:
    def __init__(self) -> None:
        # Pygame
        pygame.init()
        pygame.mouse.set_visible(False)

        # Screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Dodgy Square")

        # Colours
        self.WHITE: tuple = (255, 255, 255)
        self.BLACK: tuple = (0, 0, 0)
        self.RED: tuple = (255, 99, 71)
        self.BLUE: tuple = (65, 105, 225)

        # Font
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, 26)

        # Player
        self.player_size: int = 30
        self.player_pos: list[int] = [0, 0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_pos: list[int] = []
        self.enemy_list: list[list[int]] = []
        self.enemy_speed: int = 3
        # game's going to be running at 60 frames per second
        # 1 enemy per 20 frames => 60 / 20 = 3 enemy per 1 sec
        self.enemy_frequency: int = 20  # Low = Lots, High = Few

        # Clock
        self.clock: Clock = pygame.time.Clock()

        # Game data
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int = 0

        # --- --
