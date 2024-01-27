from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.alerts_page import AlertsPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


def handle_alert(driver):
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    return alert_text

def handle_prompt(driver, prompt_text):
    # Find and click the button to trigger the prompt alert
    prompt_page = AlertsPage()
    prompt_button = driver.find_element(*prompt_page.PROMPT_BUTTON)
    prompt_button.click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.send_keys(prompt_text)
    alert.accept()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(prompt_page.RESULT_TEXT))
    return driver.find_element(*prompt_page.RESULT_TEXT).text

def perform_drag_and_drop(driver):
    drag_and_drop_page = AlertsPage()

    source_element = driver.find_element(*drag_and_drop_page.DRAGGABLE_ELEMENT)
    target_element = driver.find_element(*drag_and_drop_page.DROP_ZONE)

    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(source_element, target_element).perform()

def open_new_window(driver):
    window_handle_page = AlertsPage()
    parent_window_handle = driver.window_handles[0]
    # Click the button to open a new window
    driver.find_element(*window_handle_page.OPEN_WINDOW_BUTTON).click()
    # Switch to the new window
    new_window_handle = [handle for handle in driver.window_handles if handle != parent_window_handle][0]
    driver.switch_to.window(new_window_handle)
# helpers/frame_helper.py




def switch_to_frame(driver):
    frame_page = AlertsPage()
    # Switch to the frame
    driver.switch_to.frame(driver.find_element(*frame_page.MAIN_FRAME))
def enter_details_and_submit(driver, name, gender, dob, job):
    frame_page = AlertsPage()
    # Enter details in the frame
    driver.find_element(*frame_page.NAME_FIELD).send_keys(name)
    driver.find_element(*frame_page.GENDER_FIELD).send_keys(gender)
    driver.find_element(*frame_page.DOB_FIELD).send_keys(dob)
    driver.find_element(*frame_page.JOB_FIELD).send_keys(job)
    # Switch back to the default content before clicking
    driver.switch_to.default_content()
    # Click the Submit button
    driver.find_element(*frame_page.SUBMIT_BUTTON).click()

def double_click_and_copy_text(driver):
    double_click_page = AlertsPage()
    # Double click on the button
    button = driver.find_element(*double_click_page.BUTTON_DOUBLE_CLICK)
    text_from_field1 = driver.find_element(*double_click_page.FIELD1).text
    text_from_field2 = driver.find_element(*double_click_page.FIELD2)
    ActionChains(driver).double_click(button).perform()
    text_from_field2.clear()
    text_from_field2.send_keys(text_from_field1)


def select_gender(driver,gender):
    gender_page = AlertsPage()
    if gender.lower() == 'male':
        driver.find_element(*gender_page.MALE_RADIO).click()
    elif gender.lower() == 'female':
        driver.find_element(*gender_page.FEMALE_RADIO).click()
    else:
        raise ValueError(f"Invalid gender: {gender}")

def select_checkbox(driver, option):
    checkbox_page = AlertsPage()
    if option == 'Option 1':
        driver.find_element(*checkbox_page.OPTION1_CHECKBOX).click()
    elif option == 'Option 2':
        driver.find_element(*checkbox_page.OPTION2_CHECKBOX).click()
    elif option == 'Option 3':
        driver.find_element(*checkbox_page.OPTION3_CHECKBOX).click()
    else:
        raise ValueError(f"Invalid checkbox option: {option}")


def select_option_from_dropdown(driver, option_text):
    dropdown_page = AlertsPage()

    dropdown_element = driver.find_element(*dropdown_page.SELECT_DROPDOWN)
    dropdown = Select(dropdown_element)

    # Select option by visible text
    dropdown.select_by_visible_text(option_text)
