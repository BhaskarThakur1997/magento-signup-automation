from behave import given, when, then
from pages.home_page import HomePage
from pages.signup_page import SignUpPage
from pages.signin_page import SignInPage
from utils.driver_setup import DriverSetup
import time

# Global variable to store email
global_email = None

@given("I am on the Magento homepage")
def step_i_am_on_magento_homepage(context):
    driver = DriverSetup.get_driver()
    driver.get("https://magento.softwaretestingboard.com/")
    context.home_page = HomePage()

@when("I navigate to the sign-up page")
def step_navigate_to_sign_up_page(context):
    context.home_page.go_to_sign_up()
    context.signup_page = SignUpPage()

@when("I fill in the sign-up form with valid details")
def step_fill_sign_up_form(context):
    global global_email
    unique_email = f"testuser{int(time.time())}@example.com"
    context.signup_page.fill_sign_up_form("John", "Doe", unique_email, "Password123!")
    global_email = unique_email  # Store email globally

@when("I submit the sign-up form")
def step_submit_sign_up_form(context):
    context.signup_page.submit()

@then("I should be redirected to the My Account page")
def step_verify_my_account_page(context):
    driver = DriverSetup.get_driver()
    assert "customer/account" in driver.current_url

@given("I am logged out and on the Magento homepage")
def step_logged_out_on_homepage(context):
    driver = DriverSetup.get_driver()
    driver.get("https://magento.softwaretestingboard.com/customer/account/logout/")
    driver.get("https://magento.softwaretestingboard.com/")
    context.home_page = HomePage()

@when("I navigate to the sign-in page")
def step_navigate_to_sign_in_page(context):
    context.home_page.go_to_sign_in()
    context.signin_page = SignInPage()

@when("I enter my credentials")
def step_enter_credentials(context):
    global global_email
    if global_email is None:
        raise Exception("No email available from previous sign-up")
    context.signin_page.enter_credentials(global_email, "Password123!")

@when("I submit the sign-in form")
def step_submit_sign_in_form(context):
    context.signin_page.submit()

@then("I should be logged in successfully")
def step_verify_logged_in(context):
    driver = DriverSetup.get_driver()
    assert driver.current_url == "https://magento.softwaretestingboard.com/"

def after_scenario(context, scenario):
    DriverSetup.quit_driver()
