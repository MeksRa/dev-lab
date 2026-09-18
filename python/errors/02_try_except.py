import sys

# 01) Try, except

# try:  # block for dangerous code
#    ...
# except:  # block for solving that code
#    ...


def first_try_except_example():
    try:
        result: float = 10 / 0
        print(result)
    except ZeroDivisionError as e:  # "as e:" only if you want to get info about error
        print(f"Error: {e}")
    print("Done!")

    while True:
        try:
            user_input: str = input("Enter a number: ")
            print(f"10 / {user_input} = {10 / float(user_input)}")
        except ZeroDivisionError:  # try to be as specific as you can
            print("You cannot divide by 0")
        except ValueError:  # and use "except Exception" only as a last resort
            print("Please enter a valid number...")
        except Exception as e:  # noqa: BLE001
            # "except Exception" covers everything, isn't recommended
            print(f"Something else went wrong: {e}")


# first_try_except_example()


def second_try_except_example():
    total: float = 0
    while True:
        user_input: str = input("Enter a number: ")
        if user_input == "0":
            print(f"Total: {total}")
            sys.exit()
        try:
            total += float(user_input)  # dangerous operation
        except ValueError:
            print("Please enter a valid number...")


# second_try_except_example()

# 02) Unknown errors

while True:
    user_input: str = input("Enter a number: ")
    try:
        number: float = float(user_input)
        print(f"You entered: {number}")
        # 2) Use this when you've already sure about the type of error
    except ValueError:
        print(f'The value you entered ("{user_input}") is invalid.')
        # 1) Use this when you're unsure which error might occur
    except Exception as e:  # noqa: BLE001
        print("Program encountered a new exception!")
        print(f"Type: {type(e)}")
        print(f"Error: {e}")
