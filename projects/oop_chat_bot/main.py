from datetime import datetime
from random import choice


class ChatBot:
    # we want to customize => we need initializer
    def __init__(self, name: str, age: int) -> None:
        self.name = name  # instance attributes
        self.age = age

    def get_description(self) -> str:  # method
        return f"{self.name} is a bot who is {self.age} years old."

    def get_response(self, text: str) -> str:  # method
        lowered: str = text.lower()
        if "hello" in lowered:
            return f"{self.name}: Hey there!"
        elif "bye" in lowered:
            return f"{self.name}: Bye there!"
        elif "how old are you" in lowered:
            return f"{self.name}: I am {self.age} years.old!"
        elif "what time is it" in lowered:
            now: datetime = datetime.now().astimezone()
            return f"{self.name}: The current time is {now:%H:%M:%S}"
        elif "how are you" in lowered:
            return f"{self.name}: Great, thanks!"
        else:
            random_responses: list[str] = [
                "I don't understand...",
                "Would you mind rephrasing that?",
                "What?",
                "Ah, What?",
            ]
            return f"{self.name}: {choice(random_responses)}"

    def run(self) -> None:
        while True:
            user_input: str = input("You: ")
            if user_input == "exit":
                print(f"Thank you for chatting with {self.name}!")
                break
            response: str = self.get_response(user_input)
            print(response)


def main() -> None:
    mario: ChatBot = ChatBot("Mario", 27)
    print(mario.get_description())
    mario.run()


if __name__ == "__main__":
    main()
