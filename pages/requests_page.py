from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class RequestsPage:
    def __init__(self, driver):
        """
        Initializes the class with a WebDriver instance.

        :param driver: The Selenium WebDriver instance used to interact with the web page.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_my_network(self):
        """
        Navigates to the "My Network" page on LinkedIn by clicking the navigation button.
        Waits for a unique element on the page to ensure it has fully loaded.

        :return: None
        """

        logger.info("navigate_to_my_network started:")

        try:
            logger.info("Finding 'My Network' button.")
            my_network_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='mynetwork']")))
            print(my_network_button.text)

            logger.info("Clicking 'My Network' button.")
            my_network_button.click()

        except Exception as e:
            logger.error(f"Error when trying to navigate to 'My Network': {e}", exc_info=True)
            raise AssertionError("Failed to load My Network page.")

    def get_pending_invitations_text(self):
        """
        Finds the 'Invitations' element and returns its text.
        Waits until the element is visible on the page.

        :return: The text of the Invitations element.
        """
        logger.info("get_pending_invitations_text started:")

        try:
            logger.info("Finding pending invitations element.")
            invitation_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Invitations')]")))
            logger.info(f"Invitations text found: {invitation_element.text}")

            return invitation_element.text
        except Exception as e:
            logger.error(f"Failed to find invitations element: {e}", exc_info=True)
            raise AssertionError("Could not find invitations element.")

    def get_show_all(self):
        """
        Finds and clicks the "Show all" button on the page to navigate to the invitation manager.

        :return: None
        """
        logger.info("get_show_all started:")

        try:
            logger.info("Finding Show all element.")
            ShowAll_element = self.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,"a[href='https://www.linkedin.com/mynetwork/invitation-manager/']"))

            logger.info(f"Clicking 'show all' button.")
            ShowAll_element.click()

            if "invitation-manager" in self.driver.current_url:
                logger.info("Go to invitation-manager successful.")
            else:
                logger.error("Go to invitation-manager failed!", exc_info=True)
                raise AssertionError("Go to invitation-manager failed.")

        except Exception as e:
            logger.error(f"Error when trying to navigate to 'show all': {e}", exc_info=True)
            raise AssertionError("Failed to load show all page.")

