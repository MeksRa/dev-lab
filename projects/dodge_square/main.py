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
        self.GREEN: tuple = (34, 139, 34)

        # Font
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, 26)

        # Player
        self.player_size: int = 30
        self.player_pos: list[int] = [0, 0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_pos: list[float] = []
        self.enemy_list: list[list[float]] = []
        self.enemy_speed: float = 3
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

    def create_enemy(self):
        """Creates a new enemy at a random position"""
        enemy_pos: list[float] = [
            random.randint(0, self.screen_width - self.enemy_size),
            -self.enemy_size,
        ]
        self.enemy_list.append(enemy_pos)

    def update_enemy_positions(self):
        """Check whether it is time to create a new enemy and then does so"""
        if self.frame_count % self.enemy_frequency == 0:
            self.create_enemy()

        # Give each enemy an id
        for idx, enemy_pos in enumerate(self.enemy_list):
            # Simulate gravity until off-screen
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed
            else:
                # +1 score when the enemy has passed
                self.enemy_list.pop(idx)
                self.score += 1
                self.enemy_speed += 0.5

                # Increase the difficulty each 15 points
                if self.enemy_frequency > 10 and self.score % 15 == 0:
                    self.enemy_frequency -= 2

    def detect_collision(self, player_pos: list[int], enemy_pos: list[float]) -> bool:
        """Collision detection logic for checking if squares are intercepting"""
        px, py = player_pos
        ex, ey = enemy_pos

        # (X) if left side of enemy sqaure falls within the range
        # of player square. => and opposite of that
        return bool(
            (px <= ex < px + self.player_size or ex <= px < ex + self.enemy_size)
            and (py <= ey < py + self.player_size or ey <= py < ey + self.enemy_size)
        )

    def show_game_over(self):
        """Display game-over text"""
        # Create the text
        game_over_text = self.font.render("Game Over", True, self.WHITE)
        # Make sure the text is centred
        text_width, text_height = game_over_text.get_size()
        coordinates: tuple = (
            self.screen_width // 2 - text_width // 2,
            self.screen_height // 2 - text_height // 2,
        )
        self.screen.blit(game_over_text, coordinates)

    def replay_game(self):
        """Reset everything to its initial state"""
        # Reset enemies
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20

        # Reset game stats
        self.game_over: bool = False
        self.frame_count: int = 0
        self.score: int = 0

    def draw_character(self, color: tuple, position: list[float] | list[int], size: int):
        """Draws a rectangle on the screen"""
        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Reset game
                # if event.type == pygame.KEYDOWN:
                #    if self.game_over and event.key == pygame.K_r:
                # self.replay_game()
                if (
                    event.type == pygame.KEYDOWN
                    and self.game_over
                    and event.key == pygame.K_r
                ):
                    self.replay_game()

                # Get the current mouse position
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

                # Update the player's position to follow the mouse
                self.player_pos[0] = mouse_pos[0] - self.player_size // 2
                self.player_pos[1] = mouse_pos[1] - self.player_size // 2

                # Make sure the player stays on the screen
                self.player_pos[0] = max(
                    0, min(self.player_pos[0], self.screen_width - self.player_size)
                )
                self.player_pos[1] = max(
                    0, min(self.player_pos[1], self.screen_height - self.player_size)
                )

            if not self.game_over:
                self.update_enemy_positions()

                for enemy_pos in self.enemy_list:
                    if self.detect_collision(self.player_pos, enemy_pos):
                        self.game_over = True
                        break

                # Reset everything for the next frame
                self.screen.fill(self.BLACK)

                # Draw the player
                self.draw_character(self.WHITE, self.player_pos, self.player_size)

                # Draw the enemies
                for enemy_pos in self.enemy_list:
                    if self.score > 20:
                        self.draw_character(self.BLUE, enemy_pos, self.enemy_size)
                        if self.score > 40:
                            self.draw_character(self.GREEN, enemy_pos, self.enemy_size)
                    else:
                        self.draw_character(self.RED, enemy_pos, self.enemy_size)

                # Display the score
                score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
                self.screen.blit(score_text, [10, 10])

                # Increment the frame count
                self.frame_count += 1
            else:
                self.show_game_over()
            pygame.display.update()
            self.clock.tick(60)


def main() -> None:
    game = DodgySquare()
    game.run()


if __name__ == "__main__":
    main()
