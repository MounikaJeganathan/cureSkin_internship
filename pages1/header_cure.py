from pages1.base_page import Page
from selenium.webdriver.common.by import By


class Headercure(Page):
    SHOP_CATEGORY = (By.XPATH, "//summary[@class = 'header__menu-item header__menu-item--top list-menu__item focus-inset']//span[contains(text(),'Shop by Category')]")


    def click_shop_category(self):
        self.click(*self.SHOP_CATEGORY)

