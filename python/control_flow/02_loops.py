import time  # import module for 'time.sleep(5)


# 1) for loop # iterate through a finite / fixed amount of elements
def for_hello():
    text: str = "Hello, world"
    for i in range(3):
        print(f"{i}: {text}")


# for_hello()


def name_expert():
    people: list[str] = ["Bob", "James", "Maria"]
    for person in people:
        if len(person) > 4:
            print(f"{person} has a long name")
        else:
            print(f"{person} has a short name")


# name_expert()


# 2) while loop # an infinite loop
# while True:
#    print("W'z")  # infinite loop
def while_hello():
    i: int = 5
    while i > 0:
        print(f"Hello: {i}")
        i -= 1


# while_hello()


def sleepy_program():
    connected: bool = True
    while connected:
        print("Using internet...")
        time.sleep(5)  # makes our program sleep for 5 seconds
        connected = False
    print("Connection ended...")


# sleepy_program()


def endless_chatbot():
    while True:
        user_input: str = input("You: ")
        if user_input == "Hello":
            print("Bot: Hey there!")
        else:
            print("Bot: Yes, that is interesting")


# endless_chatbot()


# 3) break and continue
number: int = 5


def break_example(number: int):
    while number > 0:
        number -= 1
        if number == 2:
            print("Break at 2")
            break  # tells python that it's the time to exit the loop (ends the loop)
        print(number)
    print("Done!")


# break_example(number)

# 4
# 3
# Break at 2
# Done!


def continue_example(number: int):
    while number > 0:
        number -= 1
        if number == 2:
            print("Skipping 2")
            continue  # skips the end of this iteration and moves on to the next iteration
        print(number)  # ignores only this line when number == 2
    print("Done!")


# continue_example(number)

# 4
# 3
# Skipping 2
# 1
# 0
# Done!


def calc_add():
    total: int = 0
    print('Welcome to Calc+! Add positive numbers, or insert "0" to exit.')
    while True:
        user_input: int = int(input("Enter a number: "))
        if user_input < 0:
            print("!!!Please enter positive numbers only!!!")
            continue
        if user_input == 0:
            print(f"Total: {total}")
            break
        total += user_input  # if user_input < 0 then ignores this line


# calc_add()


# 4) loop + else (special syntax)
for i in range(3):
    print(f"Iteration: {i}")
    break  # Success block won't be reached, thanks to 'break'
else:  # Success block (this block only executes if all the iterations were successful)
    print("Success!")
# result: Iteration: 0

i: int = 3
while i > 0:
    i -= 1
    print("OK")
    break  # Success block won't be reached 'cause not all iterations were successful
else:  # Success block
    print("Success!")
# OK
