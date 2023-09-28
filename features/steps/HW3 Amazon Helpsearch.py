from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open amazon help page')
def open_amazonhelp(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input cancel order into amazon helpsearch field')
def input_amazonhelpsearch(context):
    search_field = context.driver.find_element(By.ID, "helpsearch")
    search_field.send_keys('cancel order')

@when('Click on cancel order text')
def click_cancelorder_text(context):
    search_field = context.driver.find_element(By.ID, "helpsearch")
    search_field.send_keys(Keys.ENTER)


@then('Product results for cancel order are shown')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_text = 'Cancel Items or Orders'
    assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'
