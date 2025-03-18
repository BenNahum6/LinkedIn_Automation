import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.logger import logger

logger.info("Starting conftest:")

@pytest.fixture(scope="session")
def driver():
    """

    :return:
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

    :param driver:
    :return:
    """
    # Performs a one-time login before all tests
    logger.info("login test start.")
    login_page = LoginPage(driver)
    login_page.login()

    if "feed" in driver.current_url:
        logger.info("Login successful.")
    else:
        logger.error("Login failed!", exc_info=True)
        raise AssertionError("Login failed!")
