# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
# ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
# CART = (By.ID, 'nav-cart-count')
#
#
# @when('Input key chain into Amazon search field')
# def input_amazon_search(context):
#     search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
#     search_field.send_keys('key chain')
#
#
# @when('click on Amazon search icon')
# def click_search_amazon(context):
#     search_icon = context.driver.find_element(By.ID, 'nav-search-submit-button')
#     search_icon.click()
#
#
# @when('Click on the first product')
# def click_first_product(context):
#     context.driver.wait = WebDriverWait(context.driver, 5)
#     e = context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_RESULT))
#     e.click()
#
#
# @when('Click on Add to cart button')
# def click_add_to_cart(context):
#     context.driver.wait = WebDriverWait(context.driver, 5)
#     e = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
#     e.click()
#
#
# @then('Verify cart has {expected_count} Item')
# def verify_cart_count(context, expected_count):
#     cart_count = context.driver.find_element(*CART).text
#     assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count}'
