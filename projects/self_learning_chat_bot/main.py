import json
from difflib import get_close_matches
from pathlib import Path

# Path to the knowledge base file (stored next to the main.py)
BASE_DIR: Path = Path(__file__).resolve().parent
BRAIN_FILE: Path = BASE_DIR / "brain.json"


def load_brain(file_path: Path) -> dict:
    """Loads the knowledge base from a JSON file.
    If the file does not exist, it creates one with default data."""

    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Default knowledge base on first launch
        initial_brain = {
            "hello": "Hey there!",
            "how are you": "I am good, thanks!",
            "what time is it": "Don't know, don't care...",
        }
        save_brain(file_path, initial_brain)
        return initial_brain


def save_brain(file_path: Path, knowledge: dict) -> None:
    """Saves the current knowledge base to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, ensure_ascii=False, indent=4)


def get_best_match(user_question: str, knowledge: dict) -> str | None:
    """Searches for the most similar question in the knowledge base using fuzzy search."""
    questions: list[str] = [q for q in knowledge]
    # n=1 -> return 1 the best option  # cutoff -> similarity level 0.6=60%
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    print("Bot: Hello! I'm ready to chat. (Type 'quit', 'exit' or 'bye' to stop)")

    while True:
        user_input: str = input("You: ")

        # Skip empty input.
        if not user_input:
            continue

        # Perform a safe exit before searching the dictionary.
        if user_input.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye! Have a nice day!")
            break

        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f"Bot: {answer}")
        else:
            print("Bot: I do not have the answer...")
            new_answer: str = input(
                "Bot: Teach me, what should I say? (or type 'skip' to skip): "
            ).strip()

            if new_answer.lower() != "skip" and new_answer:
                # Adding a new question and answer to the dictionary.
                knowledge[user_input.lower()] = new_answer
                # Save the updated database to a JSON file.
                save_brain(BRAIN_FILE, knowledge)
                print("Bot: Thank you! I have learned something new today!")


def main() -> None:
    """Load the bot's memory from a file at startup"""
    brain: dict = load_brain(BRAIN_FILE)

    chat_bot(knowledge=brain)


if __name__ == "__main__":
    main()
