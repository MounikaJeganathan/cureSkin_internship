from pages.cart_page import Cart
from pages.header import Header
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_result import SearchResult
from pages.signin_page import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result = SearchResult(self.driver)
        self.signin_page = SignIn(self.driver)
        self.cart_page = Cart(self.driver)
        self.product_page = ProductPage(self.driver)
