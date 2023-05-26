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
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Zezwól na wszystkie pliki cookie']"))).click()
time.sleep (3)
# driver.get("www.facebook.com")
# driver.find_elements_by_xpath("//button[contains(string(), 'Zezwól na wszystkie pliki cookie')]")[0].click()
'''
button_accept_cookies_fb = driver.find_element('xpath','//*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]')
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1] - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1] - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1] - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div
button_accept_cookies_fb.click()'''

driver.get_screenshot_as_file('fb_screenshot.png')
def link_FB():
    if link_FB == "https://www.facebook.com/Poland4Weekend/":
        return link_FB
        print ("link do profilu strony na facebook jest prawidłowy")
    elif link_FB != ("https://www.facebook.com/Poland4Weekend/"):
        return "link do profilu strony na facebook jest nieprawidłowy"
        print ("link do profilu strony na facebook jest nieprawidłowy")
    
print("mama")
#xpath do Twitter
driver.find_element('xpath', '//*[@id="img_1_comp-jsugpnbl"]/img')
button_tw = driver.find_element('xpath', '//*[@id="img_1_comp-jsugpnbl"]/img')
button_tw.click()
time.sleep (5)

#xpath do Instagram
driver.find_element('xpath', '//*[@id="img_2_comp-jsugpnbl"]/img')
button_in = driver.find_element('xpath', '//*[@id="img_2_comp-jsugpnbl"]/img')
time.sleep (5)



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

'''link = driver.find_element('xpath','//*[@id="main-page-didyouknow"]/p[2]/i[1]/b/a')
webdriver.ActionChains(driver).move_to_element(link).perform()
driver.quit()'''
driver.quit()