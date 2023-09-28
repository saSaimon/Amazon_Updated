from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()

@when('Input key chain into Amazon search field')
def input_amazon_search(context, SEARCH_FIELD):
    context.app.main_page.click_amazon_search(SEARCH_FIELD)


@when('click on Amazon search icon')
def click_search_amazon(context):
    context.app.main_page.click_search_amazon()


@when('Click on the first product')
def click_first_product(context):
    context.app.main_page.click_first_product()
    context.app.main_page.wait.until_first_product(5)


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.main_page.click_add_cart()
    context.app.main_page.wait.until_add_cart(5)

@then('Verify cart has {expected_count} Item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count}'


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    e = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
    e.click()


@then('Verify cart has {expected_count} Item')
def verify_cart_count(context, cart):
    context.app.cart_show_item.verify_cart_show_item(PRODUCT_RESULT)

