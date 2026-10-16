def celsius_to_fahrenheit(celsius: float) -> str:
    return f"{celsius}°C = {(celsius * 1.8 + 32):.2f}°F"


def fahrenheit_to_celsius(fahrenheit: float) -> str:
    return f"{fahrenheit}°F = {((fahrenheit - 32) / 1.8):.2f}°C"


def kg_to_lbs(kg: float) -> str:
    return f"{kg} kg = {(kg * 2.204622):.2f} lbs"


def lbs_to_kg(lbs: float) -> str:
    return f"{lbs} lbs = {(lbs / 2.204622):.2f} kg"


def cm_to_inches(cm: float) -> str:
    return f"{cm} cm = {(cm / 2.54):.2f} inches"


def inches_to_cm(inches: float) -> str:
    return f"{inches} inches = {(inches * 2.54):.2f} cm"


def liters_to_gallons(liters: float) -> str:
    return f"{liters} L = {(liters / 3.785412):.2f} US gal"


def gallons_to_liters(gallons: float) -> str:
    return f"{gallons} US gal = {(gallons * 3.785412):.2f} L"


def km_to_miles(km: float) -> str:
    return f"{km} km = {(km / 1.609344):.2f} miles"


def miles_to_km(miles: float) -> str:
    return f"{miles} miles = {(miles * 1.609344):.2f} km"


def meters_to_feet(meters: float) -> str:
    return f"{meters} m = {(meters / 0.3048):.2f} ft"


def feet_to_meters(feet: float) -> str:
    return f"{feet} ft = {(feet * 0.3048):.2f} m"


def bar_to_psi(bar: float) -> str:
    return f"{bar} bar = {(bar * 14.50377):.2f} PSI"


def psi_to_bar(psi: float) -> str:
    return f"{psi} PSI = {(psi / 14.50377):.2f} bar"


def grams_to_oz(grams: float) -> str:
    return f"{grams} g = {(grams / 28.34952):.2f} oz"


def oz_to_grams(oz: float) -> str:
    return f"{oz} oz = {(oz * 28.34952):.2f} g"


def main() -> None:
    print("===== Ultimate Converter =====")
    while True:
        print(
            "Options:\n"
            "[0] - Exit\n"
            "[1] °C -> °F    | [2] °F -> °C\n"
            "[3] kg -> lbs   | [4] lbs -> kg\n"
            "[5] cm -> in    | [6] in -> cm\n"
            "[7] L -> gal    | [8] gal -> L\n"
            "[9] km -> miles | [10] miles -> km\n"
            "[11] m -> ft    | [12] ft -> m\n"
            "[13] bar -> PSI | [14] PSI -> bar\n"
            "[15] g -> oz    | [16] oz -> g"
        )
        print("==============================")
        user_input = input("Select option: ").strip()

        valid_options = [str(i) for i in range(17)]
        if user_input not in valid_options:
            print("Invalid input. Choose a number from the list.")
            continue

        if user_input == "0":
            print("Goodbye!")
            break

        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if user_input == "1":
            print(celsius_to_fahrenheit(amount))
        elif user_input == "2":
            print(fahrenheit_to_celsius(amount))
        elif user_input == "3":
            print(kg_to_lbs(amount))
        elif user_input == "4":
            print(lbs_to_kg(amount))
        elif user_input == "5":
            print(cm_to_inches(amount))
        elif user_input == "6":
            print(inches_to_cm(amount))
        elif user_input == "7":
            print(liters_to_gallons(amount))
        elif user_input == "8":
            print(gallons_to_liters(amount))
        elif user_input == "9":
            print(km_to_miles(amount))
        elif user_input == "10":
            print(miles_to_km(amount))
        elif user_input == "11":
            print(meters_to_feet(amount))
        elif user_input == "12":
            print(feet_to_meters(amount))
        elif user_input == "13":
            print(bar_to_psi(amount))
        elif user_input == "14":
            print(psi_to_bar(amount))
        elif user_input == "15":
            print(grams_to_oz(amount))
        elif user_input == "16":
            print(oz_to_grams(amount))


if __name__ == "__main__":
    main()
