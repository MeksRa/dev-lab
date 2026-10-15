import json
import os
from pathlib import Path
from typing import Final

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL: Final[str] = "https://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = os.getenv("EXCHANGERATESAPI_API_KEY", "")


def get_rates(mock: bool = False) -> dict:
    """
    Fetch currency exchange rates from the API or load them from a local cache file.

    Args:
        mock (bool): If True, loads rates from the local 'rates.json' file.
                     If False, fetches fresh data from the API and saves it locally.

    Returns:
        dict: A dictionary containing the exchange rates data.

    Raises:
        FileNotFoundError: If mock is True but the local cache file does not exist.
        ValueError: If the local JSON file is corrupted or the API response is invalid.
        ConnectionError: If a network or timeout error occurs during the API request.
    """

    script_dir = Path(__file__).parent
    config_file = script_dir / "rates.json"
    # --- -- ---
    # old data (cache)
    if mock:
        if config_file.exists():
            try:
                with open(config_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Local cache file '{config_file.name}' is corrupted or contains invalid JSON."
                ) from e
        else:
            raise FileNotFoundError(
                f"Local cache file '{config_file.name}' is missing. "
                "Run the script without mock first to download fresh data."
            )
    # --- -- ---
    # new data (request)
    payload: dict = {"access_key": API_KEY}

    try:
        response = requests.get(url=BASE_URL, params=payload, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout as e:
        raise ConnectionError(
            "API server request timed out. Please try again later."
        ) from e
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(
            "Failed to connect to the API server. Check your internet connection."
        ) from e
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response else "unknown"
        raise ValueError(
            f"API server returned an error (status code: {status_code}). Check your API key."
        ) from e

    try:
        data: dict = response.json()
    except ValueError as e:
        raise ValueError("API server returned invalid JSON format.") from e

    # Check for internal API error flags
    if isinstance(data, dict) and data.get("success") is False:
        error_info = data.get("error", {})
        error_msg = error_info.get("info", "Unknown API error")
        raise ValueError(f"API Error: {error_msg}")

    # Save fresh data to local cache file
    try:
        with open(config_file, "w", encoding="utf-8") as file:
            json.dump(data, file)
    except OSError as e:
        print(f"Warning: Could not save data to local cache: {e}")

    return data


def get_currency(currency: str, rates: dict) -> float:
    """
    Retrieve and validate the exchange rate for a specific currency from the rates dictionary.

    Args:
        currency (str): The currency code (e.g., 'USD', 'EUR').
        rates (dict): A dictionary of available exchange rates.

    Returns:
        float: The numeric exchange rate value.

    Raises:
        ValueError: If the currency code is not found in the rates dictionary.
    """
    # Normalize currency code to uppercase
    target_currency: str = currency.upper()

    # Check if the requested currency exists in rates dictionary
    if target_currency in rates:
        return float(rates[target_currency])
    else:
        raise ValueError(
            f"Currency '{target_currency}' is not a valid currency or not found in rates."
        )


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    """
    Convert an amount from a base currency to a target currency using provided rates.

    Args:
        amount (float): The amount of money to convert.
        base (str): The source currency code.
        vs (str): The target currency code.
        rates (dict): A dictionary of available exchange rates.

    Returns:
        float: The converted amount rounded to 2 decimal places.
    """
    # Get rates for both currencies
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    # Calculate conversion
    conversion: float = round((vs_rate / base_rate) * amount, 2)

    print(f"{amount:,.2f} ({base}) -> {conversion:,.2f} ({vs})")

    return conversion


def main() -> None:
    """
    Main interactive entry point of the application.
    Runs a CLI loop allowing users to convert currencies, toggle mock mode, and exit.
    """

    is_mock: bool = True

    print("\n=============== Currency Converter ===============")
    print("[Mock/live]  -> 't' or 'toggle' ")
    print("[Exit]       -> 'q' or 'exit' ")
    print("==================================================")

    while True:
        print(
            f"\nCurrent mode: {'MOCK (local data)' if is_mock else 'LIVE (API request)'}"
        )
        user_input: str = (
            input("Enter amount to convert (or command): ").strip().lower()
        )

        # Check for exit commands
        if user_input in ("q", "exit", "quit"):
            print("Exiting application. Goodbye!")
            break

        # Check for mode toggle command
        if user_input in ("toggle", "t"):
            is_mock = not is_mock
            print(f"-> Mock mode successfully switched to: {is_mock}")
            continue

        # Try to parse the amount
        try:
            amount: float = float(user_input)
        except ValueError:
            print(
                "Error: Invalid input. Please enter a valid number, 'toggle', or 'q'."
            )
            continue

        base: str = input("Enter base currency (e.g., EUR): ").strip()
        if base.lower() in ("q", "exit", "quit"):
            print("Exiting application. Goodbye!")
            break

        vs: str = input("Enter target currency (e.g., UAH): ").strip()
        if vs.lower() in ("q", "exit", "quit"):
            print("Exiting application. Goodbye!")
            break

        # Fetch rates and perform conversion with error handling
        try:
            data: dict = get_rates(mock=is_mock)
            rates: dict = data.get("rates", {})
            convert_currency(amount, base, vs, rates=rates)
        except (FileNotFoundError, ValueError, ConnectionError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
