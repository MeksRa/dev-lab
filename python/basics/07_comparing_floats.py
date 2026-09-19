from math import isclose

a: float = 0.1 + 0.2
b: float = 0.3

print(f".1 + .2 == {b}?")
print(f"{a} == {b}.=>", a == b)  # 0.30000000000000004 == 0.3? False
print(f"{a} == {b}. =>", isclose(a, b, rel_tol=0.001))  # 0.30000000000000004 == 0.3 True

a: float = 0.999
b: float = 1.000

# print(f"{a} == {b}?", a == b)  # 0.999 == 1.0? False
# (abs_tol) gives us an absolute tolerance, it must be in the range to be considered the same
# print(f"{a} == {b}?", isclose(a, b, abs_tol=0.002))  # 0.999 == 1.0? True

# (rel_tol) as long as the numbers are not more than 1% different, they'll always be considered equal
# print(f"{a} == {b}?", isclose(a, b, rel_tol=0.01))  # 0.999 == 1.0? True
