from Pages.main_page import MainPage
from Pages.sign_in_page import Signinpage
from Pages.cart_result_Page import CartResultPage
from Pages.product_page import Productpage
from Pages.cart_empty import CartEmptyPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.cart_result_page = CartResultPage(self.driver)
        self.product_page = Productpage(self.driver)
        self.sign_in_page = Signinpage(self.driver)
        self.cart_empty = CartEmptyPage(self.driver)
