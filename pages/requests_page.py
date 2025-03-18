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
        """

        logger.info("navigate_to_my_network started:")

        try:
            logger.info("finde my_network_button element")
            my_network_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'mynetwork')]")))

            logger.info("clicking my_network_button element")
            my_network_button.click()

        except Exception as e:
            logger.error(f"Error when trying to click 'My Network': {e}", exc_info=True)
            raise