from selenium.webdriver.common.by import By
from Pages.base_page import Page


class CartEmptyPage(Page):
    CART_TEXT = (By.CSS_SELECTOR, '[class="a-row sc-your-amazon-cart-is-empty"]')

    def verify_cart_result_page(self, empty_text):
        # actual_text = empty_text
        actual_text = self.find_element(*self.CART_TEXT).text
        assert "Your Amazon Cart is empty" in actual_text, f"{actual_text} is not matched with {empty_text}."
