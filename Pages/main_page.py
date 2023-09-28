from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from Pages.base_page import Page


class MainPage(Page):
    Amazon_Orders = (By.CSS_SELECTOR, '[href="/gp/css/order-history?ref_=nav_orders_first"]')
    # Cart_Icon = (By.ID, '#nav-cart-count')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'select.nav-search-dropdown')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[href="/gp/cart/view.html?ref_=nav_cart"]')

    def open_main_page(self):
        self.open_page('https://www.amazon.com/')

    def input_amazon_search(self, input_value):
        self.input_text(input_value, *self.SEARCH_FIELD)

    def click_amazon_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def select_department(self, alias: str):
        drop_down = self.find_element(*self.SEARCH_DROPDOWN)
        select = Select(drop_down)
        select.select_by_visible_text(alias)
        assert 'Electronics' == alias

    def click_amazon_Cart_Icon(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_amazon_orders(self):
        self.click(*self.Amazon_Orders)

    def change_location_amazon_main(self):
        self.driver.find_element(By.CSS_SELECTOR, '#nav-global-location-slot').click()
        self.driver.find_element(By.CSS_SELECTOR, '[class="a-button-dropdown a-button a-button-span12"').click()
        self.driver.find_element(By.CSS_SELECTOR, '#GLUXCountryList_234').click()
        self.driver.refresh()
