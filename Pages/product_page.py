from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from Pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class Productpage(Page):
    NEW_ARRIVALS_TAB = (By.CSS_SELECTOR, 'a[href*="New-Arrivals"]')
    NEW_ARRIVALS_DETAILS = (By.CSS_SELECTOR, "a[href*='fashion-luggage&bbn']")

    def open_amazon_product_page(self):
        self.open_page('https://www.amazon.com/gp/product/B074TBCSC8')

    def hover_New_Arrivals_tab(self):
        new_arrivals_tab = self.find_element(*self.NEW_ARRIVALS_TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_tab)
        actions.perform()

    def verify_user_sees_details(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DETAILS)