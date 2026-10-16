from weather_api import Path, Weather, get_weather, get_weather_details


def main():
    script_dir = Path(__file__).resolve().parent

    while True:
        user_city: str = input("Enter a city (or 'exit'): ").strip().lower()
        if user_city == "exit":
            print("Good luck!")
            break
        if not user_city:
            print("City name cannot be empty. Try again.")
            continue
        clean_city = user_city.replace(" ", "").replace("-", "")
        if not clean_city.isalpha() or len(user_city) < 2:
            print(
                f"Error: '{user_city}' is not a valid city name. Please use letters only."
            )
            continue

        config_path: Path = script_dir / "data" / f"{user_city}.json"

        # Get the current weather details
        try:
            # mock=False -> Live Data
            # mock=True -> Cache
            current_weather: dict = get_weather(user_city, config_path, mock=False)
            weather_details: list[Weather] = get_weather_details(current_weather)
        except FileNotFoundError:
            print(f"Error: City '{user_city}' not found in local mock cache.")
            continue
        except ValueError as e:
            print(f"Data error: {e}")
            continue

        # Get the current days
        dfmt: str = "%d/%m/%y"
        days: list[str] = sorted({f"{date.date:{dfmt}}" for date in weather_details})

        for day in days:
            print(day)
            print("---")

            grouped: list[Weather] = [
                current
                for current in weather_details
                if f"{current.date:{dfmt}}" == day
            ]

            for element in grouped:
                print(element)
        print()


if __name__ == "__main__":
    main()
