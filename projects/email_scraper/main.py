import re
from typing import Final

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# EMAIL_REGEX: Final[
#    str
# ] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
# \x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
# a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
# 0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
# \x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# More simple regex for email searching
EMAIL_REGEX: Final[str] = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


class Browser:
    def __init__(self) -> None:
        print("Starting up browser...")
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")  # prevent browser from showing
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")

        self.browser = webdriver.Chrome(options=self.chrome_options)

    def scrape_emails(self, url: str) -> set[str]:
        print(f'Scraping: "{url}" for emails')

        self.browser.get(url)
        # --- -- --- -- ---
        # Wait up to 10 seconds for at least one tag containing text (or a specific element) to appear on the page
        # Selenium will check this condition as soon as the DOM tree begins to become active
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except Exception as e:  # noqa: BLE001
            print(f"The page didn't have time to load.: {e}")
        # --- -- --- -- ---

        page_source: str = self.browser.page_source
        list_of_emails: set[str] = set()

        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())
        return list_of_emails

    def close_browser(self):
        print("Closing browser...")
        self.browser.quit()


def main():
    browser = Browser()

    try:
        emails: set = browser.scrape_emails(
            "https://www.randomlists.com/email-addresses?qty=50"
        )

        for i, email in enumerate(emails, start=1):
            print(f"{i}: {email}")
    finally:
        # Guarantee the browser closes in the event of any errors.
        browser.close_browser()


if __name__ == "__main__":
    main()
