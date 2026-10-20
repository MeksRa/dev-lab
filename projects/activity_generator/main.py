import json
from dataclasses import asdict, dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "activities.json"


@dataclass
class Activity:
    activity_id: int
    activity: str
    activity_type: str
    cost: int
    people: int

    def __str__(self) -> str:
        return f"id: [{self.activity_id}] | {self.activity} | Cost: {self.cost}$ | People: {self.people}"


def load_data() -> list[Activity]:
    """Load all the activities to JSON."""
    if not FILE_PATH.exists():
        return []

    activities: list[Activity] = []
    try:
        with FILE_PATH.open("r", encoding="utf-8") as f:
            for activity in json.load(f):
                activities.append(
                    Activity(
                        activity["activity_id"],
                        activity["activity"],
                        activity["activity_type"],
                        activity["cost"],
                        activity["people"],
                    )
                )
    except json.JSONDecodeError:
        ...
    return activities


def save_data(activities: list[Activity]) -> None:
    """Save all the activities to JSON."""
    try:
        data_to_save = [asdict(act) for act in activities]
        with FILE_PATH.open("w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    except Exception as e:  # noqa: BLE001
        print(f"Error saving activity: {e}")


def reindex_data(activities: list[Activity]) -> None:
    """Renumbers all activities sequentially from 0 to N-1"""
    for index, act in enumerate(activities):
        act.activity_id = index


def add_data(activities: list[Activity]) -> None:
    """Adding a new activity with automatic ID assignment."""
    print("\n--- Add New Activity ---")
    name = input("Enter activity name: ").strip()
    act_type = input("Enter activity type (e.g., indoor/outdoor): ").strip()

    try:
        cost = int(input("Enter cost ($): "))
        people = int(input("Enter number of people: "))
    except ValueError:
        print("Error: Cost and people must be numbers. Activity not added.")
        return

    new_id = len(activities)

    new_activity = Activity(
        activity_id=new_id,
        activity=name,
        activity_type=act_type,
        cost=cost,
        people=people,
    )

    activities.append(new_activity)
    print(f"Activity '{name}' successfully added!\n")


def remove_data(activities: list[Activity]) -> None:
    """Delete activities by ID with renumeration"""
    if not activities:
        print("No activities to remove")
        return
    try:
        target_id = int(input("Enter the activity ID to delete: "))
    except ValueError:
        print("Error: Please enter a valid number")
        return

    found_index = None
    for index, act in enumerate(activities):
        if act.activity_id == target_id:
            found_index = index
            break
    if found_index is not None:
        removed = activities.pop(found_index)
        reindex_data(activities)
        print(f"Activity '{removed.activity}' removed successfully!\n")
    else:
        print(f"Activity with ID [{target_id}] not found.\n")


def display_data(activities: list[Activity]) -> None:
    """Prints activities"""
    print("================ Activities ================")
    for i in activities:
        print(i)
    print("============================================")


def find_activity(activities: list[Activity]) -> None:
    """Looks for a suitable activity"""
    try:
        people: int = int(input("How many people are you? "))
        cost: int = int(input("How much are you willing to spend per person ($)? "))
    except ValueError:
        print("Error: Please only enter numerical values.")
        return

    matched_activities: list[Activity] = []
    for activity in activities:
        if activity.cost <= cost and activity.people <= people:
            matched_activities.append(activity)

    if matched_activities:
        print("\n--- Matched Activities ---")
        for i, matched in enumerate(matched_activities, 1):
            print(
                f"{i}: {matched.activity} | {matched.cost}$ per person [{people}p: {people * matched.cost}$]"
            )
        print()
    else:
        print("No activities matched your criteria...\n")


def main() -> None:
    activities: list[Activity] = load_data()
    while True:
        print("[0] - Exit\n[1] - Add\n[2] - Remove\n[3] - Find\n[4] - Display")
        user_choice = input("User: ").strip()

        if user_choice == "0":
            save_data(activities)
            print("Good luck!")
            break

        if user_choice == "1":
            add_data(activities)
            save_data(activities)

        elif user_choice == "2":
            remove_data(activities)
            save_data(activities)

        elif user_choice == "3":
            find_activity(activities)

        elif user_choice == "4":
            display_data(activities)

        else:
            print("Invalid input. Try: [0-3]")


if __name__ == "__main__":
    main()
