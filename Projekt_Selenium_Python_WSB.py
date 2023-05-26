from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.poland4weekend.com/')
time.sleep(2)
button_accept_cookies = driver.find_element('xpath','/html/body/div[2]/div/div/div[1]/button[1]')
button_accept_cookies.click()
time.sleep(2)

#pokaż stopkę
link = driver.find_element('xpath','//*[@id="bgLayers_comp-jsugpnao"]/div[1]')
webdriver.ActionChains(driver).move_to_element(link).perform()
#zrob zdjecie stopki
driver.get_screenshot_as_file("screen_footer.png")
time.sleep(3)


#xpath do FB
driver.find_element('xpath', '//*[@id="img_0_comp-jsugpnbl"]/img')
button_fb = driver.find_element('xpath', '//*[@id="img_0_comp-jsugpnbl"]/img')
button_fb.click()

#xpath do Twitter
driver.find_element('xpath', '//*[@id="img_1_comp-jsugpnbl"]/img')
button_tw = driver.find_element('xpath', '//*[@id="img_1_comp-jsugpnbl"]/img')
button_tw.click()

#xpath do Instagram
driver.find_element('xpath', '//*[@id="img_2_comp-jsugpnbl"]/img')
button_in = driver.find_element('xpath', '//*[@id="img_2_comp-jsugpnbl"]/img')




'''elem = driver.find_element('id', 'blog')
elem.clear()
elem.send_keys("Krakow")
elem.send_keys(Keys.RETURN)

driver.quit()

search_field = driver.find_element('id', 'grey')
search_field.send_keys('warszawa')
search_button = driver.find_element('xpath','//*[@id="acp_magento_search_id_main_page"]')
search_button.submit()
driver.get_screenshot_as_file('screen.png')
time.sleep(3)'''

driver.quit()