file_path: str = "output/info.txt"

# 01) Read ------------------------

# with open(file_path) as f:  # "r" - default
with open(file_path, "r") as f:  # more clear, readable
    # --- --- Read

    # 'read' is exhaustive, once we read it disappears (similar to generators)

    # print(f"1: {f.read()}")  # 1: This is some info
                               # Hi, Bob!
    # print(f"2: {f.read()}")  # 2:

    # --- --- Read bytes

    # print(f.read(5))  # read first 5 bytes
    # print(f.read(5))  # read next 5 bytes
    # print(f.read())   # read the rest

    # --- --- Read line

    # print(f.readline())  # This is some info
    # print(f.readline(), end="")   # use it if u wanna remove "\n" at the end
    # print(f.readline(5), end="")  # first 5 bytes
    # print(f.readline(), end="")  # read the rest

    # --- --- Read lines

    # print(f.readlines())  # ['This is some info\n', 'Hi, Bob!']

    # --- --- Use variables

    # so we can store data from a file
    text: str = f.read()
    print(f"1: {text}")  # 1: This is some info
                         # Hi, Bob!
    print(f"2: {text}")  # 2: This is some info
                         # Hi, Bob!
    print(f"3: {text}")  # 3: This is some info
                         # Hi, Bob!


# 02) Append ------------------------

# "a" appending.
with open(file_path, "a") as txt:
    txt.write("I am some text!\n")
    txt.writelines(["Eggs\n", "Ham\n", "Spam\n"])

with open("output/test.txt", "a") as txt:  # Creates a new file if it doesn't exist
    txt.write("Some text\n")


# 03) Write ------------------------

# "w" cleans the whole file and overwrites it
with open(file_path, "w") as txt:
    txt.write("Hello, Bob!")