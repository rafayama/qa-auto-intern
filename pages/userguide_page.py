from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class UserGuidePage(Page):
    USER_GUIDE_BTN = (By.CSS_SELECTOR, ".settings-block-menu a[href='/user-guide']")
    USER_GUIDE_PAGE_TITLE = (By.XPATH, "//div[text()='User guide' and @class='next-event-text']")
    VIDEO_BLOCK = (By.CSS_SELECTOR, '.video-block iframe')
    VIDEO_TITLE = (By.CSS_SELECTOR, '.chatbot-text-h1')

    def click_userguide(self):
        self.click(*self.USER_GUIDE_BTN)

    def verify_userguide_page(self):
        sleep(2)
        self.wait_for_element_to_appear(*self.USER_GUIDE_PAGE_TITLE)

    def verify_video_block_title(self):
        self.find_element(*self.VIDEO_TITLE)
        self.find_element(*self.VIDEO_BLOCK)