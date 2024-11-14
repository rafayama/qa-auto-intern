from pages.base_page import Page
from pages.signin_page import SignInPage
from pages.settings_page import SettingsPage
from pages.userguide_page import UserGuidePage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.signin_page = SignInPage(driver)
        self.settings_page = SettingsPage(driver)
        self.userguide_page = UserGuidePage(driver)