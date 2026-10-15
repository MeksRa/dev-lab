import requests
from bs4 import BeautifulSoup


def get_soup() -> BeautifulSoup:
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
    }
    response = requests.get("https://www.bbc.com/news", headers=headers)

    # Create soup correctly
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def get_headlines(soup: BeautifulSoup) -> list[str]:
    # Use a set to avoid duplicate headlines
    unique_headlines: set = set()

    # Find all h2 tags with the correct data-testid attribute
    tags = soup.find_all("h2", attrs={"data-testid": "card-headline"})

    for h in tags:
        # Extract clean text, convert to lowercase
        headline: str = h.get_text(strip=True).lower()
        if headline:
            unique_headlines.add(headline)

    # Return sorted list of unique headlines
    return sorted(unique_headlines)  # list


def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline.split():
            terms_found += 1
            term_list.append(headline)
            print(f"{i}: {headline.capitalize()} <-----------------------'{term}'")
        else:
            print(f"{i}: {headline.capitalize()}")

    print("------------------------------")
    if terms_found:
        print(f"'{term}' was mentioned {terms_found} times.")
        print("------------------------------")

        for i, headline in enumerate(term_list, start=1):
            print(f"{i}: {headline.capitalize()}")

    else:
        print(f"No matches found for: '{term}'")
        print("------------------------------")


def main() -> None:
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    while True:
        user_input: str = input(
            "Type 'exit' or enter a keyword to search in headlines: "
        ).strip()
        if user_input == "exit":
            break

        if user_input:
            check_headlines(headlines, user_input)
        else:
            print("Search term cannot be empty.")


if __name__ == "__main__":
    main()
