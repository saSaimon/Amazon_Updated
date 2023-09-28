from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, 'ul li [href*="tab"]')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')
BEST_SELLERS_BUTTON = (By.CSS_SELECTOR, '#nav-xshop-container [href*="bestsellers"]')

@given('Open amazon Best Sellers top icon page')
def open_bestsellers_top_icon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when('Click Amazon Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS_BUTTON).click()

@then('Verify Best Sellers 5 links are visible')
def verify_BestSellers_links_present(context):
    best_sellers_links = context.driver.find_elements(*BEST_SELLERS_LINKS)
    expected_text = ["Amazon Best Sellers", "Amazon Hot New Releases", "Amazon Movers & Shakers", "Amazon Most Wished For", "Amazon Gift Ideas"]

    for x in range(len(best_sellers_links)):
        link = context.driver.find_elements(*BEST_SELLERS_LINKS)[x]



        link.click()

        header_text = context.driver.find_element(*HEADER).text
        print(header_text)
        assert header_text in expected_text, f" We are expecting {header_text} but we are not getting it."


"""
Another way to fix this problem

def verify_each_windows_with_its_title(context):
    expected_titles = ["Amazon Best Seller", "Amazon Hot New Release", "Amazon Movers & Shakers",
                       "Amazon Most Wished For", "Amazon Gift Ideas"]
    menu_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    no_of_menue = len(menu_links)
    for i in range(no_of_menue):
        menu_links[i].click()
        menue_title = context.driver.find_element(*MENUE_TITLE_DESCR).text
        assert menue_title in expected_titles
        print(menue_title)
"""
