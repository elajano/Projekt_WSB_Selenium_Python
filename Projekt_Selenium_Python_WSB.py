from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

#pokaż stopkę
link = driver.find_element('xpath','//*[@id="bgLayers_comp-jsugpnao"]/div[1]')
webdriver.ActionChains(driver).move_to_element(link).perform()
time.sleep(3)
#zrób zdjęcie stopki
driver.get_screenshot_as_file('footer_screenshot.png')

#xpath do FB
driver.find_element('xpath', '//*[@id="img_0_comp-jsugpnbl"]/img')
button_fb = driver.find_element('xpath', '//*[@id="img_0_comp-jsugpnbl"]/img')
button_fb.click()
assert button_fb is not None
print ("Link do strony FB jest aktywny")
if link_FB == "https://www.facebook.com/Poland4Weekend/":
    print ("Link do profilu na Facebook jest poprawny")
time.sleep (3)

#xpath do Twitter
driver.find_element('xpath', '//*[@id="img_1_comp-jsugpnbl"]/img')
button_tw = driver.find_element('xpath', '//*[@id="img_1_comp-jsugpnbl"]/img')
button_tw.click()
assert button_tw is not None
print ("Link do strony Twitter jest aktywny")
time.sleep (5)
if link_Tw == "https://twitter.com/Poland4W":
    print ("Link do profilu na Twitter jest poprawny")
time.sleep (3)

#xpath do Instagram
driver.find_element('xpath', '//*[@id="img_2_comp-jsugpnbl"]/img')
button_in = driver.find_element('xpath', '//*[@id="img_2_comp-jsugpnbl"]/img')
button_in.click()
assert button_in is not None
print ("Link do strony Instagram jest aktywny")
time.sleep (5)
if link_In == "https://www.instagram.com/poland4weekend/":
    print ("Link do profilu na Instagram jest poprawny")
time.sleep (3)



'''

search_field = driver.find_element('id', 'grey')
search_field.send_keys('warszawa')
search_button = driver.find_element('xpath','//*[@id="acp_magento_search_id_main_page"]')
search_button.submit()
driver.get_screenshot_as_file('screen.png')
time.sleep(3)'''


driver.quit()
