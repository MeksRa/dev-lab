import time


def connect() -> None:
    print("Connecting to internet...")
    time.sleep(1)
    print("Connected!!!")


def main() -> None:
    connect()


if __name__ == "__main__":  # checks if we run script directly
    main()

# The module __name__ == "__main__" and func def main() needs here ONLY FOR isolated tests
# Since the "connections" is an auxiliary module..
