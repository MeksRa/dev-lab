import time
from functools import cache


# using cache takes memory
@cache  # a way to speed up func creating and using cache
def count_vowels(text: str) -> int:
    print("Counting...")
    time.sleep(3)  # just a way of simulating an expensive operation...
    return sum(text.count(vowel) for vowel in "AEIOUaeiou")


def main() -> None:
    while True:
        user_input: str = input("You: ").lower()

        if user_input == "info":
            print(f"Bot: {count_vowels.cache_info()}")
            # return to us the info regarding the cache
        elif user_input == "clear":
            count_vowels.cache_clear()
            print("Bot: Cache has been cleared!")
            # clear cache
        else:
            print(f"Bot: That text contains {count_vowels(user_input)} vowels")


if __name__ == "__main__":
    main()

# Output:
# You: Hello World
# Counting...
# Bot: That text contains 3 vowels
# You: Hello World
# Bot: That text contains 3 vowels
# You: hello world
# Bot: That text contains 3 vowels
# You: info
# Bot: CacheInfo(hits=2, misses=1, maxsize=None, currsize=1)
# You: clear
# Bot: Cache has been cleared!
# You: info
# Bot: CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)
# You: hello world
# Counting...
# Bot: That text contains 3 vowels
