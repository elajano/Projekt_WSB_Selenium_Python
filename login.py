from selenium import webdriver

driver = webdriver.Chrome()

driver.get("")

user_name = driver.find_element('id', 'username')
user_name.send_keys('abcdefg')

pass_field = driver.find_element('id', "password")
pass_field.send_keys('mypassword')

submit_btn = driver.find_element('css selector','#customer_login......')
submit_btn.click()


