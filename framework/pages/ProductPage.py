# product_page.py
import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-1")
    QUANTITY_INPUT = (By.ID, "product_enteredQuantity_1")
    RAM = (By.XPATH, "//select[@id='product_attribute_2']")
    HDD = (By.ID, "product_attribute_3_6")

    def add_to_cart(self, quantity):
        self.fill_form(self.QUANTITY_INPUT, quantity)
        self.get_dropdown_element(self.RAM)
        self.do_click(self.HDD)
        time.sleep(4)
        self.do_click(self.ADD_TO_CART_BUTTON)
        time.sleep(4)