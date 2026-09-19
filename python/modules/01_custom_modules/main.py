# 01)
# import greetings as g

# g.greet("Mario")  # Hello, Mario!
# print(g.AUTHOR)  # Federico

# 02)
# from greetings import greet

# greet("Mario")  # Hello, Mario!

# 03)
# from greetings import *  # import everything

# greet("Luigi")
# print(AUTHOR)
# print(VERSION)

# 04) Bad practice! It's dangerous to import everything from module, 'cause it'll override other modules
# from my_time import *  # These two modules overlap
# from time import *  # An example of why it's better not to use * if u don't need everything

# print(date())
# print(time())

# 05)
import connections


# connections.connect()
def main() -> None:
    connections.connect()


if __name__ == "__main__":  # checks if we run script directly
    main()
