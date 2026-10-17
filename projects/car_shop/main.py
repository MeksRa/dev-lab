from car import Car
from car_shop import CarShop


def print_menu() -> None:
    print("\n===== CAR SHOP MANAGEMENT SYSTEM =====")
    print("1. View all cars")
    print("2. Add a new car")
    print("3. View car details")
    print("4. Test drive a car")
    print("5. Compare two cars")
    print("6. Remove a car")
    print("0. Exit")
    print("======================================")


def main() -> None:
    shop = CarShop("cars.json")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            cars = shop.cars
            if not cars:
                print("\nNo cars available in the catalog.")
            else:
                print("\n--- Available Cars ---")
                for car in cars:
                    print(
                        f"ID: {car.car_id} | {car.brand} {car.model} ({car.year}) — ${car.price:,.2f}"
                    )

        elif choice == "2":
            print("\n--- Add a New Car ---")
            try:
                car_id = input("Enter unique ID (e.g., c01): ").strip()
                if shop.get_car_by_id(car_id):
                    print("Error: A car with this ID already exists!")
                    continue

                brand = input("Brand: ").strip()
                model = input("Model: ").strip()
                year = int(input("Year: "))
                price = float(input("Price ($): "))
                colors_input = input("Colors separated by comma (e.g., black, white): ")
                colors = [c.strip() for c in colors_input.split(",")]
                engine = input("Engine (e.g., 2.0 Turbo): ").strip()
                horsepower = int(input("Horsepower (hp): "))
                transmission = input("Transmission (Automatic / Manual): ").strip()

                new_car = Car(
                    car_id=car_id,
                    brand=brand,
                    model=model,
                    year=year,
                    price=price,
                    colors=colors,
                    engine=engine,
                    horsepower=horsepower,
                    transmission=transmission,
                )

                shop.add_car(new_car)
            except ValueError:
                print(
                    "Input error! Please make sure year, price, and horsepower are numbers."
                )

        elif choice == "3":
            car_id = input("Enter car ID to view details: ").strip()
            shop.display_car_details(car_id)

        elif choice == "4":
            car_id = input("Enter car ID for test drive: ").strip()
            shop.test_drive_car(car_id)

        elif choice == "5":
            id1 = input("Enter first car ID: ").strip()
            id2 = input("Enter second car ID: ").strip()
            shop.compare_cars(id1, id2)

        elif choice == "6":
            car_id = input("Enter car ID to remove: ").strip()
            shop.remove_car(car_id)

        elif choice == "0":
            print("\nThank you for using Car Shop! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 6.")


if __name__ == "__main__":
    main()
