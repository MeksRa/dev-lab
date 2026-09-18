user_input: str = "10"
try:
    result: float = 1 / float(user_input)
    print(f"1 / {user_input} = {result}")
except ValueError:
    print(f'You cannot use: "{user_input}" as a value')
except ZeroDivisionError:
    print("Don't be silly, you cannot divide by 0.")
else:  # rarely used block, not recommended
    # This block will only run if the 'try' block executed successfully without exceptions
    print("Success! There were no exceptions encountered!")
finally:  # Always executes, regardless of the user inputs, any exceptions
    print("Finally: I'm always executed!")
