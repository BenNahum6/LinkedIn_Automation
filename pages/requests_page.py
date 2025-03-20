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
        """
        logger.info("navigate_to_my_network started:")

        try:
            logger.info("Finding 'My Network' button.")
            my_network_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='mynetwork']")))
            print(my_network_button.text)  # מדפיס את הטקסט של האלמנט אם נמצא

            logger.info("Clicking 'My Network' button.")
            my_network_button.click()

        except Exception as e:
            logger.error(f"Error when trying to navigate to 'My Network': {e}", exc_info=True)
            raise AssertionError("Failed to load My Network page.")
