import pytest
from utils.logger import logger
from utils.helpers import extract_number_from_invitations_text

@pytest.mark.dependency(name="check_requests")
@pytest.mark.order(1)
def test_check_requests(requests_page):
    """
    Checks for pending connection requests and performs actions based on the number of requests.

    :param requests_page: Page object representing the LinkedIn requests page.
    :return: None
    """
    logger.info("Checking for pending connection requests.")
    invitations_text = requests_page.get_pending_invitations_text()

    logger.info(f"Invitations text: {invitations_text}")

    number_of_requests = extract_number_from_invitations_text(invitations_text)
    if number_of_requests == 0:
        logger.info(f"Invitations requests is 0: {invitations_text}")
        pytest.skip("No pending requests found. Skipping the test.")

    if number_of_requests > 3:
        logger.info(f"Invitations requests is more than 3: {invitations_text}.")
        requests_page.get_show_all()
        logger.info(f"Invitations requests clicked.")


    assert number_of_requests > 0, "There should be at least one pending request."
    logger.info(f"Test 'passed'. Number of pending requests: {number_of_requests}")

@pytest.mark.dependency(depends=["check_requests"])
@pytest.mark.order(2)
def test_accept_requests(requests_page):
    """
    Accepts pending LinkedIn connection requests after verifying their existence.

    :param requests_page: Page object representing the LinkedIn requests page.
    :return: None
    """
    logger.info("test_accept_requests start:")

    accepted_count = requests_page.accept_all_requests()
    logger.info(f"Accepted count: {accepted_count}")

    logger.info(f'extract_number_from_invitations_text.')
    accepted_count = extract_number_from_invitations_text(accepted_count)

    if accepted_count == 0:
        logger.info("All connection requests have been accepted.")
    else:
        logger.warning(f"There are still {accepted_count} pending connection requests.")

    assert accepted_count == 0, "There are still pending requests that were not accepted."