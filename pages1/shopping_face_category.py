from pages1.base_page import Page
from selenium.webdriver.common.by import By
from support.logger import logger


class Shoppingface(Page):
    # TITLE_PAGE = (By.XPATH, "//*[@property = 'og:title' and @content ='Face']")
    TITLE_PART = (By.XPATH, "//*[@content = 'https://shop.cureskin.com/collections/face']")
    PRODUCTS = (By.XPATH, "//div[@id = 'ProductGridContainer']//li")
    PRODUCT_TITLE = (By.XPATH, "//div[@class ='product__title']")

    def verify_title(self, expected_text):
        # self.verify_url_contains_query(*self.TITLE_PAGE)
        self.wait_for_element_appear(*self.TITLE_PART)
       # self.verify_partial_text(expected_text, *self.TITLE_PART)
        self.verify_url_contains_query(expected_text)
        logger.info(f"Verifying the title displayed with Face ")

    def verify_product_name(self, expected_result):
        self.all_products_inpage = self.find_elements(*self.PRODUCTS)
        self.all_products_inpage[0].click()
        self.verify_partial_text(expected_result, *self.PRODUCT_TITLE)
        logger.info(('Item have Face text in it'))
