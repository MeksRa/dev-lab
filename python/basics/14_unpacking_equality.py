# 01) Unpacking

a, b, c, d = 5, 10, 15, "XY"
f, g = "XY"
r, *k, s = "abcdef"
*_, last = "abcdef"
print(a, d)  # 5 XY
print(f, g)  # X Y
print(r, k, s)  # a ['b', 'c', 'd', 'e'] f
print(last)  # f


def add(a: int, b: int) -> None:
    print(f"{a + b = }")


add(5, 10)  # a + b = 15
numbers: dict[str, int] = {"a": 5, "b": 10}
add(**numbers)  # unpack a dictionary ("a" should be mapped to a; "b" to be)

nums: list[int] = [1, 2, 3, 4, 5]
params: dict[str, str] = {"sep": "-", "end": ".\n"}
print(*nums)  # 1 2 3 4 5
print(*nums, **params)  # 1-2-3-4-5.  # type: ignore

# 02) == VS is

value_1: int = 200
value_2: int = 200

print(value_1 == value_2)  # True
print(value_1 is value_2)  # True  => id(value_1) == id(value_2)
print(id(value_1), "\n", id(value_2))  # identical

value_1: int = 1000
value_2: int = int("1000")

print(value_1 == value_2)  # True
print(value_1 is value_2)  # False  => id(value_1) != id(value_2)
print(id(value_1), "\n", id(value_2))  # different

var: int | None = None
if var is None:
    print("There is no var...")
else:
    print(f"var is: {var}")


class Animal: ...


cat: Animal = Animal()
dog: Animal = Animal()
print(id(cat))  # 1586046338448
print(id(dog))  # 1586046272848
print(cat is dog)  # False
