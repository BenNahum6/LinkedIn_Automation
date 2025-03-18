from utils.logger import logger
from pages.requests_page import RequestsPage

logger.info("Starting test_accept_requests:")

def test_accept_requests(driver):
    """

    :param driver:
    :return:
    """
    logger.info("test_accept_requests start:")
    requests_page_instance = RequestsPage(driver)
    requests_page_instance.navigate_to_my_network()

    if 'mynetwork' in driver.current_url:
        logger.info("Location: My Network tab")
    else:
        logger.error("Failed to load My Network page.", exc_info=True)
        raise AssertionError("My Network page failed to load.")