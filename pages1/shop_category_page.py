from pages1.base_page import Page
from selenium.webdriver.common.by import By


class Shopcategorypage(Page):
    FACE_LINK = (By.XPATH, "//span[contains(text(),'Face')]")
    FACE = (By.XPATH, "//div[@class='list-menu-drawer motion-reduce']//list-menu-item[@data-title='Face']")
    FACE_MOB = (By.XPATH, "//div[@id='link-Shop by Category']//a[contains(text(),'Face')]")

    # "//a[(@href='/collections/face-wash') and (@class='header__menu-item list-menu__item focus-inset')]")
    # //parent::a[contains(@href, '/collections/face')]

    def click_face(self):
        # self.wait_for_element_appear(*self.FACE_LINK)
        # self.all_category_page = self.find_elements(*self.FACE_LINK)
        # self.wait
        # self.all_category_page[1].click()
        self.wait_for_element_click(*self.FACE)

    def click_face_mob(self):
        self.wait_for_element_click(*self.FACE_MOB)
