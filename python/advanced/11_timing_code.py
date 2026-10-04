from timeit import repeat, timeit

a: str = "list(range(1000))"
b: str = "set(range(1000))"

warmup: float = timeit(stmt=a, number=100_000)  # for more accurate results
a_time: float = timeit(stmt=a, number=100_000)
b_time: float = timeit(stmt=b, number=100_000)

print(f"a: {a_time:.3f}s")  # a: 1.113s
print(f"b: {b_time:.3f}s")  # b: 1.856s

# ---------------------------------------

a: str = "list(range(1000))"
b: str = "list(range(1000))"
c: str = "set(range(1000))"

# a_time: list[float] = repeat(stmt=a, repeat=5, number=100_000)
# print(f"without min() -> {a_time}")
# without min() -> [1.1056277999887243, 1.0552639999659732, 0.9764941000030376, 0.9360116999596357, 0.9201239999965765]

a_time: float = min(repeat(stmt=a, repeat=5, number=100_000))
b_time: float = min(repeat(stmt=b, repeat=5, number=100_000))
c_time: float = min(repeat(stmt=c, repeat=5, number=100_000))

print(f"a: {a_time:.3f}s")  # a: 0.986s
print(f"b: {b_time:.3f}s")  # b: 0.964s
print(f"c: {c_time:.3f}s")  # c: 1.732s

# ---------------------------------------

power_time: float = timeit("a**b", setup="a, b = 10, 3")  # 1 million times by default
print(f"a**b: {power_time:.3f}s")  # a**b: 0.029s

math_power_time: float = timeit(stmt="math.pow(10, 3)", setup="import math")
print(f"math.pow: {math_power_time:.3f}s")  # math.pow: 0.085s
math_power_time: float = timeit(stmt="pow(10, 3)", setup="from math import pow")
print(f"math.pow: {math_power_time:.3f}s")  # math.pow: 0.084s

setup: str = """
import math

a: int = 10
b: int = 3
"""

math_power_time: float = timeit(stmt="math.pow(a, b)", setup=setup)
print(f"math.pow: {math_power_time:.3f}s")  # math.pow: 0.089s

# ---------------------------------------
