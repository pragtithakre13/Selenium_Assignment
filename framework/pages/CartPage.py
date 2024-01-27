# cart_page.py
import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CartPage(BasePage):
    GO_TO_CART_BUTTON = (By.XPATH, "//span[contains(text(),'Shopping cart')]")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    TERM_AND_SERVICES_CHEKBOX = (By.ID, "termsofservice")
    def go_to_cart(self):
        self.do_click(self.GO_TO_CART_BUTTON)
        time.sleep(4)

    def proceed_to_checkout(self):
        self.do_click(self.TERM_AND_SERVICES_CHEKBOX)
        self.do_click(self.CHECKOUT_BUTTON)