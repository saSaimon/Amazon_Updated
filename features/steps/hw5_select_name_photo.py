from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULT = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, '[class="a-size-base-plus a-color-base a-text-normal"]')
PRODUCT_IMG = (By.CSS_SELECTOR, '[class="a-link-normal s-no-outline"] [class="s-image"]')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

# @when('Search for {search_query}')
# def search_amazon(context, search_query):
#     context.driver.find_element(*SEARCH_FILED).send_keys(search_query)
#     context.driver.find_element(*SEARCH_BTN).click()

@then('Verify that every product has a name and image')
def verify_product_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULT)
    print(all_products)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Title should not be blank'
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image should not be blank.'
        print(product.find_element(*PRODUCT_IMG).get_attribute("src"))