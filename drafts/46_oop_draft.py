class Monitor:
    def __init__(self, resolution: str, size_inch: int) -> None:
        self.resolution = resolution
        self.size_inch = size_inch

        self.is_on: bool = False

    def toggle_power(self) -> None:
        self.is_on = not self.is_on

    def __str__(self) -> str:
        status = "ON" if self.is_on else "OFF"
        return f"Monitor: {self.size_inch} | {self.resolution} | Status: {status}"


class Mouse:
    def __init__(self, brand: str, dpi: int) -> None:
        self.brand = brand
        self.dpi = dpi

    def click(self) -> str:
        return f"Mouse {self.brand}: click!"

    def __str__(self) -> str:
        return f"Mouse {self.brand} (DPI: {self.dpi})"


class Keyboard:
    def __init__(self, switch_type: str, has_rgb: bool) -> None:
        self.switch_type = switch_type
        self.has_rgb = has_rgb

    def type_text(self, text: str) -> str:
        return f"Typing ({self.switch_type}): '{text}'"

    def __str__(self) -> str:
        rgb_info = "w/ RGB" if self.has_rgb else "w/o RGB"
        return f"Keyboard ({self.switch_type}, {rgb_info})"


class Computer:
    def __init__(
        self, name: str, monitor: Monitor, mouse: Mouse, keyboard: Keyboard
    ) -> None:
        self.name = name

        self.monitor = monitor
        self.mouse = mouse
        self.keyboard = keyboard
        self.is_power_on: bool = False

    def power_on(self) -> None:
        self.is_power_on = True
        self.monitor.is_on = True
        print(f"Computer'{self.name}' starts up..")

    def power_off(self) -> None:
        self.is_power_on = False
        self.monitor.is_on = False
        print(f"Computer '{self.name}' turns off.")

    def get_system_status(self) -> str:
        pc_status = "ON" if self.is_power_on else "OFF"
        lines = [
            f"=== System: {self.name} ===",
            f"PC: {pc_status}",
            f"  - {self.monitor}",
            f"  - {self.mouse}",
            f"  - {self.keyboard}",
        ]
        return "\n".join(lines)


def main() -> None:
    my_monitor = Monitor("2880x1620", 16)
    my_mouse = Mouse("Steelseries", 1600)
    my_keyboard = Keyboard("Island-type White", True)

    my_pc = Computer(
        name="WorkStation-RTX",
        monitor=my_monitor,
        mouse=my_mouse,
        keyboard=my_keyboard,
    )

    print(my_pc.get_system_status())
    print("-" * 40)

    my_pc.power_on()
    print()
    print(my_pc.get_system_status())

    print()
    print(my_pc.mouse.click())
    print(my_pc.keyboard.type_text("print('Hello!')"))


if __name__ == "__main__":
    main()
