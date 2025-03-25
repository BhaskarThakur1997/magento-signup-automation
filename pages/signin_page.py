from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup

class SignInPage:
    def __init__(self):
        self.driver = DriverSetup.get_driver()
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "pass")
        self.sign_in_button = (By.ID, "send2")

    def enter_credentials(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.sign_in_button).click()
