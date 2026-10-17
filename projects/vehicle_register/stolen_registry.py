import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


class StolenRegistry:
    def __init__(self, filename: str = "stolen.json") -> None:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        self.file_path = DATA_DIR / filename

        self.stolen_plates: dict[str, str] = {}
        self.load_from_file()

    def load_from_file(self) -> None:
        """Loads the list of stolen vehicles from the JSON file"""
        if not self.file_path.exists():
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                self.stolen_plates = json.load(f)
        except (json.JSONDecodeError, Exception) as e:  # noqa: BLE001
            print(f"Error reading stolen registry: {e}")

    def save_to_file(self) -> None:
        """Saves the current list of cars to the JSON file."""
        try:
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(self.stolen_plates, f, ensure_ascii=False, indent=4)
        except Exception as e:  # noqa: BLE001
            print(f"Error saving stolen registry: {e}")

    def add_to_stolen(self, plate_number: str, reason: str) -> None:
        """Adds a vehicle to the stolen registry with a specific reason"""
        plate = plate_number.strip().upper()
        self.stolen_plates[plate] = reason
        self.save_to_file()
        print(f"ALERT: Vehicle {plate} has been added to the stolen registry!")

    def remove_from_stolen(self, plate_number: str) -> bool:
        """Removes a vehicle from the stolen registry (e.g., recovered)"""
        plate = plate_number.strip().upper()
        if plate in self.stolen_plates:
            del self.stolen_plates[plate]
            self.save_to_file()
            print(f"Vehicle {plate} has been cleared from the stolen registry.")
            return True
        print(f"Vehicle {plate} was not found in the stolen registry.")
        return False

    def is_stolen(self, plate_number: str) -> tuple[bool, str | None]:
        """Checks if a vehicle is stolen. Returns (True/False, reason)"""
        plate = plate_number.strip().upper()
        if plate in self.stolen_plates:
            return True, self.stolen_plates[plate]
        return False, None
