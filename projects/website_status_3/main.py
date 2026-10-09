import asyncio
import csv
from http import HTTPStatus
from pathlib import Path

import httpx
from fake_useragent import UserAgent


def get_websites(csv_path: Path) -> list[str]:
    websites: list[str] = []

    with csv_path.open("r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            url = row[1]

            if url.startswith(("https://", "http://")):
                websites.append(url)
            else:
                websites.append(f"https://{url}")

    return websites


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int) -> str:
    try:
        status = HTTPStatus(status_code)
        return f"({status.value} {status.name}) {status.description}"
    except ValueError:
        return '("???") Unknown status code...'


async def check_website(client: httpx.AsyncClient, website: str, user_agent) -> None:
    headers = {"User-Agent": user_agent}
    try:
        response = await client.get(website, headers=headers, timeout=5.0)
        print(website, get_status_description(response.status_code))
    except Exception:  # noqa: BLE001
        print(f'**Could not get any information for website: "{website}"')


async def main() -> None:
    base_dir = Path(__file__).parent
    csv_file = base_dir / "websites.csv"

    sites: list[str] = get_websites(csv_file)
    user_agent: str = get_user_agent()

    async with httpx.AsyncClient(follow_redirects=True) as client:
        tasks = [check_website(client, site, user_agent) for site in sites]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
