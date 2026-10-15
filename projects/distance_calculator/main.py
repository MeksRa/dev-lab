from dataclasses import dataclass

from geopy.distance import geodesic
from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from geopy.geocoders import Nominatim


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self) -> tuple[float, float]:
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent="distance_calculator")
    try:
        location = geolocator.geocode(address, timeout=10)  # type: ignore
        if (
            location
            and hasattr(location, "latitude")
            and hasattr(location, "longitude")
        ):
            return Coordinates(latitude=location.latitude, longitude=location.longitude)  # type: ignore
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Network error during geocoding: {e}")

    return None


def calculate_distance_km(home: Coordinates, target: Coordinates) -> float:
    distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
    return distance


def get_distance_km(home: str, target: str) -> float | None:
    print("Geocoding addresses...")
    home_coordinates: Coordinates | None = get_coordinates(home)
    target_coordinates: Coordinates | None = get_coordinates(target)

    if not home_coordinates or not target_coordinates:
        print("Error: Could not find one or both addresses. Please try again.")
        return None

    distance = calculate_distance_km(home_coordinates, target_coordinates)
    print("\n" + "=" * 40)
    print(f"From: {home}")
    print(f"To:   {target}")
    print(f"Distance: {distance:.2f} kilometres")
    print("=" * 40 + "\n")
    return distance


def main() -> None:
    home_address: str = "Helsinkigade 10, Copenhagen 2150, Denmark"
    print(f"Home address: {home_address}\n")
    print("========= Distance Calculator CLI =========")
    print("Type 'exit' to quit the program.\n")

    while True:
        target_address: str = input("Enter target address: ").strip()

        if target_address.lower() == "exit":
            print("Exiting application. Goodbye!")
            break

        if not target_address:
            print("Address cannot be empty. Try again.\n")
            continue

        get_distance_km(home_address, target_address)


if __name__ == "__main__":
    main()
