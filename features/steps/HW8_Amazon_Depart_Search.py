from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.main_page.select_department(alias)


@when('Search for {search_item}')
def input_amazon_search(context, search_item):
    context.app.main_page.input_amazon_search(search_item)
    context.app.main_page.click_amazon_search_icon()

@then('Verify electronics department is selected')
def verify_department(context):
    context.app.cart_result_page.verify_department()

@then('Verify {search_text} after Search')
def verify_products(context, search_text):
    context.app.cart_result_page.verify_search_select(search_text)
