import asyncio
from asyncio import Future
from datetime import datetime

import requests
from requests import Response


async def check_status(url: str) -> dict[str, int | str]:
    start_time: datetime = datetime.now().astimezone()
    response: Response = await asyncio.to_thread(requests.get, url, None)
    end_time: datetime = datetime.now().astimezone()

    return {
        "website": url,
        "status": response.status_code,
        "start_time": f"{start_time:%H:%M:%S}",
        "end_time": f"{end_time:%H:%M:%S}",
    }


async def main() -> None:
    print("Fetching results...")

    tasks: Future = asyncio.gather(
        check_status("https://google.com"),
        check_status("https://youtube.com"),
        check_status("https://github.com"),
        check_status("https://Indently.io"),
        check_status("https:lol"),
        return_exceptions=True,
    )

    results: list[dict] = await tasks

    for result in results:
        print(result)


# Output:
# Fetching results...
# {'website': 'https://google.com', 'status': 200, 'start_time': '02:25:25', 'end_time': '02:25:25'}
# {'website': 'https://youtube.com', 'status': 200, 'start_time': '02:25:25', 'end_time': '02:25:26'}
# {'website': 'https://github.com', 'status': 200, 'start_time': '02:25:25', 'end_time': '02:25:25'}
# {'website': 'https://Indently.io', 'status': 200, 'start_time': '02:25:25', 'end_time': '02:25:26'}
# Invalid URL 'https:lol': No host supplied

if __name__ == "__main__":
    asyncio.run(main=main())
