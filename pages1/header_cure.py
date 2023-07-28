from pages1.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Headercure(Page):
    SHOP_CATEGORY = (By.XPATH,
                     "//summary[@class = 'header__menu-item header__menu-item--top list-menu__item focus-inset']//span[contains(text(),'Shop by Category')]")

    SEARCH_MENU = (By.CSS_SELECTOR, "span.header__icon svg.icon-hamburger")
    SHOP_CATEGORY_MOB = (By.XPATH, "//span[contains(text(),'Shop by Category')]")

    def click_shop_category(self):
        sleep(1)
        self.click(*self.SHOP_CATEGORY)

    def click_shop_category_mobile(self):
        sleep(1)
        self.click(*self.SEARCH_MENU)
        self.wait_for_element_click(*self.SHOP_CATEGORY_MOB)

