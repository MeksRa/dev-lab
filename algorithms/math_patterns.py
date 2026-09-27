# =========================================#

# Nicomachus's triangle
# for row in EVEN -> n^3 + n
# for row in ODD -> n^3
# 1              (1)  # 1^3
# 3 5            (8)  # 2^3
# 7 9 11         (27) # 3^3
# 13 15 17 19    (64) # 4^3
def row_sum_odd_numbers(n: int) -> int:
    return n**3


# =========================================#


# Gauss's formula => S=N(N+1)/2
# 8 => (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) = 36
# 36 = 8*9/2
def summation(num: int) -> int:
    return (1 + num) * num // 2


# =========================================#


# Triangle Inequality Theorem
# a + b > c, a + c > b, b + c > a
def is_triangle(a: int, b: int, c: int) -> bool:
    a, b, c = sorted([a, b, c])
    return a > 0 and a + b > c


print(is_triangle(1, 2, 3))

# =========================================#
