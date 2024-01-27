# cart_page.py
import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    USER_EMAIL = (By.ID, "Email")
    USER_PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log in']")

    def do_login(self, email, password):
        self.do_send_keys(self.USER_EMAIL, email)
        self.do_send_keys(self.USER_PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(4)

