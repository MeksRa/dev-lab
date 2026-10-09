from pathlib import Path

import qrcode

# "Pillow" installed


class MyQr:
    def __init__(self, size: int, padding: int) -> None:
        self.size = size
        self.padding = padding

    def create_qr(
        self, data: str, file_path: Path, fg: str = "black", bg: str = "white"
    ) -> None:
        """Creates and saves QR to the specified path"""

        try:
            qr = qrcode.QRCode(box_size=self.size, border=self.padding)
            qr.add_data(data)
            qr_image = qr.make_image(fill_color=fg, back_color=bg)

            with file_path.open("wb") as output:
                qr_image.save(output)

            print(f"--- -- ---\nSuccessfully created! ({file_path})\n--- -- ---")
        except Exception as e:  # noqa: BLE001
            print(f"Error: {e}")


def get_unique_path(target_path: Path) -> Path:
    """Returns unique path for qr codes, adds _01, _02 if file exists."""
    if not target_path.exists():
        return target_path

    directory = target_path.parent
    stem = target_path.stem
    suffix = target_path.suffix

    counter = 1
    while True:
        new_path = directory / f"{stem}_{counter:02d}{suffix}"
        if not new_path.exists():
            return new_path
        counter += 1


def generate_again() -> bool:
    """Asks the user if he wants to generate another QR"""
    while True:
        response = input("Do you want to generate another one (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def main() -> None:
    """Entry point. Main controller."""
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "qr_codes"
    output_dir.mkdir(parents=True, exist_ok=True)

    myqr: MyQr = MyQr(size=10, padding=10)

    while True:
        user_input: str = input("Enter text for QR code: ").strip()
        if not user_input:
            print("Text cannot be empty")
            continue

        initial_path = output_dir / "qr.png"
        file_path = get_unique_path(initial_path)

        myqr.create_qr(data=user_input, file_path=file_path, fg="black", bg="white")
        if not generate_again():
            print("Good luck!")
            break


if __name__ == "__main__":
    main()
