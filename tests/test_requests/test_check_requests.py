import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import logger


# @pytest.mark.dependency(name="check_requests")
def test_check_requests(requests_page):
    """

    :param requests_page:
    :return:
    """
    logger.info("Checking for pending connection requests.")
    pending_requests = requests_page.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2[class*='_1s9oaxgp']")))
    logger.info(pending_requests)

    # Todo need to check it works.
    print(f"heyyyyyyyyyyy {pending_requests.text}")  # זה יחזיר: "Invitations (3)"


    if not pending_requests:
        pytest.skip("No pending requests found.")

    assert pending_requests, "There should be at least one pending request."
