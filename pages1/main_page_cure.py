from selenium.webdriver.common.by import By

from pages1.base_page import Page


class MainPagecure(Page):
    POPUP_CLOSE = (By.XPATH, "//button[@class='popup-close']")

    def open_main_page_cure(self):
        self.open_url('https://shop.cureskin.com/')
        try:
            self.wait_for_element_click(*self.POPUP_CLOSE)
        except:
            pass
