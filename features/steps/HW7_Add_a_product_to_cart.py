from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')


@when('Input {input_value} into Amazon search field')
def input_amazon_search(context, input_value):
    context.app.main_page.input_amazon_search(input_value)


@when('click on Amazon search icon')
def click_search_amazon(context):
    context.app.main_page.click_amazon_search_icon()


@when('Click on the first product')
def click_first_product(context):
   context.app.cart_result_page.click_first_product()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.cart_result_page.add_to_cart_button()


@then('Verify cart has {expected_count} Item')
def verify_cart_count(context, expected_count):
    context.app.cart_result_page.verify_cart_result_page(expected_count)
