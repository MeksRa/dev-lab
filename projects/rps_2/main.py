import random


class RPS:
    def __init__(self) -> None:
        print("Welcome to RPS 9000!")
        self.moves: dict = {"rock": "🪨", "paper": "📜", "scissors": "✂️"}
        self.valid_moves: list[str] = list(self.moves.keys())

        self.scoreboard = {"user": 0, "ai": 0}

    def play(self) -> bool:
        """Return False if player types 'exit'"""
        user_move: str = input("Rock, paper, or scissors? >> ").lower()
        if user_move == "exit":
            print("Thanks for playing!")
            # sys.exit()  # bad practice
            return False

        if user_move not in self.valid_moves:
            print("Invalid move... Try again!")
            # return self.play()  # recursive loop  # poosible, but bad practice here
            return True

        ai_move: str = random.choice(self.valid_moves)

        self.printer(user_move, ai_move)
        self.check(user_move, ai_move)
        return True

    def printer(self, user_move: str, ai_move: str) -> None:
        """Only prints game stats"""
        print("----")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")
        print("----")

    def check(self, user_move: str, ai_move: str) -> None:
        """Checks moves"""
        if user_move == ai_move:
            print("It is a tie!")

        elif (
            (user_move == "rock" and ai_move == "scissors")
            or (user_move == "scissors" and ai_move == "paper")
            or (user_move == "paper" and ai_move == "rock")
        ):
            print("You win!")
            self.scoreboard["user"] += 1
        else:
            print("AI wins...")
            self.scoreboard["ai"] += 1
        print(f"🏆 Score is: {self.scoreboard['user']}:{self.scoreboard['ai']}")


def main() -> None:
    """Entry point. Plays RPS if True else break"""
    rps: RPS = RPS()
    while True:
        if not rps.play():
            break


if __name__ == "__main__":
    main()
