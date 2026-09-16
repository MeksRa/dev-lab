# + addition
# - subtraction
# * multiplication
# / division
# // floor divison
# % modulo
# **exponentiation


def integers():
    a: int = 5
    b: int = 10
    print(a + b)  # => 15
    print(a - b)  # => -5
    print(a * b)  # => 50
    print(type(a / b), a / b)  # => <class 'float'> 0.5


def floats():
    a: float = 0.5
    b: float = 1.5
    print(a + b)  # => 2.0
    print(a - b)  # => -1.0
    print(a * b)  # => 0.75
    print(type(a / b), a / b)  # => <class 'float'> 0.3333333333333333


def floor_division():
    a: int = 17
    b: int = 5
    c: int = 10
    print(a // b)  # => 3 (5 * '3' + 2)
    print(a // c)  # => 1 (10 * '1' + 7)


def modulo_division():
    a: int = 17
    b: int = 5
    c: int = 10
    print(a % b)  # => 2 (5 * 3 + '2') => remainder of the division
    print(a % c)  # => 7 (10 * 1 + '7')
    print(10 % 2)  # 0 => even number
    print(5 % 2)  # 1 => odd number


def exponentiation():
    a: int = 2
    b: int = 3
    print(a**b)  # 8 => (2^3)
    print(9 ** (1 / 2))  # 3.0 (square root)


def augmented_assignment():
    x = 2
    x += 2  # 4 => x = x + 2
    x -= 2  # 0 => x = x - 2
    x *= 2  # 4 => x = x * 2
    x /= 2  # 1 => x = x / 2
    x //= 2  # 1 => x = x // 2
    x %= 2  # 0 => x = x % 2
    x **= 2  # 4 => x = x**2


def built_in_math_helpers():
    negative_val: int = -15
    float_val: float = 3.14159
    print(abs(negative_val))  # 15 =>(absolute val)
    print(round(float_val, 2))  # 3.14 => (round to 2 decimal places)
    print(pow(2, 3))  # 8 => (alternative to 2**3)


def boolean_logic():
    a: int = 1
    b: int = 5
    c: int = 10
    d: int = 10
    print(a == b)  # False
    print(c == d)  # True  (C is equal to D) => True
    print(c != d)  # False (C is not equal to D => False)
    print(a != d)  # True
    print(b > a)  # True
    print(c >= d)  # True
    print(c > b > a)  # True
    print(c == d and b > a)  # True and True => True
    print(c == a or b > a)  # False or True => True
    print(not (a > b))  # not False => True

    ## == (Equality) - compare values.
    # is (Identity) - compare id()
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(list1 == list2)  # True
    print(list1 is list2)  # False
    print(id(list1) == id(list2))  # False
    # if result is None:
    #   ...


# integers()
# floats()
# floor_division()
# modulo_division()
# exponentiation()
# augmented_assignment()
# built_in_math_helpers()
# boolean_logic()
