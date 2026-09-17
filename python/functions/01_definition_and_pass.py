# The two most important things - Readability and Reusability
import time
from datetime import datetime


def show_time():
    now: datetime = datetime.now().astimezone()
    print(f"Time: {now:%H:%M:%S}")


show_time()
time.sleep(2)
show_time()


# pass => just a placeholder
def get_status():
    pass  # doesn't do anything here


def connect_to_internet():
    pass  # if you don't have any code for this yet, use "pass" as a placeholder


number: int = 2
if number > 0:
    pass
else:
    pass  # does nothing, but allows to continue programming without any problems

for i in range(3):
    pass


def connect(): ...  # Absolutely the same as "pass", but stay consistent - use only one of them
