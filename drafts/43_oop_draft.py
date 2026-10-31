class Person:
    number_of_people = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


# --- -- --- -- --- -- ---
class Math:
    @staticmethod
    def add_5(x: int) -> int:
        return x + 5


def main() -> None:
    p1 = Person("Some dude")
    p2 = Person("One more dude")
    print(Person.number_of_people_())  # 2
    # --- -- ---
    print(Math.add_5(20))  # 25


if __name__ == "__main__":
    main()
