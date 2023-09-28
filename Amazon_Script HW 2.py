from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/help/customer/display.html ')

search_field = driver.find_element(By.ID, "helpsearch")
search_field.send_keys('cancel order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'

driver.quit()
