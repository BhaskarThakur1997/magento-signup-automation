from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup

class HomePage:
    def __init__(self):
        self.driver = DriverSetup.get_driver()
        self.create_account_link = (By.LINK_TEXT, "Create an Account")
        self.sign_in_link = (By.LINK_TEXT, "Sign In")

    def go_to_sign_up(self):
        self.driver.find_element(*self.create_account_link).click()

    def go_to_sign_in(self):
        self.driver.find_element(*self.sign_in_link).click()
