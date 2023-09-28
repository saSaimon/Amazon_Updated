from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


@given('Open Amazon product B074TBCSC8 page')
def open_amazon_product_page(context):
    context.app.product_page.open_amazon_product_page()

@when('Hover over New Arrivals tab')
def hover_New_Arrivals_tab(context):
    context.app.product_page.hover_New_Arrivals_tab()

@then('Verify verifies that the user sees the details')
def verify_user_sees_details(context):
    context.app.product_page.verify_user_sees_details()

@when('Change the location')
def change_location(context):
    context.app.main_page.change_location_amazon_main()

