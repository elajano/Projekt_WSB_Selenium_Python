from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome()
driver.get('https://poland4weekend.com')
time.sleep(2)
#button_accept_cookies = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/button[1]')
#button_accept_cookies.click()
#time.sleep(4)

search_field = driver.find_element('css selector' ,'#acp_magento_search_id_main_page')
search_field.send_keys('Krakow')
time.sleep(2)
search_field.send_keys(Keys.ENTER)

'''
search_button.submit()
driver.get_screenshot_as_file('screen.png')
time.sleep(3)
driver.quit()

#//*[@id="acp_magento_search_id_main_page"]

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://www.poland4weekend.com/')


    # manipulacja obiektem inputbox 
elem = driver.find_element("xpath",'//*[@id="acp_magento_search_id_main_page"]')
elem.clear()
elem.send_keys("Krakow")
elem.send_keys(Keys.RETURN)

assert driver.find_element("xpath",'//*[@id="acp_magento_search_id_main_page"]').text == "Krakow"

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Setup chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.set_window_size(500, 500)

# Navigate to the url
driver.get('https://www.poland4weekend.com/')
time.sleep(3)

search_field = driver.find_element(By.CLASS_NAME, 'search-box typing_box')
# search_field = driver.find_element(By.ID, )
time.sleep(3)
driver.save_screenshot("search.png")
search_field.send_keys('Krakow')
time.sleep(3)
search_field.send_keys(Keys.RETURN)


# Take a screenshot before entering a value
driver.save_screenshot("screenshot_1.png")
time.sleep(2)
# Enter a value in the input text field
input_text_fname.send_keys("Krakow")
time.sleep(2)
# Take a screenshot after entering a value
driver.save_screenshot("screenshot-2.png")

# Close the driver
driver.quit()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
time.sleep(1)
button1_accept = driver.find_element('id','L2AGLb')
button1_accept.click()
search_field = driver.find_element('name','q')
search_field.send_keys('Ile lat ma Mariusz Pudzianowski?')
search_button = driver.find_element('name','btnK')
search_button.submit()
driver.get_screenshot_as_file('screen.png')
time.sleep(3)
driver.quit()'''
