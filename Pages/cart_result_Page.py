from selenium.webdriver.common.by import By
from Pages.base_page import Page
from selenium.webdriver.support.ui import Select

class CartResultPage(Page):
    PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
    SELECTED_DEPARTMENT_CATEGORY = (By.CSS_SELECTOR, "#nav-subnav[data-category='electronics")
    SELECTED_DEPARTMENT_CATEGORY_TEXT = (By.CSS_SELECTOR, '#nav-subnav [href="/electronics-store/b/?ie=UTF8&node=172282&ref_=topnav_storetab_e"] .nav-a-content')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CART_ITEM = (By.CSS_SELECTOR, '[class="sc-without-multicart"]')
    SELECT_TEXT = (By.CSS_SELECTOR, '[id="swm-link"]')


    def click_first_product(self):
        self.wait_for_element_click(*self.PRODUCT_RESULT)

    def verify_cart_result_page(self, result_word):
        self.verify_partial_text(result_word, *self.CART_ITEM)

    def verify_department(self):
        self.wait_for_element_appear(*self.SELECTED_DEPARTMENT_CATEGORY)
        self.verify_partial_text('Electronics', *self.SELECTED_DEPARTMENT_CATEGORY_TEXT)

    def add_to_cart_button(self):
            self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def verify_search_select(self, expected_text):
        self.verify_partial_text(expected_text, *self.SELECT_TEXT)



