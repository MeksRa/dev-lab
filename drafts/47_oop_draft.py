class Lamp:
    def __init__(self, room: str) -> None:
        self.room = room
        self.is_on: bool = False
        self.brightness: int = 100

    def toggle(self) -> None:
        self.is_on = not self.is_on

    def set_brightness(self, level: int) -> None:
        if 0 <= level <= 100:
            self.brigthness = level

    def __str__(self) -> str:
        status = f"ON ({self.brightness}%)" if self.is_on else "OFF"
        return f"Lamp at the room '{self.room}' - Status: {status}"


class RemoteControl:
    def __init__(self, model: str) -> None:
        self.model = model
        self.lamps: list[Lamp] = []

    def pair_lamp(self, lamp: Lamp) -> None:
        """Sync lamp with remote control (add lamp)"""
        self.lamps.append(lamp)

    def toggle_lamp(self, index: int) -> None:
        lamp_idx = index - 1
        if 0 <= lamp_idx < len(self.lamps):
            self.lamps[lamp_idx].toggle()

    def turn_all_on(self) -> None:
        for lamp in self.lamps:
            lamp.is_on = True

    def turn_all_off(self) -> None:
        for lamp in self.lamps:
            lamp.is_on = False

    def show_status(self) -> str:
        if not self.lamps:
            return f"Remote Controller '{self.model}': no paired lamps"
        lines = [f"Remote Controller '{self.model}' - Lamp condition:"]
        for i, lamp in enumerate(self.lamps, start=1):
            lines.append(f"[{i}] {lamp}")
        return "\n".join(lines)


def main() -> None:
    living_room_lamp = Lamp("Living Room")
    kitchen_lamp = Lamp("Kitchen")
    bedroom_lamp = Lamp("Bedroom")

    my_remote = RemoteControl("SmartController")

    my_remote.pair_lamp(living_room_lamp)
    my_remote.pair_lamp(kitchen_lamp)
    my_remote.pair_lamp(bedroom_lamp)

    print(my_remote.show_status())
    print("-" * 20)

    my_remote.toggle_lamp(1)
    my_remote.toggle_lamp(3)

    print(my_remote.show_status())
    print("-" * 20)

    my_remote.turn_all_off()
    print(my_remote.show_status())


if __name__ == "__main__":
    main()
