def greet(name: str, language: str, default: str = "Hello"):
    # name, language, default - parameters # 'default' => we defined the value
    if language == "it":  # italian))
        print(f"Ciao, {name}!")
    else:
        print(f"{default}, {name}!")


greet(name="Mario", language="it")  # Mario, it, Hello - arguments
# You can put parameters="arguments" in any order you want, they will work properly.
greet("Mario", language="it")
# argument without parameter you should put at the beggining to avoid a SyntaxError
greet("Mario", language="it", default="Hola")
# we can redefine the value of the parameter
