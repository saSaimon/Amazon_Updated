from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ORDER_BUTTON = (By.CSS_SELECTOR, 'a[href="/gp/css/order-history?ref_=nav_orders_first"]')
SIGNIN_HEADER = (By.CSS_SELECTOR, 'h1.a-spacing-small')
EMAIL_FIELD = (By.CSS_SELECTOR, '#ap_email')

@given('Open https://www.amazon.com')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')

@when('Click Orders')
def clcik_orders(context):
    context.driver.find_element(*ORDER_BUTTON).click()


@then('Verify Sign in page opened: Sign In header is visible, email input field is present')
def verify_signin_opens(context):
   actual_text =  context.driver.find_element(*SIGNIN_HEADER).text
   expected_text = "Sign in"
   assert actual_text == expected_text, f'Expected text should be {expected_text} but got {actual_text}'
   context.driver.find_element(*EMAIL_FIELD).is_displayed()
