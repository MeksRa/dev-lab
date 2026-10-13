import time

from crypto_data import Coin, get_coins


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, "!!Triggered!!")
            else:
                print(coin)


def main() -> None:
    coins: list[Coin] = get_coins()

    while True:
        time.sleep(30)
        coins: list[Coin] = get_coins()
        alert("btc", bottom=73_000, top=75_000, coins_list=coins)
        alert("eth", bottom=2_000, top=2_500, coins_list=coins)
        alert("xrp", bottom=1.20, top=1.24, coins_list=coins)


if __name__ == "__main__":
    main()
