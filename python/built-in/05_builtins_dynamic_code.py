# Always use exec and eval with caution!

# ==============
# 01) eval()  | evaluates the code, accepts expressions
# ==============
x: int = 5
y: int = 10

result: int = eval("1 + 10 + 100")
print(result)  # 111
print(eval("x + y"))  # 15


# Useful for simple calculators, but can be very dangerous in real code.
# People can inject their code through this eval()
def example_calc():
    while True:
        user_input: str = input("Enter math: ")
        print(eval(user_input))


# example_calc()


# ==============
# 02) exec()  | doesn't return anything, only executes EVERYTHING
# ==============

code: str = """
x: int = 10
y: int = 20

print(x + y)
print("Hello, world!")

for i in range(3):
    print(i)

"""

# exec(code)


def example_func():
    while True:
        user_input: str = input("Command: ")
        exec(user_input)  # noqa: S102


# example_func()
