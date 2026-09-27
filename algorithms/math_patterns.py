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


def fibonacci(signature: list[int], n: int) -> list[int]:
    if n < len(signature):
        return signature[:n]

    result = signature.copy()
    while len(result) < n:
        result.append(sum(result[-2:]))

    return result


def tribonacci(signature: list[int], n: int) -> list[int]:
    if n < len(signature):
        return signature[:n]

    result = signature.copy()
    while len(result) < n:
        result.append(sum(result[-3:]))

    return result


def xbonacci(signature: list[int], n: int) -> list[int]:
    if n < len(signature):
        return signature[:n]

    result = signature.copy()
    window_size = len(signature)

    while len(result) < n:
        result.append(sum(result[-window_size:]))

    return result


print(fibonacci([0, 1], 10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(tribonacci([1, 1, 1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(xbonacci([0, 0, 0, 1], 10))  # [0, 0, 0, 1, 1, 2, 4, 8, 15, 29]

# =========================================#
