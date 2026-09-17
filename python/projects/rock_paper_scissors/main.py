import random
import sys

# Step 1: Starting information
print("Welcome to RPS!")
moves: dict = {"rock": "🪨", "paper": ".📜", "scissors": "✂️"}
valid_moves: list[str] = list(moves.keys())
scoreboard = {"user": 0, "ai": 0}

# Step 2: Infinite loop
while True:
    user_move: str = input("Rock, paper, or scissors? >> ").lower()  # Rock,ROCK => rock
    if user_move == "exit":
        print("Thanks for playing")
        sys.exit()  # use sys.exit() in real projects, instead of exit(), quit()
    if user_move not in valid_moves:
        print("Invalid move...")
        continue

    # AI decides
    ai_move: str = random.choice(valid_moves)

    print("----")
    print(f"You: {moves[user_move]}")
    print(f"AI: {moves[ai_move]}")
    print("----")

    # Check moves
    if user_move == ai_move:
        print("It is a tie!")
    elif (
        (user_move == "rock" and ai_move == "scissors")
        or (user_move == "scissors" and ai_move == "paper")
        or (user_move == "paper" and ai_move == "rock")
    ):
        print("You win!")
        scoreboard["user"] += 1
    else:
        print("AI wins...")
        scoreboard["ai"] += 1
    print(f"🏆 Score is: {scoreboard['user']}:{scoreboard['ai']}")