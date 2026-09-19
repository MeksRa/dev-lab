numbers: list[int] = [1, 2, 3, 4, 5, 6]
# forward
print(numbers[0:3])  # [1, 2, 3] # => from 0 to 2.
print(numbers[:3])  # [1, 2, 3] # => it grabs everything up until 3.
print(numbers[3:])  # [4, 5, 6] # => it grabs everything from 3 onwards
print(numbers[:3] + numbers[3:])  # [1, 2, 3, 4, 5, 6] # => returns original list back.
print(numbers[3:6])  # [4, 5, 6] # => from 3 to 5.
print(numbers[2:4])  # [3, 4]    # => from 2 to 3.

# backward
print(numbers[-1])  # 6 # => to get the last element from a list
print(numbers[-2])  # 5 # => it would go two steps back

# step
print(numbers[0:4:2])  # [1, 3] # => [from:to:step] => from 0 to 3 step 2 (forward)
print(numbers[4:0:-2])  # [5, 3] # => from 4 to 1 step -2 (backward)
print(numbers[::2])  # [1, 3, 5] # from 0 to the end, step 2 (forward)

# reverse
print(numbers[::-1])  # [6, 5, 4, 3, 2, 1] # => reversed list

name: str = "Mario"
print(name[::-1])  # oiraM # => reversed string
