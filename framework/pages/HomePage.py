

from selenium.webdriver.common.by import By

from tests.conftest import TestData
from pages.BasePage import BasePage
from tests.test_base import BaseTest


class HomePage(BasePage):
    BUILD_YOUR_OWN_COMPUTER = (By.XPATH, "//h2/a[contains(text(),'Build your own computer')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def go_to_build_your_own_computer(self):
        self.do_click(self.BUILD_YOUR_OWN_COMPUTER)