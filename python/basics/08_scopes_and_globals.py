# 01) Scopes

# Try not to have things out in the global scope, it just becomes very messy

number: int = 999  # global / outer scope/ outermost layer of this script


# create a new function => create a new scope (won't be visible to the outer layer)
def change_number() -> None:
    number = 10  # inner / local scope
    var = "a"

    # Everything in the outer layer will always be visible to what's inside the inner layer

    def inner() -> None:  # inner function
        first_inner = 5
        print(number, var)  # You're able to use previous local vars
        # print(second_inner) ==> You can't use it

        def second_inner() -> None:
            print(number, var)
            second_inner = 4
            print(first_inner)
            print(second_inner)


change_number()  # nothing has changed as you can see..
print(number)  # 999 # number from global/outer scope, as you see.


def print_number() -> None:
    print(number)


print_number()  # 999

# 02) Globals

text: str = "A"


# When you create a local scope make sure that your variables are not shadowing ones from outer
def change_text() -> None:
    global text  # refer a local variable to the global scope
    text = "B"

    def inner_changer() -> None:
        global text
        text = "C"

    inner_changer()


print(text)  # A
change_text()
print(text)  # C

# 03) Nonlocals


def outer_func() -> None:
    name: str = ""
    value: int = 0

    def inner_func() -> None:
        # saying that these are not local variables, these vars are grabbing the values from different scope
        nonlocal value, name  # nonlocal => Searches until the first match, does not go to the global
        name = "Tom"
        value = 100

    inner_func()
    print(name, value)


outer_func()  # Tom 100


def level_1():
    count = 1  # <= nonlocal from level_3 will change only this var!

    def level_2():
        # There are no variables named "count" here

        def level_3():
            nonlocal count
            count = 999  # Found count in level_1 and overwrote it.

        level_3()

    level_2()
    print(count)  # 999


level_1()
