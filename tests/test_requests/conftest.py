import pytest
from utils.logger import logger
from pages.requests_page import RequestsPage


@pytest.fixture(scope="function")
def requests_page(driver):
    """
    Navigates to the 'My Network' page on LinkedIn before running a test.

    :param driver: The Selenium WebDriver instance.
    :return: An instance of RequestsPage with the driver set to the 'My Network' page.
    """
    logger.info("Navigating to 'My Network' page:")
    requests_page = RequestsPage(driver)
    requests_page.navigate_to_my_network()

    yield requests_page
