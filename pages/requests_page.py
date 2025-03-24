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
            invitation_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Invitations') or contains(text(), 'No pending invitations')]")))
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

    def accept_all_requests(self):
        """
        Finds and clicks all 'Accept' buttons on the LinkedIn connection requests page.
        :return: Number of pending invitations remaining after accepting.
        """
        logger.info("accept_all_requests started:")

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Invitation')]")))
            logger.info("Page with Invitations header is fully loaded.")
        except Exception as e:
            logger.error(f"Failed to load the Invitations page: {e}", exc_info=True)
            return 0

        # # Scroll to load all invitations (in case of lazy loading)
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # Locate buttons with more precise selectors
        try:
            accept_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Accept invitation')]")
            logger.info(f"Found {len(accept_buttons)} 'Accept' buttons.")
        except Exception as e:
            logger.error(f"Failed to find 'Accept' buttons: {e}", exc_info=True)
            return 0

        if not accept_buttons:
            logger.warning("No 'Accept' buttons found.")
            return 0

        # Click all Accept buttons
        for index, button in enumerate(accept_buttons):
            try:
                logger.info(f"Clicking 'Accept' button #{index + 1}.")
                button.click()
            except Exception as e:
                logger.error(f"Error when trying to click 'Accept' button #{index + 1}: {e}", exc_info=True)

        num = self.get_pending_invitations_text()
        logger.info(f"Found {num} pending invitations after accepting.")
        return num
