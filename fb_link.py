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
driver.get('https://www.facebook.com/')

# button_accept_cookies = driver.find_element('xpath','//*[@id="u_0_k_uJ"]')
# button_accept_cookies = driver.find_element('data-testid','cookie-policy-manage-dialog-accept-button')
# button_accept_cookies = driver.find_element('id','u_0_k_uJ')
# driver.find_elements_by_xpath("//button[contains(string(), 'Zezwól na wszystkie pliki cookie')]")[0].click()
# button_accept_cookies_fb = driver.find_element('xpath','//*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]')
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1] - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1] - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1] - nie dziala
# //*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Zezwól na wszystkie pliki cookie']"))).click()
# button_accept_cookies = driver.find_element('data-coockiebanner','"accept button"')
# button_accept_cookies.click()
time.sleep(2)

driver.quit()