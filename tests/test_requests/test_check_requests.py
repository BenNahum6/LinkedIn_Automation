import pytest
from utils.logger import logger
from utils.helpers import extract_number_from_invitations_text

# @pytest.mark.dependency(name="check_requests")
def test_check_requests(requests_page):
    """
    Checks for pending connection requests and performs actions based on the number of requests.

    :param requests_page: Page object representing the LinkedIn requests page.
    :return: None
    """
    logger.info("Checking for pending connection requests.")
    invitations_text = requests_page.get_pending_invitations_text()

    logger.info(f"Invitations text: {invitations_text}")
    print(f"Invitations text: {invitations_text}")

    number_Of_requests = extract_number_from_invitations_text(invitations_text)
    if number_Of_requests == 0:
        logger.info(f"Invitations requests is 0: {invitations_text}")
        # pytest.skip("No pending requests found. Skipping the test.")

    if number_Of_requests > 3:
        requests_page.get_show_all()


    assert number_Of_requests > 0, "There should be at least one pending request."
    logger.info(f"Test passed. Number of pending requests: {number_Of_requests}")