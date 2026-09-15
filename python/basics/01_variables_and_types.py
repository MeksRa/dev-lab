# Variables
print("Hello, World!") # Greeting the World!
print('Hello' + ' World!')

greeting = 'Hello'
name = input('What\'s your name?\n')
print(greeting + ', ' + name + '!')

# Constants
# Use uppercase letters to indicate that these variables are constants and should not be changed.
PI = 3.14159
VERSION = 2

# Data types
# print(10 + 'hello') # error, you can't add a string and an integer together
# print(10 + 5.5) # => 15.5

# Numeric types:
u_integers = 100 # or -100
u_floats = 10.5 # or -10.5
u_complex = 1j # or -1j
print(u_complex + 1) # => (1+1j) => 'j or J to indicate the imaginary part of a complex number'
print(type(u_floats)) # => <class 'float'>

# Boolean Types:
is_connected = True
is_disconnected = False

# String types: 
u_string = 'Hello, World!'

# Sequence types:
u_list = [1, 2, 3, 4, 5] # can be changed
u_tuple = (2.5, 1.0) # can't be changed
# empty_list, empty_tuple = [], ()

# Mapping types:
u_dictionary = {'name': 'John', 'age': 30}
# empty_dict = {}

# Set types:
u_set = {1, 10, 25, 50} # can't have duplicates
u_frozenset = frozenset({1, 2, 3}) # immutable set, can't be changed
# empty_set = set()
# set.add() / set.remove() / set.discard()

# Dynamically typed language means we can change the type of a variable at runtime.
number = 10
print(number)
print(type(number)) # => <class 'int'>

number = 'ten'
print(number)
print(type(number)) # => <class 'str'>

number: int = 10 # type hint. just annotates the variable with a type, but doesn't enforce it.
text: str = '100'
# number = 'ten' # still valid, but not recommended to change the type of a variable
# after it has been declared with a type hint.

def example_function(x: str) -> str: # -> str: => type hint for the return type of the function
    return x
print(example_function('this function should return a string'))