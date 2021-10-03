from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"
def calc(x, y):
  return str(int(x) + int(y))

try:
 browser = webdriver.Chrome() 
 browser.get(link)
 time.sleep(1)
 x = browser.find_element_by_id("num1").text
 y = browser.find_element_by_id("num2").text
 result = calc(x,y)
 select = Select(browser.find_element_by_tag_name("select"))
 select.select_by_value(result )
 button = browser.find_element_by_css_selector('.btn')
 button.click()
finally:
 time.sleep(30)
 browser.quit()