from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

# @given('Open amazon page')
# def open_amazonhelp(context):
#     context.driver.get('https://www.amazon.com/')


@when('Click on Amazon shopping cart icon')
def click_amazon_shoppingcart(context):
    search_icon = context.driver.find_element(By.ID, 'nav-cart-count-container')
    search_icon.click()


@then('Product results shopping cart is empty are shown')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = 'Your Amazon Cart is empty'
    assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'
