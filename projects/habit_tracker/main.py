from datetime import datetime, timedelta

import pandas as pd
from habit_tracker import Habit, track_habit
from tabulate import tabulate


def main() -> None:
    # 1. Set the start dates (10 and 30 days ago from today)
    now = datetime.now()
    coffee_start = now - timedelta(days=10)
    wasting_start = now - timedelta(days=30)

    # 2. Compiling a list of habits using our calculation function
    habits: list[Habit] = [
        track_habit("Coffee", coffee_start, cost=1.0, minutes_per_day=5),
        track_habit("Wasting time", wasting_start, cost=50.0, minutes_per_day=60)
    ]

    # 3. Converting a list of objects into a table using pandas
    data = [vars(h) for h in habits]
    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='psql'))  # with pandas
    # 4. Output to the terminal in a clean format (without extra row indices)
    print(tabulate(data, headers="keys", tablefmt="psql")) # without pandas

if __name__ == "__main__":
    main()