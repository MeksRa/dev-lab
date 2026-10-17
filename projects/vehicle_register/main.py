from car import Car
from registry import VehicleRegistry
from stolen_registry import StolenRegistry


def print_menu() -> None:
    print("\n===== VEHICLE REGISTRATION SYSTEM (GIBDD) =====")
    print("1. View all registered vehicles")
    print("2. Register a new vehicle")
    print("3. Check vehicle details (with stolen check)")
    print("4. Remove vehicle from registry")
    print("--- Stolen Registry Management ---")
    print("5. Add vehicle to STOLEN database")
    print("6. Remove vehicle from STOLEN database (Recovered)")
    print("0. Exit")
    print("===============================================")


def main() -> None:
    vehicle_registry = VehicleRegistry("registry.json")
    stolen_registry = StolenRegistry("stolen.json")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            cars = vehicle_registry.cars
            if not cars:
                print("\nNo vehicles registered in the database.")
            else:
                print("\n--- Registered Vehicles ---")
                for car in cars:
                    is_stolen, _ = stolen_registry.is_stolen(car.plate_number)
                    status = "[STOLEN]" if is_stolen else "[CLEAN]"
                    print(
                        f"{car.plate_number} | {car.brand} {car.model} ({car.year}) | Owner: {car.owner} {status}"
                    )
        elif choice == "2":
            print("\n--- Register a NEW Vehicle ---")
            try:
                plate_number = (
                    input("Enter plate number (e.g., A777AA77): ").strip().upper()
                )
                if vehicle_registry.find_by_plate(plate_number):
                    print(
                        "Error: A vehicle with this plate number is already registered."
                    )
                    continue
                brand = input("Brand: ").strip()
                model = input("Model: ").strip()
                year = int(input("Year: "))
                owner = input("Owner full name: ").strip()
                color = input("Color: ").strip()
                engine = input("Engine (e.g., 2.0 Turbo): ").strip()
                horsepower = int(input("Horsepower (hp): "))
                transmission = input("Transmission (Automatic / Manual): ").strip()

                new_car = Car(
                    plate_number=plate_number,
                    brand=brand,
                    model=model,
                    year=year,
                    owner=owner,
                    color=color,
                    engine=engine,
                    horsepower=horsepower,
                    transmission=transmission,
                )

                vehicle_registry.register_car(new_car)
            except ValueError:
                print("Input error! Please make sure year and horsepower are numbers.")

        elif choice == "3":
            plate_number = input("Enter plate number to check details: ").strip().upper()

            is_stolen, reason = stolen_registry.is_stolen(plate_number)
            if is_stolen:
                print(
                    f"\nWARNING! VEHICLE {plate_number.upper()} IS IN THE STOLEN DATABASE."
                )
                print(f"Reason / Details: {reason}")

                car = vehicle_registry.find_by_plate(plate_number)
                if car:
                    print(car.get_passport_info())
                else:
                    print(
                        f"Vehicle with plate '{plate_number}' was not found in the general vehicle registry."
                    )

        elif choice == "4":
            plate_number = input("Enter plate number to remove from registry: ").strip().upper()
            vehicle_registry.remove_car(plate_number)

        elif choice == "5":
            print("\n--- Add Vehicle to Stolen Database ---")
            plate_number = input("Enter plate number: ").strip().upper()

            car = vehicle_registry.find_by_plate(plate_number)

            if not car:
                print(
                    "Warning: This plate number is not found the general vehicle registry, but you can still add it to the wanted list."
                )

            reason = input(
                "Enter theft reason / details (e.g., Stolen on 2026-10-15, armed hijacking): "
            ).strip()
            stolen_registry.add_to_stolen(plate_number, reason)

        elif choice == "6":
            plate_number = input(
                "Enter plate number to clear from stolen registry: "
            ).strip()
            stolen_registry.remove_from_stolen(plate_number)

        elif choice == "0":
            print("\nExiting Vehicle Registration System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 6.")


if __name__ == "__main__":
    main()
