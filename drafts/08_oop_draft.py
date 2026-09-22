class Thermostat:
    def __init__(self, room_name: str, max_temp: int) -> None:

        self.room_name: str = room_name
        self.max_temp: int = max_temp

        self.current_temp: int = 20
        self.is_active: bool = False

    def switcher(self) -> None:
        if self.is_active:
            self.is_active = False
            print(f"The Thermostat for {self.room_name} has just been turned off!")
        else:
            self.is_active = True
            print(f"The Thermostat for {self.room_name} has just been turned on!")

    def set_temp(self, new_temp: int) -> None:
        if not self.is_active:  # Guard Clause
            print("Error: Thermostat is inactive")
            return  # 1
        if new_temp <= 0 or new_temp > self.max_temp:  # Guard Clause
            print("Error: Invalid temperature")
            return  # 2

        self.current_temp = new_temp
        print(
            f"The thermostat temperature for {self.room_name} has just been changed to {new_temp} °C"
        )

    def __str__(self) -> str:
        status: str = "Active" if self.is_active else "Inactive"
        return f"Room: {self.room_name} | Current temperature: {self.current_temp}°C | Status: {status}"


def menu():
    thermostat1: Thermostat = Thermostat("Room_1", 30)
    while True:
        print("""
|---------------|
|Thermostat Info|
|---------------|
[0] <- exit
[1] <- Switch on/ Switch off
[2] <- Set temperature
[3] <- Status
    """)
        user_input: str = input("User: ")
        if "0" == user_input:
            print("Bye")
            break
        elif "1" == user_input:
            thermostat1.switcher()
        elif "2" == user_input:
            new_temp = input("New temperature: ").strip()
            if not new_temp.isdigit():
                print("Error: Enter a valid number")
            else:
                thermostat1.set_temp(int(new_temp))
        elif "3" == user_input:
            print(thermostat1)


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
