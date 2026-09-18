# Arguments / Parameters
def greet(name: str, language: str, default: str = "Hello"):
    # name, language, default - parameters # 'default' => we defined the argument
    if language == "it":  # italian))
        print(f"Ciao, {name}!")
    else:
        print(f"{default}, {name}!")


greet(name="Mario", language="it")  # Mario, it, Hello - arguments
# You can put parameters="arguments" in any order you want, they will work properly.
greet("Mario", language="it")
# argument without parameter you should put at the beggining to avoid a SyntaxError
greet("Mario", language="it", default="Hola")
# we can redefine the argument of the parameter


# Return functions
def get_length(text: str) -> int:  # "-> int" annotated return type
    print(f'Getting the length of: "{text}"...')
    return len(text)


name: str = "Mario"
length: int = get_length(name)
print(length)


def make_upper(text: str) -> str:
    return text.upper()


print(make_upper("hello"))


# Connects to internet and returns nothing
def connect_to_internet() -> None:  # such functions return "None" by default
    print("Connecting to internet...")
    # return None  # this is redundant


print(connect_to_internet())  # None
