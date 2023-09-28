from selenium.webdriver.common.by import By
from behave import given, when, then


bestsellers = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")


@given('Open amazon bestsellers page')
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('verify 5 links are displayed')
def verify_links(context):
    actual_links = context.driver.find_elements(*bestsellers)
    assert len(actual_links) == 5, f'expected 5 links but we see {len(actual_links)}'

