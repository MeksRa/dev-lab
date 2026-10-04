from typing import TextIO

file_path: str = "output/info.txt"
# Relative path, it depends on where the script was launched (Current Working Directory termial).

# ----------------------------------------

# If something happens between "open" and "close" you'll end up with a memory leak.
# cuz the file is going to remain open throughout the lifetime of our program
# even if we are done using it.

file: TextIO | None = None

try:
    file = open(file_path, "r")  # noqa: SIM115
    text: str = file.read()

    raise Exception("Unknown exception")  # noqa: TRY002
    print(text)
    # This is some info
    # Hi, Bob!
except FileNotFoundError:
    print("Could not find the file...")
except Exception as e:  # noqa: BLE001
    print(e)
finally:
    print("Force closing the file...")
    if file is not None:
        file.close()
        # Unknown exception
        # Force closing the file...

# --- Best practice -> using 'with" keyword --- #

# "with" will automatically close the file as soon as we leave "with" block.

file_path: str = "Hello.txt"  # unreal path/file
try:
    with open(file_path, "r") as f:
        text: str = f.read()

    print(text)
except FileNotFoundError:
    print(f"No file path found for: {file_path}")
    # No file path found for: Hello.txt
