import selenium
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.poland4weekend.com")

elements = driver.find_elements(By.TAG_NAME, "h1" )

for element in elements:
    print ("homepage H1")
    print(element.text)
  
    