class Car:
    def __init__(self, car_id: int, brand: str, daily_rate: float) -> None:
        self.car_id: int = car_id
        self.brand: str = brand
        self.is_available: bool = True
        self.daily_rate: float = daily_rate

    def rent_car(self) -> None:
        if not self.is_available:  # Guard Clause
            print(f"Error: Car {self.brand} is already rented!")
            return  # 1
        self.is_available = False
        print(f"Car {self.brand} has been successfully rented.")

    def return_car(self) -> None:
        if self.is_available:  # Guard Clause
            print(f"Error: Car {self.brand} was not rented!")
            return  # 1
        self.is_available = True
        print(f"Car {self.brand} is now available")

    def __str__(self) -> str:
        status = "Available" if self.is_available else "Rented"
        return f"[ID: {self.car_id}] {self.brand} - ${self.daily_rate:.2f}/day | Status: {status}"


class RentalFleet:  # Class manager
    def __init__(self) -> None:
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        for existing_car in self.cars:  # Guard Clause, check for duplicates
            if existing_car.car_id == car.car_id:
                print(f"Error: Car ID {car.car_id} already exists!")
                return  # 1
        self.cars.append(car)
        print(f"Car {car.brand} (ID: {car.car_id}) added to the fleet.")

    def find_car(self, car_id: int) -> Car | None:
        for car in self.cars:
            if car.car_id == car_id:
                return car  # match
        # loop finished
        return None

    def rent_car_by_id(self, car_id: int) -> None:
        car = self.find_car(car_id)
        if car is None:
            print(f"Error: Car with ID {car_id} not found.")
            return

        car.rent_car()

    def show_fleet(self) -> None:
        if not self.cars:  # Guard Clause
            print("Fleet is empty")
            return  # 1
        for car in self.cars:
            print(car)


def menu() -> None:
    fleet: RentalFleet = RentalFleet()  # RentalFleet Instance for management

    bmw: Car = Car(0, "BMW", daily_rate=50.0)  # Car Instance 1
    subaru: Car = Car(1, "SUBARU", daily_rate=100.0)  # Car Instance 2

    fleet.add_car(bmw)
    fleet.add_car(subaru)

    print("\n--- Initial Fleet ---")
    fleet.show_fleet()
    print("\n--- Renting BMW (ID 0) ---")
    fleet.rent_car_by_id(0)
    print("\n--- Trying to rent BMW again ---")
    fleet.rent_car_by_id(0)
    print("\n--- Updated Fleet Status ---")
    fleet.show_fleet()


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
