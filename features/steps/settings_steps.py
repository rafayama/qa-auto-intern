# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMAIL = '<LOGIN EMAIL>'
PASSWORD = '<PASSWORD>'
EMAIL_INPUT = (By.ID, 'email-2')
PASSWORD_INPUT = (By.ID, 'field')
LOGIN_BTN = (By.CSS_SELECTOR, '.login-button')
SETTINGS_BTN = (By.XPATH, "//a[@href='/settings']")
USER_GUIDE_BTN = (By.CSS_SELECTOR, ".settings-block-menu a[href='/user-guide']")
USER_GUIDE_PAGE_TITLE = (By.XPATH, "//div[text()='User guide' and @class='next-event-text']")
VIDEO_BLOCK = (By.CSS_SELECTOR, '.video-block iframe')
VIDEO_TITLE = (By.CSS_SELECTOR, '.chatbot-text-h1')

@given('Open Reely main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')
    sleep(5)

@when('Logged in')
def logged_in(context):
    email_field = context.driver.find_element(*EMAIL_INPUT)
    email_field.click()
    email_field.send_keys(EMAIL)

    password_field = context.driver.find_element(*PASSWORD_INPUT)
    password_field.click()
    password_field.send_keys(PASSWORD)

    login_button = context.driver.find_element(*LOGIN_BTN)
    login_button.click()

@when('Click on Settings button')
def click_settings(context):
    context.driver.find_element(*SETTINGS_BTN).click()
    sleep(2)

@when('Click on User guide button')
def click_user_guide(context):
    context.driver.find_element(*USER_GUIDE_BTN).click()
    sleep(2)

@then('Verify that the right page opens')
def verify_right_page_opens(context):
    context.driver.find_element(*USER_GUIDE_PAGE_TITLE)

@then('Verify that all lesson videos contain titles')
def verify_lesson_videos(context):
    context.driver.find_element(*VIDEO_BLOCK)
    context.driver.find_element(*VIDEO_TITLE)