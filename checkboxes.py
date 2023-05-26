'''
Let's use the demo website "https://the-internet.herokuapp.com/checkboxes" to test the checkboxes functionality with Selenium 4 in Python. 
This website has two checkboxes that you can select and deselect.

REMEMBER! INSTALL SELENIUM IN VIRTUAL ENVIRONEMNT!

python -m venv .venv
.\.venv\Scripts\activate

pip install selenium

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the browser
browser = webdriver.Chrome()

# Open the checkboxes page
browser.get("https://the-internet.herokuapp.com/checkboxes")

# Locate the checkboxes
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")

# Check the first checkbox
checkboxes[0].click()
assert checkboxes[0].is_selected()
