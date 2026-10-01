# 111-112

# call func1(delay=2)
# call func2(delay=1)
# func2() has finished
# func1() has finished
# ==========================

import asyncio
from asyncio import Task
from datetime import datetime


async def fetch_data(input_data: int) -> dict:
    print("Fetching data...")
    start_time: datetime = datetime.now().astimezone()
    await asyncio.sleep(3)
    # "await" tells to wait for this line of code to complete before moving on
    end_time: datetime = datetime.now().astimezone()
    print("Data retrieved!")

    return {
        "input": input_data,
        "start_time": f"{start_time:%H:%M:%S}",
        "end_time": f"{end_time:%H:%M:%S}",
    }


async def main() -> None:

    # Example: 1  [SYNC]  3 + 3 = 6 sec
    data1: dict = await fetch_data(1)
    data2: dict = await fetch_data(2)

    print(f"{data1=}")
    print(f"{data2=}")
    # Fetching data...
    # Data retrieved!
    # Fetching data...
    # Data retrieved!
    # data1={'input': 1, 'start_time': '01:03:12', 'end_time': '01:03:15'}
    # data2={'input': 2, 'start_time': '01:03:15', 'end_time': '01:03:18'}

    # Example: 2  [ASYNC]  3 sec
    task1: Task[dict] = asyncio.create_task(fetch_data(1))
    task2: Task[dict] = asyncio.create_task(fetch_data(2))

    data1: dict = await task1
    data2: dict = await task2

    print(f"{data1=}")
    print(f"{data2=}")

    # Fetching data...
    # Fetching data...
    # Data retrieved!
    # Data retrieved!
    # data1={'input': 1, 'start_time': '01:09:20', 'end_time': '01:09:23'}
    # data2={'input': 2, 'start_time': '01:09:20', 'end_time': '01:09:23'}

    # ================================


if __name__ == "__main__":
    asyncio.run(main=main())
