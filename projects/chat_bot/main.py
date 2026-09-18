from datetime import datetime


def get_username() -> str:
    print("Bot: Hmm. What's your name, stranger?")
    name: str = input("You: ").strip() or "Stranger"
    return name


def get_response(text: str, name: str) -> str:
    lowered: str = text.lower()  # "Hello" => "hello"
    if lowered in ["hello", "hi", "hey"]:
        return f"Hey there, {name}!"
    elif "how are you" in lowered:
        return f"I'm good thanks, {name}!"
    elif "your name" in lowered:
        return "My name is: Bot :)"
    elif "time" in lowered:
        current_time: datetime = datetime.now().astimezone()
        return f"The time is: {current_time:%H:%M}"
    elif lowered in ["bye", "see you", "goodbye"]:
        return f"It was nice talking to you, {name}! Bye!"
    else:
        return f"Sorry, {name}! I do not understand: {text}"


def main() -> None:
    username: str | None = None

    while True:
        if username is None:
            username = get_username()
        user_input: str = input(f"{username}: ")
        if user_input.lower() == "exit":
            print("Bot: It was a pleasure talking to you!")
            break
        bot_response: str = get_response(user_input, username)
        print(f"Bot: {bot_response}")


if __name__ == "__main__":
    main()
