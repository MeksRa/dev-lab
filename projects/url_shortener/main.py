import os
from typing import Final
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Load environment variables from .env file
load_dotenv()

# Safely get API key from .env
API_KEY: Final[str] = os.getenv("CUTTLY_API_KEY", "")
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    """Sends a request to Cutt.ly API to shorten the given URL."""

    # Check if API key is present before making a request
    if not API_KEY:
        print("Error: API key is missing. Please check your .env file.")
        return

    # Check if the text looks like a link at all
    parsed_url = urlparse(full_link)
    if not parsed_url.scheme:
        # If the user forgets http:// or https://, we could insert it automatically
        # or show a clear error message. Let's require a valid format for now:
        print("Error: Invalid link format. Please include http:// or https://")
        return

    payload: dict = {"key": API_KEY, "short": full_link}

    try:
        # Safely perform network request with exception handling
        request = requests.get(BASE_URL, params=payload, timeout=10)
        # request.raise_for_status()  # Check for HTTP errors (like 404 or 500)
        data: dict = request.json()

    except RequestException as e:
        print(f"Network error occured: {e}")
        return

    # Parse the API response safely
    if url_data := data.get("url"):
        status = url_data.get("status")

        # Dictionary mapping API status codes to user-friendly messages
        status_messages = {
            1: "Warning: This link has already been shortened.",
            2: "Error: The entered text is not a valid link.",
            3: "Error: The preferred link name is already taken.",
            4: "Error: Invalid API key. Please check your .env file.",
            5: "Error: The link failed validation (contains invalid characters).",
            6: "Error: The link provided is from a blocked domain.",
            7: "Success! Shortened Link:",
            8: "Error: You have reached your monthly link limit.",
        }

        # Get message for status, or fallback for unknown codes
        message = status_messages.get(status, f"Unknown API response status: {status}")

        if status == 7:
            short_link: str = url_data.get("shortLink", "")
            print(f"{message}", short_link)
        else:
            print(message)
    else:
        print("Invalid response format from server.")


def main() -> None:
    """Main entry point of the script."""
    input_link: str = input("Enter a link to shorten: ").strip()
    if input_link:
        shorten_link(input_link)
    else:
        print("Error: Link cannot be empty.")


if __name__ == "__main__":
    main()
