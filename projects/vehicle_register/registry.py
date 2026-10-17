import json
from pathlib import Path

from car import Car

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


class VehicleRegistry:
    def __init__(self, filename: str = "registry.json") -> None:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        self.file_path = DATA_DIR / filename
        self.cars: list[Car] = []
        self.load_from_file()

    def load_from_file(self) -> None:
        """Loads all registered cars from the JSON file."""
        if not self.file_path.exists():
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.cars = [Car.from_dict(car_data) for car_data in data]
        except (json.JSONDecodeError, Exception) as e:  # noqa: BLE001
            print(f"Error reading vehicle registry: {e}")

    def save_to_file(self) -> None:
        """Saves the current list of cars to the JSON file."""
        try:
            data = [car.to_dict() for car in self.cars]
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:  # noqa: BLE001
            print(f"Error saving vehicle registry: {e}")

    def register_car(self, car: Car) -> bool:
        """Registers a new vehicle if the plate number is unique."""
        if self.find_by_plate(car.plate_number):
            print(
                f"Error: Vehicle with plate '{car.plate_number}' is already registered."
            )
            return False

        self.cars.append(car)
        self.save_to_file()
        print(f"Vehicle {car.plate_number} successfully registered.")
        return True

    def find_by_plate(self, plate_number: str) -> Car | None:
        """Finds and returns a car by its plate number (case-insensitive)"""
        search_plate = plate_number.strip().upper()
        for car in self.cars:
            if car.plate_number.upper() == search_plate:
                return car
        return None

    def remove_car(self, plate_number: str) -> bool:
        """Removes a vehicle from the registry by plate number."""
        car = self.find_by_plate(plate_number)
        if car:
            self.cars.remove(car)
            self.save_to_file()
            print(
                f"Vehicle with plate {plate_number} has been removed from the registry."
            )
            return True
        print(f"Vehicle with plate {plate_number} not found in the registry.")
        return False
