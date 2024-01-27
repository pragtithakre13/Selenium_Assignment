from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Config.config import TestData


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_dropdown_element(self, locator):
        x = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        drop = Select(x)
        drop.select_by_visible_text(TestData.RAM_SIZE)

    def select_country(self, locator):
        x = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        drop = Select(x)
        drop.select_by_visible_text(TestData.COUNTRY_NAME)

    def select_state(self, locator):
        x = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        drop = Select(x)
        drop.select_by_visible_text(TestData.STATE_NAME)

    def fill_form(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))