import time

from tests.conftest import TestData
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from tests.test_base import BaseTest


class TestDemoNopCommerce(BaseTest):

    def test_demo_nopcommerce(self):
        home_page = HomePage(self.driver)
        home_page.go_to_build_your_own_computer()

        product_page = ProductPage(self.driver)
        product_page.add_to_cart(quantity="2")

        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        cart_page.proceed_to_checkout()

        # login_page = LoginPage(self.driver)
        # login_page.do_login(TestData.LOGIN_EMAIL, TestData.LOGIN_PASSWORD)

        # checkout_page = CheckoutPage(self.driver)
        # checkout_page.fill_billing_details(
        #     TestData.first_name,
        #     TestData.last_name,
        #     TestData.email,
        #     TestData.COUNTRY_NAME,
        #     TestData.STATE_NAME,
        #     TestData.city,
        #     TestData.address,
        #     TestData.zip_code,
        #     TestData.phone
        # )
