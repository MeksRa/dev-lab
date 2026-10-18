import json
import random
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "stats.json"


class SlotMachine:
    def __init__(self, username: str, coins: int) -> None:
        self.username = username
        self.coins = coins
        self.symbols: dict[str, int] = {"🍏": 1, "🍎": 2, "🍇": 5, "🍋": 10, "🔔": 20}

    def save_stats(self) -> None:
        """Saves the player's current data to a JSON file."""
        data: dict[str, int] = {}
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}

        data[self.username] = self.coins

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def spin(self, bet: int) -> None:
        if bet <= 0:
            print("Bet must be greater than 0.")
            return

        if self.coins < bet:
            print("Not enough coins.")
            return

        self.update_coins(-bet)
        result: list[str] = []
        for _ in range(5):
            time.sleep(0.1)
            landed: str = random.choice(list(self.symbols))
            print(landed, end="", flush=True)
            result.append(landed)
        print()

        winnings: int = self.calculate_winnings(result, bet)
        print(f"Coins won: {winnings}")

        self.coins += winnings
        self.save_stats()

        if self.coins == 0:
            print(f"Game over, {self.username}!")
            sys.exit()
        else:
            print(f"Coins remaining: {self.coins}")
            print("=============================")

    def calculate_winnings(self, result: list[str], bet: int) -> int:
        """Calculates using winning logic -> (3+ in row) is multiplied by the bet"""
        max_streak = 1
        current_streak = 1
        winning_symbol = result[0]

        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                current_streak += 1
            else:
                current_streak = 1

            if current_streak > max_streak:
                max_streak = current_streak
                winning_symbol = result[i]

        if max_streak >= 3:
            return self.symbols.get(winning_symbol, 1) * max_streak * bet

        return 0

    def update_coins(self, amount: int) -> None:
        self.coins += amount

    def play(self) -> None:
        print(f"Welcome back, {self.username}!")
        print(f"Starting coins: {self.coins}")
        print("=============================")
        while True:
            try:
                bet: int = int(input("Bet: "))
                self.spin(bet)
            except ValueError:
                print("Please enter a valid number.")


def load_or_create_player(username: str, default_coins: int = 100) -> int:
    """Loads the coins of an existing player or creates a new one with 100 coins."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data: dict[str, int] = json.load(f)
                if username in data:
                    # If a player survived with 0 coins in the previous run, give them a fresh start
                    coins = data[username]
                    return coins if coins > 0 else default_coins
        except json.JSONDecodeError:
            ...

    return default_coins


def main() -> None:
    username: str = input("Enter your username: ").strip().lower().capitalize()
    if not username:
        username = "Player"

    coins: int = load_or_create_player(username)
    game: SlotMachine = SlotMachine(username=username, coins=coins)
    game.save_stats()
    game.play()


if __name__ == "__main__":
    main()
