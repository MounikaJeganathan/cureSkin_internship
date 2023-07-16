from pages1.main_page_cure import MainPagecure
from pages1.header_cure import Headercure
from pages1.shop_category_page import Shopcategorypage
from pages1.shopping_face_category import Shoppingface


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page_cure = MainPagecure(self.driver)
        self.header_cure = Headercure(self.driver)
        self.shop_category_page = Shopcategorypage(self.driver)
        self.shopping_face_category = Shoppingface(self.driver)
