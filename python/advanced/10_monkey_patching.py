import logging
import time


class Internet:
    def __init__(self, provider: str) -> None:
        self.provider = provider

    def connect(self) -> None:
        print(f"[{self.provider}] Connecting...")
        time.sleep(2)  # simulating a delay
        print(f"[{self.provider}] You are now connected!")


def test_connect() -> None:
    print("[Provider] You are now connected!")


# -----------------------------------------


def new_print(text: str) -> None:
    logging.warning(text)  # noqa: LOG015


def main() -> None:
    internet: Internet = Internet("Verizon")
    internet.connect()
    # [Verizon] Connecting...
    # [Verizon] You are now connected!
    # --- ---
    internet.connect = test_connect  # monkey patching
    internet.connect()
    # [Provider] You are now connected!

    # ----------------------------

    print = new_print
    print("Hello, world!")
    # WARNING:root:Hello, world!


if __name__ == "__main__":
    main()
