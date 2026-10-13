import time
from dataclasses import dataclass
from typing import Final

import requests

# Public API
BASE_URL: Final[str] = "https://api.coingecko.com/api/v3/coins/markets"


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self) -> str:
        return f"{self.name} ({self.symbol}): €{self.current_price:,}"


def get_coins() -> list[Coin]:
    payload: dict = {"vs_currency": "eur", "order": "market_cap_desc"}
    data = requests.get(BASE_URL, params=payload)

    if data.status_code == 429:
        print("Request limit exceeded (429). Waiting before retrying...")
        time.sleep(60)  # wait a minute before the next request.
        return []

    json: dict = data.json()

    coin_list: list[Coin] = []
    for item in json:
        current_coin: Coin = Coin(
            name=item.get("name"),
            symbol=item.get("symbol"),
            current_price=item.get("current_price"),
            high_24h=item.get("high_24h"),
            low_24h=item.get("low_24h"),
            price_change_24h=item.get("price_change_24h"),
            price_change_percentage_24h=item.get("price_change_percentage_24h"),
        )
        coin_list.append(current_coin)

    return coin_list


def main() -> None:
    coins = get_coins()
    for coin in coins:
        print(coin)


if __name__ == "__main__":
    main()
