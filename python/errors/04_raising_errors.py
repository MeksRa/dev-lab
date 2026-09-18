def check_age(age: int) -> bool:
    if age < 0:
        raise ValueError("Not a valid age...")  # a message isn't necessary but useful
    elif age >= 21:
        print("You are old enough!")
        return True
    else:
        print("You are not old enough...")
        return False


# check_age(-10)

raise Exception("This is a general exception.")  # noqa: TRY002
