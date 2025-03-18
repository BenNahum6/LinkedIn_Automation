import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.logger import logger

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
    driver = webdriver.Chrome()
    driver.maximize_window()
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
