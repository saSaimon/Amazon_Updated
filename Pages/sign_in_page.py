from selenium.webdriver.common.by import By
from Pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class Signinpage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_Sign_in_page(self):
        actual_text = self.find_element(*self.SIGN_IN_TEXT).text
        print(actual_text)
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        assert "Sign in" == actual_text, f'Sign In page did not open'



