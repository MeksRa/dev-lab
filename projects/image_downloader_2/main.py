from pathlib import Path
from urllib.parse import urlparse

import requests


def save_folder(folder_name: Path | str) -> Path:
    """Creates a directory if it doesn't already exist, and returns the path."""

    directory = Path(folder_name)

    # parents=True => create the entire folder chain if necessary (image_downloader_2/images)
    # exist_ok=True => won't raise an error if the folder already exists.
    directory.mkdir(parents=True, exist_ok=True)

    return directory


def get_extension(image_url: str) -> str | None:
    """Safely extracts the file extension from a URL."""

    # Parse the URL and extract only the path (excluding parameters and host)
    parsed_path = urlparse(image_url).path

    # Extract the suffix (extension) and convert it to lowercase. (.JPG -> .jpg)
    suffix = Path(parsed_path).suffix.lower()

    # Whitelist of permitted formats
    allowed_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}

    # Return the extension only if it is in allowed_extensions list
    return suffix if suffix in allowed_extensions else None


def download_image(url: str, filename: str, save_dir: Path) -> None:
    """Downloads an image from a URL, checks for duplicates, and saves it to a folder."""

    # Check the extension using our function.
    ext = get_extension(url)
    if not ext:
        raise ValueError(
            "No supported image extension (.jpg, .png, etc.) was found in the link."
        )

    # Construct the full file path using pathlib (the / operator).
    file_path = save_dir / f"{filename}{ext}"

    # Check if the file exists and add a suffix (_01, _02...) if it is taken
    base_name = filename
    counter = 1
    while file_path.exists():
        # Format the counter with a leading zero: 1 -> "01", 2 -> "02", etc.
        filename_with_suffix = f"{base_name}_{counter:02d}"
        file_path = save_dir / f"{filename_with_suffix}{ext}"
        counter += 1
    print("Downloading...")

    # Downloading a file as a stream and writing it in parts
    try:
        # stream=True enables streaming data transfer
        # timeout=15 if takes longer than 15 sec it'll abort the attempt and proceed except block
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()  # Raises an error if the server returns a 404 or 500

        # Open the file for writing bytes ("wb")
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Successfully saved: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Network error during download: {e}")


def main() -> None:
    print("--- -- --- -- Image Downloader -- --- -- ---")

    # Get data from the user
    input_url: str = input("Enter the image URL: ").strip()
    input_name: str = input("How to name a file (without extension): ").strip()

    # Construct a cross-platform path relative to the main.py file

    # __file__ is the path to the current file (main.py)
    # .resolve().parent — get the absolute path to the folder containing this file
    CURRENT_DIR = Path(__file__).resolve().parent

    # Construct the path relative to the script's folder:
    base_dir = CURRENT_DIR / "images"

    # Preparing the folder
    saved_path = save_folder(base_dir)

    # Start downloading and handling potential errors
    try:
        download_image(input_url, input_name, saved_path)
    except (ValueError, FileExistsError) as err:
        print(f"Warning: {err}")
    except Exception as err:  # noqa: BLE001
        print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()
