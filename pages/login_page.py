from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD, LINKEDIN_LOGIN_URL

class LoginPage:
    def __init__(self, driver):
        """
        Initializes the class with a WebDriver instance.

        :param driver: The Selenium WebDriver instance used to interact with the web page.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self):
        """
        Logs into LinkedIn using provided credentials.

        :return: None
        """

        # Opens the browser with the LinkedIn url
        self.driver.get(LINKEDIN_LOGIN_URL)

        # Get the elements
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn__primary--large")))

        # Inserting information into elements
        email_input.send_keys(LINKEDIN_EMAIL)
        password_input.send_keys(LINKEDIN_PASSWORD)
        login_button.click()
