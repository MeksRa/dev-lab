import asyncio
from asyncio import Future  # , Task
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int, fails: bool) -> dict:
    print("Fetching data...")

    start_time: datetime = datetime.now().astimezone()
    await asyncio.sleep(3)
    # "await" tells to wait for this line of code to complete before moving on
    end_time: datetime = datetime.now().astimezone()

    if fails:
        raise Exception("Something went wrong...")  # noqa: TRY002

    print("Data retrieved!")
    return {
        "input": input_data,
        "start_time": f"{start_time:%H:%M:%S}",
        "end_time": f"{end_time:%H:%M:%S}",
    }


async def main() -> None:
    # we can put as many coroutines into ".gather()" as we want
    # "Future" represents eventual result of async operations
    tasks: Future[tuple] = asyncio.gather(
        fetch_data(1, delay=1, fails=False),
        fetch_data(2, delay=2, fails=False),
        fetch_data(3, delay=1, fails=True),
        return_exceptions=True,
    )

    results: tuple = await tasks
    for result in results:
        print(result)

    # Output:
    # Fetching data...
    # Fetching data...
    # Fetching data...
    # Data retrieved!
    # Data retrieved!
    # {'input': 1, 'start_time': '02:07:03', 'end_time': '02:07:06'}
    # {'input': 2, 'start_time': '02:07:03', 'end_time': '02:07:06'}
    # Something went wrong...


if __name__ == "__main__":
    asyncio.run(main=main())
