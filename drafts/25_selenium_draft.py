import time

from selenium import webdriver


# Selenium Manager will automatically find and configure the required driver "under the hood."
class Browser:
    def __init__(self):
        print("Starting up...")
        self.browser = webdriver.Chrome()

    def open_page(self, url: str):
        print(f"Opening: {url}")
        self.browser.get(url)

    def close_browser(self):
        print("Closing browser")
        self.browser.quit()


def main() -> None:
    browser = Browser()
    browser.open_page("https://www.python.org")
    time.sleep(5)
    browser.close_browser()


if __name__ == "__main__":
    main()

# pip install selenium
