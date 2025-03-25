from selenium.webdriver.common.by import By
from utils.driver_setup import DriverSetup

class SignUpPage:
    def __init__(self):
        self.driver = DriverSetup.get_driver()
        self.first_name_field = (By.ID, "firstname")
        self.last_name_field = (By.ID, "lastname")
        self.email_field = (By.ID, "email_address")
        self.password_field = (By.ID, "password")
        self.confirm_password_field = (By.ID, "password-confirmation")
        self.create_account_button = (By.CSS_SELECTOR, "button[title='Create an Account']")

    def fill_sign_up_form(self, first_name, last_name, email, password):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.confirm_password_field).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.create_account_button).click()
