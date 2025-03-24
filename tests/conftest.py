import pytest
from time import sleep
import random
from selenium import webdriver
from pages.login_page import LoginPage
from utils.logger import logger
from selenium_stealth import stealth

logger.info("Starting conftest:")

@pytest.fixture(scope="session")
def driver():
    """
    Creates a Chrome WebDriver instance for testing.

    - Initializes a Chrome WebDriver.
    - Maximizes the browser window.
    - Yields the driver for test usage.
    - Quits the driver after all tests in the session are completed.

    :return: Selenium WebDriver instance
    """
    logger.info("Creating driver.")

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.maximize_window()

    print("\n🔍 Checking stealth settings...\n")
    print("navigator.webdriver:", driver.execute_script("return navigator.webdriver"))  # Need to return None
    print("navigator.userAgent:",driver.execute_script("return navigator.userAgent"))  # Need to return User-Agent
    print("navigator.languages:", driver.execute_script("return navigator.languages"))  # Need to return ['en-US', 'en']

    # Checking a website that detects bots
    driver.get("https://bot.sannysoft.com/")
    print("\n🚀 Go to https://bot.sannysoft.com/ and check if everything is 'green'.\n")

    sleep(random.uniform(5, 10))

    yield driver
    logger.info("Deleting driver.")
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def login(driver):
    """
    Logs into LinkedIn before running all tests in the session.

    :param driver: The WebDriver instance used for automation.
    :return: None. Raises AssertionError if login fails.
    """
    # Performs a one-time login before all tests
    logger.info("login test start.")
    login_page = LoginPage(driver)
    login_page.login()

    if "feed" in driver.current_url:
        logger.info("Login successful.")
    else:
        logger.error("Login failed!", exc_info=True)
        raise AssertionError("Login failed.")
