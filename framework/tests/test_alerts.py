from pages.alerts_page import AlertsPage
from helpers.alerts_helpers import handle_alert,perform_drag_and_drop,handle_prompt,open_new_window,switch_to_frame,enter_details_and_submit,select_gender,select_checkbox,select_option_from_dropdown
from selenium.webdriver.common.by import By
from pages.alerts_page import AlertsPage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

@pytest.mark.skip
def test_alerts(driver):
    driver
    alerts_page = AlertsPage()
    alert_button = driver.find_element(*alerts_page.ALERT_BUTTON)
    alert_button.click()
    alert_text = handle_alert(driver)
    assert alert_text == "I am an alert box!"

@pytest.mark.skip
def test_confirm_box(driver):
    driver
    alert_pages = AlertsPage()
    alert_buttons = driver.find_element(*alert_pages.CONFIRM_BOX)
    alert_buttons.click()
    alwert_txt = handle_alert(driver)
    assert alwert_txt == "Press a button!"

#notworking
@pytest.mark.skip
def test_prompt_alert(driver):
    result_text = handle_prompt(driver, 'Harry Potter')
    assert 'Harry Potter!' in result_text

@pytest.mark.skip
def test_drag_and_drop(driver):
   perform_drag_and_drop(driver)
   target_text = driver.find_element(By.ID,'droppable').text
   assert 'Dropped!' == target_text

@pytest.mark.skip
def test_window_handle(driver):
    open_new_window(driver)
    new_window_title = driver.title
    assert 'Your Store' == new_window_title

#notworking
@pytest.mark.skip
def test_frame(driver):
    time.sleep(30)
    switch_to_frame(driver)
    enter_details_and_submit(driver, 'John Doe', 'Male', '01/01/1990', 'Developer')
    success_message = driver.find_element(BY.XPATH,'//h1[normalize-space()="An error has occurred"]').text
    assert 'An error has occurred' == success_message

@pytest.mark.skip
def test_double_click(driver):
    double_click_page = AlertsPage()

    # Find the elements directly
    field1_element = driver.find_element(*double_click_page.FIELD1)
    field2_element = driver.find_element(*double_click_page.FIELD2)
    text_from_field1 = field1_element.text
    button = driver.find_element(*double_click_page.BUTTON_DOUBLE_CLICK)
    ActionChains(driver).double_click(button).perform()
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'field2'), text_from_field1)
        )
    except TimeoutException:
        print("Timeout waiting for FIELD2 to update.")

    field2_text = field2_element.text
    assert text_from_field1 == field2_text

@pytest.mark.skip
def test_assert_gender_radio_buttons(driver):
    select_gender(driver, 'male')
    assert driver.find_element(By.ID,'male').is_selected()

@pytest.mark.skip
def test_select_checkbox(driver):
    # Select the checkbox (either 'Option 1', 'Option 2', or 'Option 3')
    select_checkbox(driver, 'Option 1')

    # Add assertions to verify the result, e.g., check if the correct checkbox is selected
    option1_checkbox = driver.find_element(By.XPATH, '//input[@id="sunday"]')
    option2_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]')
    option3_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]')

    assert option1_checkbox.is_selected()
    assert not option2_checkbox.is_selected()
    assert not option3_checkbox.is_selected()


def test_select_option_from_dropdown(driver):
    select_option_from_dropdown(driver, 'India')
    selected_option = driver.find_element(By.XPATH,'//*[@id="country"]/option[10]')
    assert selected_option.text == 'India'