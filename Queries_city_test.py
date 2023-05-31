from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.poland4weekend.com/')

link_FB = "https://www.facebook.com/Poland4Weekend/"
link_Tw = "https://twitter.com/Poland4W"
link_In =  "https://www.instagram.com/poland4weekend/"

time.sleep(2)
button_accept_cookies = driver.find_element('xpath','/html/body/div[2]/div/div/div[1]/button[1]')
button_accept_cookies.click()
time.sleep(2)



    # manipulacja obiektem inputbox 
elem = driver.find_element("xpath",'//*[@id="acp_magento_search_id_main_page"]')
elem.clear()
elem.send_keys("Krakow")
elem.send_keys(Keys.RETURN)

assert driver.find_element("xpath",'//*[@id="acp_magento_search_id_main_page"]').text == "Krakow"

driver.quit()