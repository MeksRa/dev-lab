import asyncio
from asyncio import Task
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int) -> dict:
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
    # task: Task[dict] = asyncio.create_task(fetch_data(1, delay=3))
    # await asyncio.sleep(1)
    # print("Running other code...")
    # data: dict = await task
    # print(data)

    # Output:
    # Fetching data...
    # Running other code...
    # Data retrieved!
    # {'input': 1, 'start_time': '01:22:45', 'end_time': '01:22:48'}

    # =================

    # task1: Task[dict] = asyncio.create_task(fetch_data(2, delay=10))
    # await asyncio.sleep(1)
    # task1.cancel(msg="Took too long...")
    # await asyncio.sleep(1)
    # print(task1.cancelled())

    # Output:
    # Fetching data...
    # True

    # =================

    # task2: Task[dict] = asyncio.create_task(fetch_data(2, delay=10))
    # await asyncio.sleep(1)
    # task2.cancel(msg="Took too long...")

    # try:
    #     data: dict = await task2
    #     print(data)
    # except asyncio.CancelledError as e:
    #     print("Task was cancelled...")
    #     print(e)
    #     print(task2.cancelled())

    # Output:
    # Fetching data...
    # Task was cancelled...
    # Took too long...
    # True

    # =================

    # task3: Task[dict] = asyncio.create_task(fetch_data(3, delay=3))
    # await asyncio.sleep(1)  # change .sleep(1) to .sleep(4) and you'll get result

    # try:
    #     data: dict = task3.result()
    #     print(data)
    # except asyncio.InvalidStateError as e:
    #     print(e)

    # Output:
    # Fetching data...
    # Result is not set.

    # =================

    # task4: Task[dict] = asyncio.create_task(fetch_data(3, delay=3))
    # print(task4.done())
    # data: dict = await task4
    # print(data)
    # print(task4.done())

    # Output:
    # False
    # Fetching data...
    # Data retrieved!
    # {'input': 3, 'start_time': '01:39:10', 'end_time': '01:39:13'}
    # True
    #
    # - - - - - - - - -
    # if task5.done():
    # data = task5.result()
    # - - - - - - - - -
    # =================

    task5: Task[dict] = asyncio.create_task(fetch_data(5, delay=30))
    try:
        data: dict = await asyncio.wait_for(task5, timeout=3)
        print(data)
    except asyncio.TimeoutError:
        print("Request too long...")

    # Output:
    # Fetching data...
    # Request too long...


if __name__ == "__main__":
    asyncio.run(main=main())
