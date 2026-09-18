# 01) *args

print(1, 2, 3, "hello", sep=":")  # 1:2:3:hello
# default => sep=" "; end="\n"


def add(*args: int) -> int:
    print(args)
    print(type(args))
    return sum(args)


# "*args" absorbs all the values that we pass to "add(1, 2, 3)" and converts it into a tuple
print(add(1, 2, 3))
# (1, 2, 3)
# <class 'tuple'>
# 6


def greet(greeting: str, *people: str, ending: str) -> None:
    for person in people:
        print(f"{greeting}, {person}{ending}")


# "*people" absorbs "Bob", "James", "Maria", and converts it into a tuple
# Everything that comes after *args should have a keyword argument. e.g., ending=""
greet("Hello", "Bob", "James", "Maria", ending="!")

# 02) **kwargs


def pin_position(**kwargs: int) -> None:
    print(kwargs)


# **kwargs absorbs named arguments in pin_position(x=10,y=10) and converts them to a dictionary
pin_position(x=10, y=20)  # {'x': 10, 'y': 20}


# follow the logical order: *args must come before **kwargs, you can't put anything after **kwargs
def order_example(*args: str, default=20, **kwargs: int) -> None:
    print(args)
    print(kwargs)
    print(default)


order_example("a", "b", default=20, a=1, b=2)
# ('a', 'b')  # a tuple
# {'a': 1, 'b': 2}  # a dictionary
# 20

# 03) *&/


def combo_func(var_a: str, /, var_b: str, *, var_c: str) -> None:
    print(var_a)
    print(var_b)
    print(var_c)


# Two ways to call this function
combo_func("a", "b", var_c="c")
combo_func("a", var_b="b", var_c="c")


# 3.1) "/" means that we must use positional-only argument for all the parameters on the left
def func(var_a: str, /, var_b: str) -> None:
    print(var_a)
    print(var_b)


func("a", "b")
func("a", var_b="b")


# def f( [positional-only] / [positional or key])
def func_slash(var_a: str, var_b: str, var_c: str, /) -> None:
    print(var_a)
    print(var_b)
    print(var_c)


func_slash("a", "b", "c")


# 3.2) "*" means that everything after must be keyword arguments only
def func_asterisk(*, var_a: str, var_b: str) -> None:
    print(var_a)
    print(var_b)


func_asterisk(var_a="a", var_b="b")
