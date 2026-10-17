import json
from pathlib import Path

from car import Car

BASE_DIR = Path(__file__).resolve().parent


class CarShop:
    def __init__(self, filename: str = "cars.json") -> None:
        self.file_path = BASE_DIR / filename
        self.cars: list[Car] = []
        self.load_from_file()

    def load_from_file(self) -> None:
        """Loads cars from JSON-file"""
        if not self.file_path.exists():
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.cars = [Car.from_dict(car_data) for car_data in data]
        except (json.JSONDecodeError, Exception) as e:  # noqa: BLE001
            print(f"Error reading file: {e}")

    def save_to_file(self) -> None:
        """Saves current car list into JSON-file"""
        try:
            data = [car.to_dict() for car in self.cars]
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:  # noqa: BLE001
            print(f"Error saving file: {e}")

    def add_car(self, car: Car) -> None:
        """Adds car to shop and saves to JSON-file"""
        self.cars.append(car)
        self.save_to_file()
        print(
            f"The car {car.brand} {car.model} has been successfully added to the catalog!"
        )

    def remove_car(self, car_id: str) -> bool:
        """Deletes a car by car_id. Returns True if it was deleted, and False if it was not found."""
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                self.save_to_file()
                print(f"Car with ID: {car_id} has been deleted.")
                return True
        print(f"Car with ID: {car_id} hasn't been found.")
        return False

    def get_car_by_id(self, car_id: str) -> Car | None:
        """Helper method: searches for and returns a Car object by its ID"""
        for car in self.cars:
            if car.car_id == car_id:
                return car
        return None

    def display_car_details(self, car_id: str) -> None:
        """Displays detailed information about the machine"""
        car = self.get_car_by_id(car_id)
        if not car:
            print(f"Car with ID: {car_id} hasn't been found.")
            return

        print(f"\n===== Car details: {car.brand} {car.model} ({car.year}) =====")
        print(f"ID: {car.car_id}")
        print(f"Price: ${car.price:,.2f}")
        print(f"Engine: {car.engine}")
        print(f"Horsepower: {car.horsepower} h.p.")
        print(f"Transmission: {car.transmission}")
        print(f"Available colors: {', '.join(car.colors)}")
        print("==================================================")

    def test_drive_car(self, car_id: str) -> None:
        """Starts a test drive of the car"""
        car = self.get_car_by_id(car_id)
        if not car:
            print(f"Car with ID: {car_id} hasn't been found for test-drive.")
            return

        print("\n--- TEST-DRIVE ---")
        print(car.test_drive())
        print("--------------------")

    def compare_cars(self, car_id_1: str, car_id_2: str) -> None:
        """Compares two cars based on their specifications"""
        car1 = self.get_car_by_id(car_id_1)
        car2 = self.get_car_by_id(car_id_2)

        if not car1 or not car2:
            print("One of the cars for comparison could not be found.")
            return

        print(
            f"\n===== Comparison: {car1.brand} {car1.model} vs {car2.brand} {car2.model} ====="
        )
        print(
            f"{'Characteristic':<20} | {car1.brand} {car1.model:<15} | {car2.brand} {car2.model}"
        )
        print("-" * 65)
        print(f"{'Price':<20} | ${car1.price:<16,.2f} | ${car2.price:<15,.2f}")
        print(f"{'Year':<20} | {car1.year:<18} | {car2.year}")
        print(
            f"{'Horsepower':<20} | {car1.horsepower} h.p. {'':<11} | {car2.horsepower} h.p."
        )
        print(f"{'Transmission':<20} | {car1.transmission:<18} | {car2.transmission}")
        print(f"{'Engine':<20} | {car1.engine:<18} | {car2.engine}")
        print("=================================================================")
