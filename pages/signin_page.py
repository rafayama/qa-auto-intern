from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_PAGE_URL = "https://soft.reelly.io/sign-in"
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')
    USER_EMAIL = 'rafa.yamashiro@gmail.com'
    USER_PASSWORD = '7huNderb0!t'

    def open_signin_page(self):
        self.open(self.SIGNIN_PAGE_URL)

    def sign_in(self):
        self.input_text(self.USER_EMAIL, *self.EMAIL_INPUT)
        self.input_text(self.USER_PASSWORD, *self.PASSWORD_INPUT)
        self.click(*self.CONTINUE_BTN)
