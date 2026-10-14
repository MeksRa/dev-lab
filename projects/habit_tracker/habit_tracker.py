from dataclasses import dataclass
from datetime import datetime


@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(
    name: str, start: datetime, cost: float, minutes_per_day: float
) -> Habit:
    goal: int = 60  # 60 days to get rid of a habit
    hourly_wage: int = 30

    # 1. Calculating elapsed time
    time_elapsed: float = (datetime.now() - start).total_seconds()
    hours: float = round(time_elapsed / 60 / 60, 1)  # convert to hours, and round
    days: float = round(hours / 24, 2)  # convert to days, and round

    # 2. Calculating the money and time saved
    money_saved: float = cost * days
    calculated_minutes: float = round(days * minutes_per_day)
    total_money_saved: str = (
        f"${round(money_saved + (calculated_minutes / 60 * hourly_wage), 2)}"
    )

    # 3. Counting down the days to the goal
    days_to_go: float = round(goal - days)

    # 4. Formatting text for output
    remaining_days: str = "Cleared!" if days_to_go <= 0 else f"{days_to_go} days left"
    time_since: str = f"{round(days)} days" if hours > 72 else f"{hours} hours"

    return Habit(
        name=name,
        time_since=time_since,
        remaining_days=remaining_days,
        minutes_saved=calculated_minutes,
        money_saved=total_money_saved,
    )
