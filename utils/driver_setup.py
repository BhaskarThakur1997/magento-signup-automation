from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverSetup:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            service = Service(executable_path=ChromeDriverManager().install())
            cls._driver = webdriver.Chrome(service=service)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
