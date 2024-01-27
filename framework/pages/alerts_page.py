from selenium.webdriver.common.by import By
class AlertsPage:

    ALERT_BUTTON = (By.XPATH, '//button[normalize-space()="Alert"]')
    CONFIRM_BOX=(By.XPATH,'//button[normalize-space()="Confirm Box"]')
    PROMPT_BUTTON = (By.XPATH, '//button[normalize-space()="Prompt"]')
    RESULT_TEXT = (By.ID, '//p[@id="demo"]')
    DRAGGABLE_ELEMENT = (By.ID, 'draggable')
    DROP_ZONE = (By.ID, 'droppable')
    OPEN_WINDOW_BUTTON = (By.XPATH, '//button[normalize-space()="New Browser Window"]')

    MAIN_FRAME = (By.XPATH, '//h2[normalize-space()="Frames"]')
    NAME_FIELD = (By.XPATH, '//*[@id="RESULT_TextField-0"]')
    GENDER_FIELD = (By.XPATH, '//*[@id="RESULT_RadioButton-1_0"]')
    DOB_FIELD = (By.XPATH, '//*[@id="RESULT_TextField-2"]')
    JOB_FIELD = (By.XPATH, '//*[@id="RESULT_RadioButton-3"]/option[2]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="FSsubmit"]')

    BUTTON_DOUBLE_CLICK = (By.XPATH, '//button[normalize-space()="Copy Text"]')
    FIELD1 = (By.ID, 'field1')
    FIELD2 = (By.ID, 'field2')

    MALE_RADIO = (By.ID, 'male')
    FEMALE_RADIO = (By.ID, 'female')

    OPTION1_CHECKBOX = (By.XPATH, '//input[@id="sunday"]')
    OPTION2_CHECKBOX = (By.XPATH, '//input[@id="monday"]')
    OPTION3_CHECKBOX = (By.XPATH, '//input[@id="tuesday"]')

    SELECT_DROPDOWN = (By.ID, 'country')
