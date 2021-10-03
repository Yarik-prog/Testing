from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/cats.html"

try:
 browser = webdriver.Chrome() 
 browser.implicitly_wait(5)
 browser.get(link)

 button = browser.find_element_by_id("button")
 button.click()

finally:
 time.sleep(30)
 browser.quit()