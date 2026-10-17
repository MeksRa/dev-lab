from dataclasses import asdict, dataclass


@dataclass
class Car:
    car_id: str
    brand: str
    model: str
    year: int
    price: float
    colors: list[str]
    engine: str
    horsepower: int
    transmission: str

    def test_drive(self) -> str:
        return f"You start up your {self.brand} {self.model}. You hit the gas, and {self.horsepower} horsepower propels you forward!"

    def to_dict(self) -> dict:
        """Converts an object into a dictionary for saving to JSON"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Car":
        """Creates a Car object from a dictionary (when reading from JSON)"""
        return cls(**data)
