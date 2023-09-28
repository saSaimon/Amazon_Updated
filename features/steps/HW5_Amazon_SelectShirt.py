from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTION = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')



@given('Open Amazon Shirt {page_num} page')
def verify_amazon_shirt_page(context, page_num):
    context.driver.get(f'https://www.amazon.com/gp/product/{page_num}/')





@then('Verify user can click through colors')
def verify_can_select_colors(context):
    expected_colors = ["0510-black Grey Green Navy Blue", "0510-black White Green Navy Red", "590-black Grey Green", "590-black Grey Navy"]
    colors = context.driver.find_elements(*COLOR_OPTION)
    actual_colors = []

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*SELECTED_COLOR).text
        actual_colors += [current_color]
    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'

