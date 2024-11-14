from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
    SETTINGS_BTN = (By.XPATH, "//a[@href='/settings']")

    def click_settings(self):
        sleep(2)
        self.click(*self.SETTINGS_BTN)