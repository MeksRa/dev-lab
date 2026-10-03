# ============================================ #
#
# mypy analyzes the project for errors
# Pylance for code highlighting, Mypy for a full analysis before pushing to GitHub.
#
# >> mypy python/advanced/01_mypy.py
#
# python\advanced\01_mypy.py:4: error: List item 2 has incompatible type "bool"; expected "str"  [list-item]
# python\advanced\01_mypy.py:4: error: List item 3 has incompatible type "list[int]"; expected "str"  [list-item]
# python\advanced\01_mypy.py:10: error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"  [arg-type]
# Found 3 errors in 1 file (checked 1 source file)
#
# --- example of code with an error
# items: list[str] = ["cup", "apple", True, [1, 2, 3]]
# def add_numbers(a: int, b: int) -> int:
#    return a + b
# result = add_numbers(10, "hello")
# ---
#
# ============================================ #
