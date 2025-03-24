import pytest
from utils.logger import logger

# @pytest.mark.dependency(depends=["check_requests"])
def test_accept_requests(requests_page):
    """

    :param requests_page: Page object representing the LinkedIn requests page.
    :return: None
    """
    logger.info("test_accept_requests start:")
    assert True


