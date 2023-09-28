from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_url(self, url=''):
        print(f'Opening URL: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Checking by locator {locator}. Expected text {expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))


    # def verify_text(self, expected_text: str, *locator):
    #     """
    #     Search for a webelement, get its text, compare with expected_text
    #     :param expected_text: Text to be in webelement
    #     :param locator: Search strategy and locator of webelemnt (ex. (By.ID, 'id') )
    #     """
    #     actual_text = self.driver.find_element(*locator).text
    #     assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"