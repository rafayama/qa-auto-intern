from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
    SETTINGS_BTN = (By.XPATH, "//a[@href='/settings']")

    def click_settings(self):
        self.click(*self.SETTINGS_BTN)