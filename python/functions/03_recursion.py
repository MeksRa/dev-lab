# Usually the best way to explain the concept of recursion
# is by putting a mirror in fron of another mirror.
# => What you get in the end is a reflection that reflects
# the same reflection back and forth
# and what appears to be an infinite cycle.
import time


def func() -> None:  # There is an RecursionError at the end
    print("Recursion")
    func()


# func()


def connect_to_internet(signal: bool, delay: int) -> None:
    if delay > 5:
        signal = True
    if signal:  # == True
        print("Connected!")
    else:
        print(f"Connection failed. Trying again in: {delay}s...")
        time.sleep(delay)
        connect_to_internet(signal, delay + 2)


connect_to_internet(False, 0)
