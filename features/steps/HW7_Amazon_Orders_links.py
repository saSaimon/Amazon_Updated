from selenium.webdriver.common.by import By
from behave import given, when, then


Amazon_Orders = (By.ID, '#nav-orders')
Sign_in_result = (By.XPATH, "//div[@class='a-box']//h1")
Cart_Icon = (By.ID, '#nav-cart-count')
Cart_Empty = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")


# @given('Open Amazon page')
# def open_amazon(context):
#     context.app.main_page.open_main_page()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.main_page.click_amazon_orders()


@then('Verify Sign In page is opened')
def verify_Sign_in_page(context):
    context.app.sign_in_page.verify_Sign_in_page()






# @given('Open Amazon page')
# def open_amazon(context):
#     context.app.main_page.open_main_page()


@when('Click on cart icon')
def click_amazon_Cart_Icon(context):
    context.app.main_page.click_amazon_Cart_Icon()


@then('Verify {empty_text} text present')
def verify_cart_reslt_page(context, empty_text):
    context.app.cart_empty.verify_cart_result_page(empty_text)

