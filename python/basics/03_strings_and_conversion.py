name: str = "Mario"  # 'Mario\'s'
fruit: str = "Banana"  # "Banana's" # "Quote: \"Hello there\""
print(name + " eats a " + fruit)  # => string concatenation

poem: str = """We have the freedom
to write whatever we want
on as many lines as we want.
You can also use ''' here
insted of \"\"\"."""
print(poem)

txt_value: str = "100"
int_value: int = 50
print(int(txt_value) + int_value)
# int(), str(), float() ... it has to be a compatible value
