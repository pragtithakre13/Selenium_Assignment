import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://testautomationpractice.blogspot.com/'
    driver.get(url)
    yield driver
    driver.close()

@pytest.fixture
def driver_nopcommerce():
    driver=webdriver.Chrome()
    driver.maximize_window()
    url=' https://demo.nopcommerce.com/'
    driver.get(url)
    yield driver
    driver.close()

class TestData:

    BASE_URL = "https://demo.nopcommerce.com/"
    RAM_SIZE = "2 GB"
    first_name = "pragati",
    last_name = "thakre",
    email = "pragatithakre@gmail.com",
    COUNTRY_NAME = "United States"
    STATE_NAME = "Alaska"
    city = "New York",
    address = "123 Main St",
    zip_code = "10001",
    phone = "1234567890"

    LOGIN_EMAIL = "pragati@gmail.com"
    LOGIN_PASSWORD = "pragati@123"