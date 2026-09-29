from difflib import get_close_matches


class ChatBot:
    def __init__(self, knowledge: dict[str, str]) -> None:
        self.knowledge = knowledge

    def _get_best_match(self, user_question: str) -> str | None:
        questions: list[str] = list(
            self.knowledge.keys()
        )  # [q for q in self.knowledge]
        matches: list[str] = get_close_matches(
            user_question, questions, n=1, cutoff=0.6
        )

        if matches:
            return matches[0]
        return None

    def get_response(self, user_input: str) -> str:
        best_match: str | None = self._get_best_match(user_input)

        if best_match:
            return self.knowledge[best_match]
        else:
            return "I do not understand"


def main() -> None:
    brain: dict[str, str] = {
        "hello": "Hey there!",
        "how are you?": "I'm good, thanks!",
        "do you know what the time is?": "Not at all!",
        "what time is it?": "No clue!",
        "what can you do?": "I can answer questions!",
        "ok": "Great.",
    }
    chatbot1: ChatBot = ChatBot(brain)

    while True:
        user_input: str = input("You: ")
        response: str = chatbot1.get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
