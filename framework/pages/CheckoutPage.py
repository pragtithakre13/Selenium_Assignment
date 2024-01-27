# checkout_page.py

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "akshay ")
    LAST_NAME_INPUT = (By.ID, "udawant")
    EMAIL_INPUT = (By.ID, "akshay@gmail.com")
    COUNTRY_DROPDOWN = (By.ID, "BillingNewAddress_CountryId")
    STATE_DROPDOWN = (By.ID, "BillingNewAddress_StateProvinceId")
    CITY_INPUT = (By.ID, "BillingNewAddress_City")
    ADDRESS_INPUT = (By.ID, "BillingNewAddress_Address1")
    ZIP_CODE_INPUT = (By.ID, "BillingNewAddress_ZipPostalCode")
    PHONE_INPUT = (By.ID, "BillingNewAddress_PhoneNumber")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")

    def fill_billing_details(self, first_name, last_name, email, country, state, city, address, zip_code, phone):
        self.fill_form(self.FIRST_NAME_INPUT, first_name)
        self.fill_form(self.LAST_NAME_INPUT, last_name)
        self.fill_form(self.EMAIL_INPUT, email)
        self.select_country(self.COUNTRY_DROPDOWN)
        self.select_state(self.STATE_DROPDOWN)
        self.fill_form(self.CITY_INPUT, city)
        self.fill_form(self.ADDRESS_INPUT, address)
        self.fill_form(self.ZIP_CODE_INPUT, zip_code)
        self.fill_form(self.PHONE_INPUT, phone)
        self.click(self.CONTINUE_BUTTON)


