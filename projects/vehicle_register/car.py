from dataclasses import asdict, dataclass


@dataclass
class Car:
    plate_number: str
    brand: str
    model: str
    year: int
    owner: str
    color: str
    engine: str
    horsepower: int
    transmission: str

    def get_passport_info(self) -> str:
        """Returns full detailed information about the vehicle"""
        return (
            f"\n--- Vehicle Passport ---"
            f"\nPlate Number: {self.plate_number}"
            f"\nBrand / Model: {self.brand} {self.model} ({self.year})"
            f"\nOwner: {self.owner}"
            f"\nColor: {self.color}"
            f"\nEngine: {self.engine} ({self.horsepower} hp)"
            f"\nTransmission: {self.transmission}"
            f"\n------------------------"
        )

    def to_dict(self) -> dict:
        """Converts an object to a dictionary (for saving in JSON)"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Car":
        """Creates a Car object from a dictionary (when reading from JSON)"""
        return cls(**data)
