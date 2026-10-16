import json
import os
from pathlib import Path
from typing import Final

import requests
from dotenv import load_dotenv
from model import Weather, dt

load_dotenv()


def load_api_key() -> str:
    api_key = os.getenv("OPENWEATHERMAP_API_KEY", "")
    if not api_key:
        raise ValueError("API KEY not found in environment variables.")
    return api_key


API_KEY: Final[str] = load_api_key()
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city_name: str, path: Path, mock: bool = True) -> dict:
    if mock:
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Local cache file '{path.name}' is corrupted or contains invalid JSON."
                ) from e
        else:
            raise FileNotFoundError(
                f"Local cache file '{path.name}' is missing. "
                "Run the script without mock first to download fresh data."
            )

    # Request live data
    payload: dict = {"q": city_name, "appid": API_KEY, "units": "metric"}

    try:
        request = requests.get(url=BASE_URL, params=payload, timeout=10)
        request.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            raise ValueError(
                f"City '{city_name}' was not found by OpenWeatherMap API."
            ) from e
        elif e.response is not None and e.response.status_code == 401:
            raise ValueError("Invalid API key. Please check your .env file.") from e
        else:
            raise ValueError(f"API error occurred: {e}") from e
    except requests.exceptions.RequestException as e:
        raise ConnectionError(
            "Network error: Failed to connect to weather service."
        ) from e

    try:
        data: dict = request.json()
    except ValueError as e:
        raise ValueError("API server returned invalid JSON format.") from e

    # Save new data to /data/{user_city}.json
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file)
    except OSError as e:
        print(f"Warning: Could not save data to local cache: {e}")

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get("list", [])
    if not days:
        raise ValueError(f"Problem with json: {weather}")
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(
            date=dt.fromtimestamp(day.get("dt", 0)),
            details=day.get("main", {}),
            temp=str(day.get("main", {}).get("temp", "")),
            weather=day.get("weather", []),
            description=day.get("weather", [{}])[0].get("description", ""),
        )
        list_of_weather.append(w)
    return list_of_weather
